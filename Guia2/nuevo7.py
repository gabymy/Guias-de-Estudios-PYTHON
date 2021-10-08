# Hacer un programa que genere un número entero al azar (módulo random) entre 0 y
# 1000, y le vaya pidiendo al usuario que ingrese números enteros para adivinarlo. Si el
# usuario ingresa un número menor que el objetivo, muestra "Es más alto!"; si el usuario
# ingresa uno mayor, muestra "Es más bajo!"; si el usuario acierta, muestra "Viva
# Python!", y termina. Si el usuario no acertó en 7 intentos, que muestre "Alpiste perdiste!"
# y termine.

import random
import time
print('§ Adivina el numero §')

intentosRealizados = 0
numerominimo = 1
numeromaximo = 1000

print('¡Hola!, ¿Como te llamas?  ')
miNombre = input()

print('Bueno, ' + miNombre + ' ¿Jugamos?')
time.sleep(1)
print(f'Estoy pensando en un numero entre ' +
      str(numerominimo) + ' y ' + str(numeromaximo))


numero = random.randint(numerominimo, numeromaximo)


while intentosRealizados < 7:
    print('Intenta adivinar...')
    numerousuario = input()
    numerousuario = int(numerousuario)

    intentosRealizados = intentosRealizados + 1

    if numerousuario < numero:
        print('¡¡¡Es un numero mas alto!!!')

    if numerousuario > numero:
        print('¡¡¡Es un numero mas bajo!!!')

    if numerousuario == numero:
        intentosRealizados = str(intentosRealizados)
        print('Muy bien' + miNombre +
              '¡¡¡Viva Python!!! Lo lograste en ' + intentosRealizados + ' intentos')
        break

if intentosRealizados >= 7:
    # numerousuario != numero:
    numero = str(numero)
    print('¡Alpiste Perdiste! ' + miNombre + ', el numero era ' + numero)
