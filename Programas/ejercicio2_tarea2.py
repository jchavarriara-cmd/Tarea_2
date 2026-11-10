

consumo_total = 0
consumo_mayor = 0
dias_superior_150 = 0

for dia in range(1, 8):
    consumo = int(input(f"Ingrese el consumo del día {dia} en litros: "))
    consumo_total += consumo
    if consumo > consumo_mayor:
        consumo_mayor = consumo
    if consumo > 150:
        dias_superior_150 += 1

promedio = consumo_total / 7

print()
print(f"Consumo total: {consumo_total} litros")
print(f"Promedio diario: {round(promedio, 2)} litros")
print(f"Mayor consumo: {consumo_mayor} litros")
print(f"Días con consumo superior a 150 litros: {dias_superior_150}")