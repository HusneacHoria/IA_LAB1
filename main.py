from distances.manhattan import citire_vectori, manhattan_manual, manhattan_scipy


def main() -> None:
    x, y = citire_vectori("input.txt")

    d_manual = manhattan_manual(x, y)

    print("Vector X:", x)
    print("Vector Y:", y)
    print("Manhattan (manual):", d_manual)

    try:
        d_scipy = manhattan_scipy(x, y)
        print("Manhattan (SciPy cityblock):", d_scipy)
    except Exception as e:
        print("Nu am putut calcula cu SciPy:", e)


if __name__ == "__main__":
    main()
