monedas = {
    "Moneda 1": 10,
    "Moneda 2": 5,
    "Moneda 3": 20,
    "Moneda 4": 15,
    "Moneda 5": 8
}

suma_total = sum(monedas.values())

promedio_valor = suma_total / len(monedas)

moneda_mas_valiosa = max(monedas, key=monedas.get)
valor_moneda_mas_valiosa = monedas[moneda_mas_valiosa]

print("Suma total de todas las monedas de oro:", suma_total)
print("Promedio de valor de las monedas:", promedio_valor)
print("Moneda más valiosa:", moneda_mas_valiosa)
print("Valor de la moneda más valiosa:", valor_moneda_mas_valiosa)