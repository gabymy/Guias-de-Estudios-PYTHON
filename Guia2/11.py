# Crear dos funciones: una que permita convertir de segundos a horas, minutos y
# segundos, y la otra que permita convertir de horas, minutos y segundos a segundos.

def s2hms(segs):
    # divmod nos devuelve una tupla, que es cociente, resto de una division
    mins, segs = divmod(segs, 60)
    hrs, mins = divmod(mins, 60)
    print(f'{hrs} {mins} {segs}')


def hms2s(hrs, mins, segs):
    seg = hrs + 3600 + mins + 60 + segs
    print(f'{seg}')
