# -*- coding: utf-8 -*-
"""fai_video.py <copione.py> [--verticale] [--prova] [--solo id1,id2] [--voce NOME] [--tieni-media]

Fa tutto: voce (edge-tts, in cache) -> controllo del copione -> render Manim -> controllo dello
schermo -> audio a -14 LUFS, sottotitoli, MP4 -> fotogrammi e report in qa/<slug>/ -> pulizia.

  --prova      render veloce a bassa risoluzione; il risultato resta in qa/<slug>/prova.mp4
  --verticale  forza il formato 9:16 (altrimenti vale META["formato"] del copione)
  --solo       rende solo i segmenti indicati (per correggere una scena); implica --prova
  --voce       prova un'altra voce (es. it-IT-GiuseppeMultilingualNeural)
  --solo-voce  sintetizza e controlla il copione, senza render

Python: C:/Users/admin/AppData/Local/Programs/Python/Python312/python.exe, con PYTHONUTF8=1.
"""
import argparse
import importlib.util
import os
import shutil
import sys
import time
from pathlib import Path

QUI = Path(__file__).resolve().parent
sys.path.insert(0, str(QUI))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("copione")
    ap.add_argument("--verticale", action="store_true")
    ap.add_argument("--prova", action="store_true")
    ap.add_argument("--solo", default="")
    ap.add_argument("--voce", default=None)
    ap.add_argument("--solo-voce", action="store_true")
    ap.add_argument("--tieni-media", action="store_true")
    a = ap.parse_args()
    if a.solo:
        a.prova = True

    import videolib as vl

    percorso = Path(a.copione).resolve()
    spec = importlib.util.spec_from_file_location("copione_video", percorso)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    classi = [c for c in vars(mod).values() if isinstance(c, type) and issubclass(c, vl.ScenaBase)
              and c is not vl.ScenaBase and c.__module__ == "copione_video"]
    if len(classi) != 1:
        sys.exit("Il copione deve definire una sola classe che eredita da ScenaBase.")
    Classe = classi[0]
    meta = dict(Classe.META)
    formato = "9:16" if a.verticale else meta.get("formato", "16:9")
    slug = meta["slug"]
    nome_qa = slug + ("_prova" if a.prova else "")
    cartella_qa = vl.QA_DIR / nome_qa
    if cartella_qa.exists():
        shutil.rmtree(cartella_qa, ignore_errors=True)
    cartella_qa.mkdir(parents=True, exist_ok=True)
    media = vl.MEDIA / nome_qa
    vl.imposta_formato(formato, prova=a.prova, media_dir=media)
    F = vl.F
    report = [f"VIDEO {slug}  formato {formato}  {'PROVA' if a.prova else 'FINALE'}  {time.strftime('%Y-%m-%d %H:%M')}", ""]

    # 1. voce ---------------------------------------------------------------
    print("1/4 voce")
    t0 = time.time()
    segmenti = Classe.SEGMENTI
    mancanti = [s.id for s in segmenti if not hasattr(Classe, "seg_" + s.id)]
    if mancanti:
        sys.exit(f"Mancano i metodi seg_<id> per: {', '.join(mancanti)}")
    vl.sintetizza(segmenti, voce=a.voce or meta.get("voce", vl.VOCE), velocita=meta.get("velocita", 0))
    tot = sum(s.durata + s.pausa_dopo for s in segmenti)
    parole = sum(s.n_parole for s in segmenti)
    print(f"  totale {tot:.0f} s, {parole} parole  ({time.time() - t0:.0f} s)")
    report += ["COPIONE", f"  durata prevista {tot:.0f} s, {parole} parole, {len(segmenti)} segmenti"]
    for s in segmenti:
        report.append(f"  {s.id:<16} {s.durata:5.1f} s  {s.n_parole:3d} parole  "
                      f"{60 * s.n_parole / max(s.durata_voce, .1):4.0f} parole/min")
    problemi = vl.controlla_copione(segmenti)
    for g, m in problemi:
        print(f"  {g.upper()}: {m}")
        report.append(f"  {g.upper()}: {m}")
    if not problemi:
        report.append("  nessun problema")
    if a.solo_voce:
        vl.scrivi_report(cartella_qa / "report.txt", report)
        return

    # 2. render -------------------------------------------------------------
    print(f"2/4 render {vl.config.pixel_width}x{vl.config.pixel_height} a {vl.config.frame_rate} fps")
    t0 = time.time()
    scena = Classe()
    scena.cartella_qa = cartella_qa
    scena.solo_segmenti = [x for x in a.solo.split(",") if x] or None
    scena.render()
    t_render = time.time() - t0
    video_muto = Path(scena.renderer.file_writer.movie_file_path)
    durata = scena.time
    print(f"  {durata:.1f} s di video in {t_render:.0f} s")

    # 3. controllo dello schermo ---------------------------------------------
    print("3/4 controllo")
    report += ["", f"SCHERMO (render {t_render:.0f} s per {durata:.0f} s di video)"]
    errori = [q for q in scena.qa if q[0] == "errore"]
    for g, sid, t, msg, _ in scena.qa:
        riga = f"  {g.upper()} [{sid} a {t:.1f} s] {msg}"
        print(riga)
        report.append(riga)
    if not scena.qa:
        report.append("  nessun problema rilevato in automatico")

    # 4. finalizzazione -------------------------------------------------------
    print("4/4 audio, sottotitoli, MP4")
    fatti = [s for s in segmenti if s.t0 is not None]
    wav = cartella_qa / "traccia.wav"
    vl.traccia_audio(fatti, durata, wav)
    if a.prova:
        dest_dir, base = cartella_qa, "prova"
    else:
        dest_dir, base = vl.USCITA / meta["materia"], slug
        dest_dir.mkdir(parents=True, exist_ok=True)
    mp4 = dest_dir / f"{base}.mp4"
    ass = None
    if formato == "9:16":
        ass = cartella_qa / "sottotitoli.ass"
        vl.scrivi_ass(fatti, ass, vl.config.pixel_width, vl.config.pixel_height)
    vl.finalizza(video_muto, wav, mp4, ass=ass)
    n_srt = vl.scrivi_srt(fatti, dest_dir / f"{base}.srt")
    if not a.prova:
        shutil.copyfile(percorso, dest_dir / f"{base}_copione.py")
    info = vl.info_mp4(mp4)
    lufs, tp, _ = vl.misura_loudness(mp4)
    wav.unlink(missing_ok=True)
    report += ["", "FILE", f"  {mp4}",
               f"  {info['larghezza']}x{info['altezza']} a {info['fps']:.0f} fps, {info['mb']:.1f} MB",
               f"  durata video {info['durata_video']:.2f} s, audio {info.get('durata_audio') or 0:.2f} s, traccia audio: {'si' if info['audio'] else 'NO'}",
               f"  volume {lufs:.1f} LUFS, picco {tp:.1f} dBTP, sottotitoli: {n_srt} blocchi"]
    if not info["audio"] or abs(info["durata_video"] - (info.get("durata_audio") or 0)) > 0.25:
        report.append("  ERRORE: durata audio e video diverse o audio assente")
        errori.append("audio")
    if abs(lufs + 14) > 1.0 or tp > -1.0:
        report.append("  AVVISO: volume fuori da -14 LUFS ±1 o picco sopra -1 dBTP")
    fr = vl.estrai_fotogrammi(mp4, cartella_qa / "fotogrammi", ogni=5.0 if formato == "16:9" else 3.0, segmenti=fatti)
    report += ["", "FOTOGRAMMI (da guardare con Read, uno per uno)",
               f"  fine di ogni segmento: {cartella_qa}\\NN_<id>.png",
               *[f"  {f}" for f in fr["fogli"]],
               f"  schermo fermo al massimo {fr['fermo'][0]:.1f} s (da {fr['fermo'][1]:.0f} a {fr['fermo'][2]:.0f} s)"]
    if fr["fermo"][0] > F["fermo_max"]:
        report.append(f"  AVVISO: schermo fermo oltre {F['fermo_max']:.0f} s")
    vl.scrivi_report(cartella_qa / "report.txt", report)
    if not a.tieni_media:
        vl.pulisci_media(media)
        if vl.MEDIA.exists() and not any(vl.MEDIA.iterdir()):
            vl.MEDIA.rmdir()
    print(f"\n{mp4}\n  {info['larghezza']}x{info['altezza']}, {info['durata_video']:.1f} s, {info['mb']:.1f} MB, "
          f"{lufs:.1f} LUFS\n  report: {cartella_qa / 'report.txt'}")
    print(f"  problemi automatici: {len(errori)} errori, {len(scena.qa) - len([q for q in scena.qa if q[0] == 'errore'])} avvisi, "
          f"{len(problemi)} sul copione.  ORA GUARDA I FOTOGRAMMI.")


if __name__ == "__main__":
    main()
