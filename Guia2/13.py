# . Crear una función que tome una lista de palabras y devuelva cuál es la más larga y
# cuántos caracteres tiene

def palabras(*pals):  # *es para pasar parametros indeterminados
    cant_letras = 0
    palabra_mas_larga = ''
    for palabra in pals:
        cant_carac = len(palabra)
        if cant_carac > cant_letras:
            cant_letras = cant_carac
            palabra_mas_largas = palabra

        elif cant_carac == cant_letras:

            print(
                f'La palabra mas larga es {palabra_mas_largas} y tiene {cant_letras} caracteres')
