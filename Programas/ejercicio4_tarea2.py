

# ======================================================================
# Archivo: ejercicio4_tarea2.py
# Curso: SOFT-01 - Principios de Programación 1
# Alumno: Jorge Chavarría Ramírez
# Fecha: 22/11/2026
# Descripción: Ejercicio 4. Control de abastecimiento de una expedición
# ======================================================================

# Declaración e inicialización de variables
AGUA_INICIAL = 150
ALIMENTO_INICIAL = 100
JORNADAS_MINIMAS = 1
JORNADAS_MAXIMAS = 30
agua_disponible = AGUA_INICIAL
alimento_disponible = ALIMENTO_INICIAL
agua_consumida_total = 0
alimento_consumido_total = 0
dias_completados = 0
expedicion_interrumpida = False

# Entrada de datos de jornadas e inicialización de ciclo while
jornadas_planeadas = int(input(f"Ingrese la cantidad de jornadas (de {JORNADAS_MINIMAS} a {JORNADAS_MAXIMAS}): "))

while jornadas_planeadas < JORNADAS_MINIMAS or jornadas_planeadas > JORNADAS_MAXIMAS:
    print(f"Error: La cantidad de jornadas debe estar entre {JORNADAS_MINIMAS} y {JORNADAS_MAXIMAS}.")
    jornadas_planeadas = int(input(f"Ingrese nuevamente la cantidad de jornadas: "))

# Inicia ciclo for como un contador de días
for dia in range(1, jornadas_planeadas + 1):
    # Verificación de recursos antes de iniciar una jornada
    if agua_disponible == 0 or alimento_disponible == 0:
        expedicion_interrumpida = True
        break
    print(f"Jornada {dia} de {jornadas_planeadas}")
    print(f"Inventario actual: Agua = {round(agua_disponible, 2)} L, Alimento = {round(alimento_disponible, 2)} unidades")

    # Verificación del consumo de agua con input del usuario
    consumo_agua = float(input("Ingrese el consumo de agua de hoy en L: "))
    while consumo_agua <= 0 or consumo_agua > agua_disponible:
        print(f"Error: El consumo debe ser mayor a 0 y no exceder los {round(agua_disponible, 2)} L")
        consumo_agua = float(input("Ingrese nuevamente el consumo de agua en L: "))

    # Verificación del consumo de alimento con input del usuario
    consumo_alimento = int(input("Ingrese el consumo de alimento de hoy en unidades: "))
    while consumo_alimento <= 0 or consumo_alimento > alimento_disponible:
        print(f"Error: El consumo debe ser mayor a 0 y no exceder las {round(alimento_disponible, 2)} unidades disponibles.")
        consumo_alimento = int(input("Ingrese nuevamente el consumo de alimento (unidades): "))

    # Cálculos para actualizar inventario de recursos
    agua_disponible -= consumo_agua
    alimento_disponible -= consumo_alimento
    agua_consumida_total += consumo_agua
    alimento_consumido_total += consumo_alimento

    dias_completados += 1
    print(f"Saldo restante: Agua = {round(agua_disponible, 2)} L, Alimento = {round(alimento_disponible, 2)} unidades")

    # Se interrumpe la jornada si algun recurso es igual a 0
    if agua_disponible == 0 or alimento_disponible == 0:
        if dia < jornadas_planeadas:
            print("¡ALERTA! Uno de los recursos se ha agotado. No es posible continuar a la siguiente jornada.")
            expedicion_interrumpida = True
        break

# Se calculan los promedios de consumo y se imprimen salidas e informe
promedio_agua = agua_consumida_total // dias_completados
promedio_alimento = alimento_consumido_total // dias_completados

if expedicion_interrumpida:
    estado_mision = "Interrumpida anticipadamente por agotamiento de suministros"
else:
    estado_mision = "Completada exitosamente según lo planificado"

print()
print(f"Estado de la expedición: {estado_mision}")
print(f"Días completados: {dias_completados} de {jornadas_planeadas}")
print(f"Agua total consumida: {round(agua_consumida_total, 2)} L")
print(f"Alimento total consumido: {alimento_consumido_total} unidades")
print(f"Agua restante: {round(agua_disponible, 2)} L")
print(f"Alimento restante: {alimento_disponible} unidades")
print(f"Promedio diario agua: {round(promedio_agua, 2)} L por día")
print(f"Promedio diario alimento: {promedio_alimento} unidades por día")