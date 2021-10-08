#Resolucion GUIA Nº1
#01/08/2021
#Pedir al usuario dos números y muestre por pantalla su división. 
#Si el divisor es cero, el programa debe devolver un mensaje indicando que no se puede dividir por 0.

numero = float(input('Dividendo:  '))
numero_dos = float(input('Divisor:  '))
if numero_dos == 0:
    print('Prueba de nuevo. No se puede dividir por 0')
else:
    print(numero/numero_dos)    
    

