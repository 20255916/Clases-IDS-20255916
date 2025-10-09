#2

dias= ["lunes", "martes", "miercoles", "jueves", "viernes"] 
lu = int(input("Lunes: "))
dias[0] = lu 
print(dias) 
ma = int(input("Martes: "))
dias[1] = ma
print(dias) 
mie = int(input("Miercoles: "))
dias[2] = mie
print(dias) 
jue = int(input("Jueves: "))
dias[3] = jue
print(dias)
vie = int(input("VIernes: "))
dias[4] = vie
print(dias)
print(f"la produccion de la semana fue {lu+ma+mie+jue+vie}")