#Resolucion GUIA Nº1
#01/08/2021
#Almacenar contraseña en una variable
#Preguntar al usuario por la contraseña
#Imprimir si la contraseña introducida por el usuario coincide con la guardada en la variable.

basic = 'contraseña'#almacenar en variable
password = input('Introduce la contraseña:  ')
if basic == password.lower(): #lower: convierte todos los caracteres de mayusculas a minusculas. luna=LUNA
  print('La contaseña coincide')
else:
  print('La contraseña no coincide')