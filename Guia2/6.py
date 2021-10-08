# Crear una función que recibe dos números y devuelve "mayor" si el primer número es
# mayor que el segundo, "menor", o "iguales".


def compara(num1=0, num2=0):
    num1 = int(input('ingrese número: '))
    num2 = int(input('ingrese otro número: '))

    if num1 > num2:
        print(num1 + ' es mayor')
    elif num1 < num2:
        print(num1 + 'es menor ')
    elif num1 == num2:
        print('Ambos son iguales')


compara(num1=0, num2=0)
