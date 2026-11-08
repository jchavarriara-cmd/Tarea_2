

print("CONTROL DE TEMPERATURA")

temperatura_inicial = float(input("Ingrese la temperatura inicial (°C): "))
temperatura_objetivo = float(input("Ingrese la temperatura objetivo (°C): "))
incremento = float(input("Ingrese el incremento por ciclo (°C): "))

if temperatura_objetivo <= temperatura_inicial:
    print("Error: la temperatura objetivo debe ser mayor que la inicial.")

elif incremento <= 0:
    print("Error: el incremento debe ser mayor que cero.")

else:

    temperatura_actual = temperatura_inicial
    ciclos = 0

    print()
    print("Simulación de calentamiento: ")

    while temperatura_actual < temperatura_objetivo:

        temperatura_actual = temperatura_actual + incremento
        ciclos = ciclos + 1

        print(f"Ciclo: {ciclos}, temperatura: {temperatura_actual} °C")

    print()
    print("RESULTADOS")
    print(f"Temperatura final: {temperatura_actual} °C")
    print(f"Total de ciclos: {ciclos}")