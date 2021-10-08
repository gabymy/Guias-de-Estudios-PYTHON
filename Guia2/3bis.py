print('==============================')
print('Comprobador de años bisiestos')
print('==============================')


def es_bisiesto():
    anio = int(input('Escribi el año, descubri si fue bisiesto:   '))

    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                print('El año elegido', anio, 'ES BISIESTO')
        else:
            print('El año elegido', anio, 'NO ES BISIESTO')


es_bisiesto()
