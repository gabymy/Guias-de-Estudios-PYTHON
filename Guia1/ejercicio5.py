#Resolucion GUIA Nº1
#01/08/2021
#Preguntar nombre del usuario <noombre> <n> tienen que estar en variable
#Imprimir cantidad de letras

nombre = input('Por favor, introduce tu nombre ')
#Upper devuelve todos los caracteres en mayusculas. Ignora simbolos y numeros.
#Asi reconoce si escriben en mayusculas o minusculas
print(nombre.upper()  +    ' tiene  '  + str(len(nombre))  +  ' letras ')
#len: devuelve el numero de elementos de un objeto.


#cont = 0
#for letra in nombre:
#    cont += 1
#print(f'{nombre} tiene {cont} letras')    