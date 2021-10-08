# Crear una función que pida al usuario 3 números y devuelva cuál es el mayor, cuál es el
# menor y cuál es la media de los 3 números.
print('escribe tres numeros, separados entre si, por comas')
numeros = input()
numeros = []

# Le agregamos 3 números
for i in range(3):
    numero = int(input("Introduce el número #{}: ".format(i + 1)))
    numeros.append(numero)

# Asumir que el mayor es el primero de la lista
mayor = numeros[0]
# Recorrer y comparar
for numero in numeros:
    if numero > mayor:
        mayor = numero
# Imprimir el resultado
print("Mayor:", mayor)


# def numeros(n1, n2, n3):
# mator = max(n1, n2, n3) para saber cual es el maximo numero
# menor = min(n1, n2, n3) idem minimo
# media = sum(n1, n2, n3)/len(n1,n2,n3) sum=suma
#print(f'el mayor en {mayor}, el menor es{menor} y la media es {media:2f}')
