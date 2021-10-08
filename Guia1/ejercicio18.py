#Resolucion GUIA Nº1
#01/08/2021
#Crear un programa que pida al usuario una palabra
#Mostrar por pantalla una a una las letras de la palabra introducida empezando por la última

palabra = input('Escribe una palabra:  ')
for i in range(len(palabra) -1, -1, -1):#len calcula el numero de caracteres, en este caso desde el input. -1 indica posicion
    print(palabra[i])
    
    
#[star =0: stop =len(obj):step=1] slice
#reversed metodo que da vuelta la palabra
#:: funciona como comas
    