# Crear una función que reciba dos palabras y que imprima línea por línea las primeras,
# segundas, etc. letras de ambas palabras. Por ejemplo, llamándola con "Hola" y
# "mundo"

def columnitas(palabra1, pal2):
    if len(palabra1) != len(pal2):
        # max devuelve el valor maximo
        maslargo = max(len(palabra1), len(pal2))
        # just comleta con espacios la plabara mas corta para alcanzar la mas larga
        # por defecto se llena con espacios sino al final podes agregar con que llenarlo 'l'
        pal1 = palabra1.ljust(maslargo)
        pal2 = pal2.ljust(maslargo)

    for a, b in zip(palabra1, pal2):  # zip=asocia dos iterables
        print(a, b)


columnitas("Hola", "mundo")
