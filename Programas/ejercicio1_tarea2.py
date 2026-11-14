
#============================================================================
# Archivo: ejercicio1_tarea2.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV2
# Alumno: Jorge Chavarría Ramírez
# Fecha: 22/11/2026 
# Descripción: Ejercicio 1. Control de temperatura de una cámara experimental 
#============================================================================


temperatura_inicial = float(input("Ingrese la temperatura inicial en °C: "))
temperatura_objetivo = float(input("Ingrese la temperatura objetivo en °C: "))
incremento = float(input("Ingrese el incremento por ciclo en °C: "))

if temperatura_inicial >= temperatura_objetivo:
    print("Error: temperatura inicial debe ser menor que temperatura objetivo.")
elif incremento <= 0:
    print("Error: el incremento debe ser mayor que cero.")
else:
    temperatura_actual = temperatura_inicial
    ciclos = 0
    print()
    while temperatura_actual < temperatura_objetivo:
        
        temperatura_actual = temperatura_actual + incremento
        ciclos = ciclos + 1
        
        print(f"Ciclo: {ciclos}, temperatura: {temperatura_actual} °C")

print()
print("Resultado:")
print(f"Temperatura final: {temperatura_actual} °C")
print(f"Total de ciclos: {ciclos}")