

#========================================================================
# Archivo: ejercicio3_tarea2.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV2
# Alumno: Jorge Chavarría Ramírez
# Fecha: 22/11/2026 
# Descripción: Ejercicio 3. Administración de un estacionamiento privado 
#========================================================================

# Declaración de las variables
CAPACIDAD = 20
ocupacion = 0
salidas = 0
recaudacion = 0

# Ciclo while para mantener corriendo el menú
while True:
    print()
    print("1. Registrar ingreso")
    print("2. Registrar salida")
    print("3. Consultar ocupación")
    print("4. Consultar recaudación")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    # Registrar el ingreso de vehículos
    if opcion == 1:

        if ocupacion == CAPACIDAD:
            print("No hay espacios disponibles.")

        else:
            ocupacion += 1
            print("Ingreso registrado.")

    # Registrar salida de vehículos
    elif opcion == 2:

        if ocupacion == 0:
            print("No hay vehículos en el estacionamiento.")

        else:
            while True:

                horas = int(input("Ingrese la cantidad de horas : "))

                if horas > 0:
                    break

                print("Las horas deben ser mayores que cero.")

            pago = horas * 800

            ocupacion -= 1
            salidas += 1
            recaudacion += pago

            print("Salida registrada.")
            print(f"Monto cobrado: ${pago}")

    # Consultar ocupación del estacionamiento
    elif opcion == 3:

        libres = CAPACIDAD - ocupacion

        print(f"Espacios ocupados: {ocupacion}")
        print(f"Espacios libres: {libres}")

    # Consultar la recaudación
    elif opcion == 4:

        print(f"Vehículos que han salido: {salidas}")
        print(f"Recaudación total: ${recaudacion}")

    # Sale del ciclo while y presenta salidas
    elif opcion == 5:

        print()
        print(f"Vehículos presentes: {ocupacion}")
        print(f"Salidas procesadas: {salidas}")
        print(f"Recaudación total: ${recaudacion}")

        break

    # Muestra que la opción seleccionada es inválida
    else:
        print("Error: opción inválida.")