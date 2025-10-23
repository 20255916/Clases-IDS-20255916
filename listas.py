"""estructuras de datos:
string, tupla, lista"""

# datos= [1, 2, "tres",["lunes", "martes", "miercoles"]]
# print(datos[-1][-1][3])


nombre= "Antonio"

repetidos = nombre.lower().count("a") #metió en una variable la función de .count para contar cuantas "a"
                                      #hay en "Antonio"

print(repetidos)


#no entiendo una chucha

nombres= ["Ana", "Antonio", "Ana", "Jose"]
r_a= 0
print(nombres.count("Maria"))
r_a= r_a + nombres[0].lower().count("a")
r_a= r_a + nombres[1].lower().count("a")
r_a= r_a + nombres[2].lower().count("a")
r_a= r_a + nombres[3].lower().count("a")
int(r_a)

#int(nombres.index("Ana, 
 #ya es paja
