# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular(que es una
# persona) y cantidad(puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Construir los siguientes métodos para la clase:
# ● Un constructor, donde los datos pueden estar vacíos.
# ● El atributo no se puede modificar directamente, sólo ingresando o retirando
# dinero.
# ● mostrar(): Muestra los datos de la cuenta.
# ● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida
# es negativa, no se hará nada.
# ● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en
# números rojos.
class Persona():

    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def validar_dni(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(self.__dni) != 9:
            print("DNI incorrecto")
            self.__dni = ""
        else:
            letra = self.__dni[8]
            num = int(self.__dni[:8])
            if letra.upper() != letras[num % 23]:
                print("DNI incorrecto")
                self.__dni = ""

    @dni.setter
    def dni(self, dni):
        self.__dni = dni
        self.validar_dni()

    @edad.setter
    def edad(self, edad):
        if edad < 0:
            print("Edad incorrecta")
            self.__edad = 0
        else:
            self.__edad = edad

    def mostrar(self):
        return "Nombre:"+self.nombre+" - Edad:"+str(self.edad)+" - DNI:"+self.dni

    def esMayorDeEdad(self):
        return self.edad >= 18
