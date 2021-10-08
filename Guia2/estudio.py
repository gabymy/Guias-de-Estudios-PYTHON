# Imprimimos el menú en pantalla
import math
from fractions import Fraction
print("""
    1) Herramientas       3) Temperatura
    2) Calculadora        4) Mas...
    """)

# Leemos lo que ingresa el usuario
eligio = input("-Selecciona algo :")

# Según lo que ingresó, código diferente
if eligio == "1":
    print("Listamos otras herramientas")
elif eligio == "2":
    x = 3
    y = 5
    print("x * y = ", x * y)
elif eligio == "3":
    print("Creo que hace frío")
elif eligio == "4":
    print("otra opción")
else:
    print("Opción no válida")


# seleccion de reinicio en el programa para que no se corte
while (True):
    print("""Bienvendido en que te puedo ayudar
    1) Quiero una operación
    2) Salir""")
    opcion = input()
    if opcion == "1":
        a = input('Ingrese valor de A: ')
        b = input('Ingrese valor de B: ')
        c = input('Ingrese valor de C: ')
        if a.isnumeric() and b.isnumeric() and c.isnumeric():
            a = int(a)
            b = int(b)
            c = int(c)
            y = b ** 2 - 4 * a * c
            if y > 0:
                p = (-b + math.sqrt(y)) / (2 * a)
                print(f'X1 = {round(p, 2)} // {Fraction(p)}')
                n = (-b - math.sqrt(y)) / (2 * a)
                print(f'X2 = {round(n,2)} // {Fraction(n)}')
            else:
                print('No tiene resultado real')
        else:
            print("Los parametros introducidos deben ser números vuelva a intentarlo")

    elif opcion == "2":
        print("Que pases un buen dia")
        break
    else:
        print("El Numero introduccido es erroneo")

# eleccion de diferentes opciones y reinicio
menu = '''
Escoja una opción:
    1)Mostrar el contenido de la agenda.
    2)Añadir contacto a agenda.
    3)Salir.
Utilize el numero correspondiente para seleccionar la accion.
> '''

print('Bienvenido a la agenda de contactos')

while True:
    opcion = input(menu)

    if opcion == '1':
        print("Ha seleccionado la opcion 1.")
        agenda = open("agenda.csv")
        print(agenda.read())
        agenda.close()

    elif opcion == '2':
        agenda = open("agenda.csv", "a")
        nombre = input("Introduzca el nombre\n>")
        numero = input("Introduzca el numero\n>")
        agenda.write(nombre)
        agenda.write(",")
        agenda.write(numero)
        agenda.write("\n")
        print("Contacto guardado con exito")
        agenda.close()

    elif opcion == '3':
        print('Hasta pronto...')
        break

    else:
        print("Ha escogido una opcion invalida, intentelo de nuevo.")
