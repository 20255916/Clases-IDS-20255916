#un pequeño sistema de registro de alumnos

#configuracion inicial
alumnos= 0 
lista_alumnos= []
cantidad= int(input("Cuantos alumnos vamos a ingresar?"))

print("Bienvenido a nuestro sistema de control de alumnos")

opcion= input("Elija la opcion (1: Ingresar alumno): ")

for i in range(cantidad):
    alumno= input("Digite nombre del pajarito: ")
    lista_alumnos.append(alumno)

print(lista_alumnos) 
