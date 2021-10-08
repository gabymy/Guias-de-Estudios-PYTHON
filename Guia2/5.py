# Crear una función que pida cuántas listas se quieren crear y las solicite como se
# muestra a a continuación:
print("Generador de listas")

numero = int(input("¿Cuántas listas quiere escribir?   "))


def crea_lista(contador):
    print(f"Cuantas palabras tiene la lista \n",  contador, end="", )
    numero = int(input())
    lista = []
    for i in range(numero):
        print(f"Dígame la palabra \n", i + 1, end="")
        palabra = input()
        lista += [palabra]
    return lista


for i in range(1, numero + 1):
    print(f"La lista", i, "es:\n",  crea_lista(i))
