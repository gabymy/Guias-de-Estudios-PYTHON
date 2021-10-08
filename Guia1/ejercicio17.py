#Resolucion GUIA Nº1
#01/08/2021
#Crear un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


tabla_desde = 1#arranca en la tabla del uno
tabla_hasta = 10 #recorre las tablas hasta la del diez
desde = 1 #empieza multiplicar desde el uno
hasta = 10 #llega a multiplicar hasta el 10

for F1 in range(tabla_desde, tabla_hasta +1):#toma el primer y segundo dato 
    print('---------------')
    for F2 in range(desde, hasta +1): #toma el segundo dato
        print(f'{F1} x {F2} = {F1 * F2}')#multiplica e imprime por consola
        print()
        
#for numero in range(1, 11, 2)va mostrando de a dos en dos        
        

 #cadenas "f", que simplifica la inserción de variables y expresiones en las cadenas.
# Una cadena "f" contiene variables y expresiones entre llaves ({}) que se sustituyen directamente por su valor
#Si no se escribe la letra f antes de la cadena, Python no sustituye los valores de las variables ni calcula las expresiones.