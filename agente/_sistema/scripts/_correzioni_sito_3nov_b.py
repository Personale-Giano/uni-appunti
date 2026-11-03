"""Seconda tornata del 3 nov: errori trovati dal nuovo lint_bozza.py --contenuti (stesso controllo sulle evidenziazioni)."""
import sys
sys.path.insert(0, r"C:\Users\admin\AppData\Local\Temp\claude\C--Users-admin-Documents-GitHub\b6d55e1f-a35f-4167-b75a-3e32cd15bf7d\scratchpad")
import correzioni_3nov as k
k.C[:] = [
    ("algebra", "cap31.6", "Σ<sub>σ ∈ S_{n</sub>}", "Σ<sub>σ ∈ S<sub>n</sub></sub>"),
    ("matematica-discreta", "cap21.24", "*Matrix*", "<em>Matrix</em>"),
    ("matematica-discreta", "cap29.3", "si capisce *perché* la relazione", "si capisce <em>perché</em> la relazione"),
    ("programmazione", "cap27.2", "(*The Psychology of Computer Programming*, 1971)", "(<em>The Psychology of Computer Programming</em>, 1971)"),
    ("programmazione", "cap12.36", "int** ppX = &amp;pX; pX = *ppX; **ppX = 10;", "<code>int** ppX = &amp;pX; pX = *ppX; **ppX = 10;</code>"),
]
k.BACKUP = k.BACKUP.with_name(k.BACKUP.name + "-b")
if __name__ == "__main__":
    k.main("--applica" in sys.argv)
