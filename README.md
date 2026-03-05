# IA Lab 01 — Distanța Manhattan (manual + SciPy)

## Ce face proiectul
- Citește 2 vectori din `input.txt` (2 linii, valori separate prin spațiu)
- Calculează distanța Manhattan:
  - manual
  - cu `scipy.spatial.distance.cityblock`

## Instalare și rulare (Windows / VS Code)
1) Deschide folderul proiectului în VS Code
2) Terminal → New Terminal, apoi:

```bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

## Output așteptat (pentru input-ul default)
Manhattan manual: 12  
Manhattan SciPy: 12

## Observație
Dacă folosești Python 3.14.x și ai probleme cu SciPy/debugger, recomand Python 3.12.x.
