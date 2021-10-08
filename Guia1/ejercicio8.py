# Resolucion GUIA Nº1
# 01/08/2021
# Preguntar al usuario una cantidad a invertir, el interés anual y el número de años
# Mostrar el capital obtenido

inversion = float(input('¿Cuanto dinero vas invertir?  '))
interes = float(input('¿Cual es el interes anual ofrecido?  '))
anios = int(input('¿Durante cuantos años vas a tener invertido el dinero?  '))

print('El CAPITAL obtenido despues de tus años de inversion es ' +
      str(round(inversion * (interes / 100+1) ** anios)))

# ROUND devuelve un redondeo. En este caso el entero mas aproximado

# if interes >=1 :
#interes /= 100

#capital_obtenido = capital + capital + intenteres + años
#print(f'El capital obtenido es {capital}')

# NO USAR Ñ NUNCA
