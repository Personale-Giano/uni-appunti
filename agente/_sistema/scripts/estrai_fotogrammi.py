"""Estrae fotogrammi da un video a intervalli regolari (per leggere le lavagne delle registrazioni).
Uso: python estrai_fotogrammi.py VIDEO CARTELLA_OUT [passo_secondi=90] [inizio=0] [fine=fine_video] [larghezza=1600]
"""
import os
import sys

import av

video, out = sys.argv[1], sys.argv[2]
passo = float(sys.argv[3]) if len(sys.argv) > 3 else 90
inizio = float(sys.argv[4]) if len(sys.argv) > 4 else 0
c = av.open(video)
durata = c.duration / 1e6
fine = min(float(sys.argv[5]), durata) if len(sys.argv) > 5 else durata
largh = int(sys.argv[6]) if len(sys.argv) > 6 else 1600
os.makedirs(out, exist_ok=True)
v = c.streams.video[0]
t = inizio
n = 0
while t < fine:
    c.seek(int(t * 1e6), stream=None)
    for fr in c.decode(v):
        if fr.time is not None and fr.time >= t - 0.5:
            im = fr.to_image()
            h = int(im.height * largh / im.width)
            im.resize((largh, h)).save(os.path.join(out, "t%05d.jpg" % int(t)), quality=90)
            n += 1
            break
    t += passo
print(n, "fotogrammi in", out)
