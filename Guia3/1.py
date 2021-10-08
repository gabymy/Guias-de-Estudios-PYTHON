# Ejercicio 1
# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
# Construir los siguientes métodos para la clase:
# ● Un constructor, donde los datos pueden estar vacíos.
# ● mostrar(): Muestra los datos de la persona.
# ● esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
nombre = input('Ingresa tu nombre:  ')
anio = input('Año de nacimiento:  ')
dni = 0


def edad():
    if anio >= 18:
        print('Es mayor de edad')
    else:
        print('')


class Persona:
    def __init__(self, nombre, anio, dni):
        self.nombre = nombre
        self.anio = anio
        self.dni = dni

    def descripcion(self):
        print(f'{self.nombre} es  {self.profesion} y su {self.dni}')
#class Persona():
#def__init__(self, nombre='', edad=0, dni='')