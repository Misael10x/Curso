def energia_nivel_hidrogeno():
    n = int(input("Introduce el número cuántico principal (n ≥ 1): "))
    if n < 1:
        print("\nEl número cuántico debe ser mayor o igual a 1.")
        return

    E = -13.6 / (n ** 2)
    print(f"\nEnergía del nivel n={n}: {E:.2f} eV")

if __name__ == "__main__":
    energia_nivel_hidrogeno()
