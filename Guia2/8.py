# Crear una función que reciba un texto y devuelva el mismo texto pero con cada palabra
# invertida. Por ejemplo, llamándola con "Esto es una prueba", debe devolver "otsE se
# anu abeurp"


def invertir(texto):
    palabras = texto.split()  # El split()método divide una cadena en una lista
    invert = [x[::-1] for x in palabras]
    # El join()método toma todos los elementos en un iterable y los une en una cadena.
    invertirtexto = " ".join(invert)
    return invertirtexto


# assert sirve para hacer comprobaciones
assert invertir("Esto es una prueba") == "otsE se anu abeurp"

# def invertir(frase):
#frase = frase.split()
#frase_dada_vuelta = ()
# for palabra in frase:
#   palabra = palabra[:: -1]
#  frase_dada_vuelta.append(palabra)
#frase = ''.join(frase_dada_vuelta)
# print(frase)

#invertir('esto es una prueba')
