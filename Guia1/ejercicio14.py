#Resolucion GUIA Nº1
#01/08/2021
#Crear un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

bonificacion = 100000 #datos
inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
puntos = float(input('Escribe tu puntuación:  '))

if puntos == inaceptable:#Clasifiación por niveles de rendimiento
    nivel = 'Inaceptable'
elif puntos == aceptable:
    nivel = 'Aceptable'
elif puntos >= 0.6:
    nivel = 'Meritorio'
else:
    print('No ingreso la puntacion correcta')    

print('Tu nivel de rendimiento es %s' % nivel)
print('Te corresponde cobrar %.2f'  % (puntos * bonificacion))

#if punto_us == 0.0
#bonif *== punto_us
#print(f'rendimiento inaceptable, recibe {bonificacion} pesos')


#if punt_us == 0.0 or punt_us == 0.4 or put_us ==0.6
#bonif *= punt_us
