#Resolucion GUIA Nº1
#01/08/2021
#Preguntar usuario la edad del cliente y mostrar el precio de la entrada. 
#Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 500 y si es mayor de 18 años, 1000.

anios = int(input('Ingrese edad:  '))
if anios <= 4:
    precio = 0
    print('Puedes pasar GRATIS')
    
elif anios <= 18:
 precio = 500
 print('Debes abonar: $', precio)

elif anios >=18:
 precio = 1000
 print('Debes abonar: $', precio)  
 
else:
    print('No ingreso una edad correcta')       