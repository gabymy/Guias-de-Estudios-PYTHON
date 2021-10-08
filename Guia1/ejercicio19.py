#Resolucion GUIA Nº1
#01/08/2021
#Crear un programa en el que se pregunte al usuario por una frase y una letra
#Mostrar el número de veces que aparece la letra en la frase.


frase = input('Escribe una palabra o frase:  ')
letra= i=input('Ahora, escoge una letra de tu frase:  ')
contador = 0
for i in frase.lower:
    if  i == letra:
        contador += 1
        
print( 'La letra que escogiste  '  ,  letra  ,  ' aparece  ' + str(contador) +  ' vez/veces' )

#cont = frase.count(letra)