# Crear una función que pida un año y que escriba si es bisiesto o no. Se recuerda que
# los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los
# múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 2012 es
# bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.
print('Comprobador de años bisiestos')
fecha = int(input("Escriba un año y le diré si es bisiesto: "))


def es_bisiesto(anio):
    return anio % 400 == 0 or (anio % 100 != 0 and anio % 4 == 0)


if es_bisiesto(fecha):
    print("El año", fecha, "es un año bisiesto.")
else:
    print("El año", fecha, "no es un año bisiesto.")
