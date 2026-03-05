from __future__ import annotations

from typing import List, Tuple

try:

    from scipy.spatial.distance import cityblock 
except Exception:
    cityblock = None


def parse_vector(line: str) -> List[float]:
    #parseaza o linie de text intr-un vector numeric
    line = line.strip()
    if not line:
        raise ValueError("Eroare:linie goala,nu se poate construi vectorul.")
    return [float(x) for x in line.split()]


def citire_vectori(path: str) -> Tuple[List[float], List[float]]:
    #citeste doi vectori dintr-un fisier text
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f.readlines() if ln.strip()]

    if len(lines) < 2:
        raise ValueError("Fisierul trebuie sa aiba cel putin 2 linii nenule.")

    x = parse_vector(lines[0])
    y = parse_vector(lines[1])
    return x, y


def manhattan_manual(x: List[float], y: List[float]) -> float:
    #calculeaza distanta manhattan manual
    if len(x) != len(y):
        raise ValueError(
            f"Vectorii trebuie sa aiba aceeasi dimensiune. len(x)={len(x)}, len(y)={len(y)}"
        )

    return sum(abs(a - b) for a, b in zip(x, y))


def manhattan_scipy(x: List[float], y: List[float]) -> float:
    #calculeaza distanta manhattan folosind SciPy
    if cityblock is None:
        raise RuntimeError(
            "SciPy nu este disponibil."
            
        )
    return float(cityblock(x, y))
