#Resolucion GUIA Nº1
#01/08/2021
#Crear un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir”.


while True:
    usuario = input('Escribe algo:  ').lower()
    if usuario == 'salir':
        break
    print(usuario)
    
    
    
#rta = input('ingrese una palabra')
# while rta != 'salir':
# print(rta)
#rta = input ('ingrese una palabra o escriba 'salir' para fializar: ').lower()    