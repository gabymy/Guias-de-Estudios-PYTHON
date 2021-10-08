# Crear una función que pida al usuario el ancho y altura de un rectángulo y lo dibuje con
# caracteres producto *
print('==========')
print('Rectangulo')
print('==========')
print()


def rectangulo(caracter='*'):
    altura = int(input('ingresa la altura del rectangulo:  '))
    base = int(input('ingresa la base del rectangulo:  '))

    for i in range(altura):
        print(base * '*')


rectangulo()
