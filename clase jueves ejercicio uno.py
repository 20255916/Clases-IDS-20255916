### Ejercicio 1
# Captura de cantidades

Enero = int(input("Digite las cantidades de Enero: "))
Febrero = int(input("Digite las cantidades de Febrero: "))
Marzo = int(input("Digite las cantidades de Marzo: "))

costo = Enero*1.25+Febrero*1.38+Marzo*1.14

print(costo)
print(f"Las cantidades de enero, febrero y marzo son:")
print(f"{Enero}, {Febrero} y {Marzo} con un costo")
print(f"de ${costo:.2f}")
