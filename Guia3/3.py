# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuantaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del
# titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por
# ciento. Construir los siguientes métodos para la clase:
# ● Un constructor.
# ● En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de
# edad., por lo tanto hay que crear un método esTitularValido() que devuelve
# verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso
# contrario.
# ● Además la retirada de dinero sólo se podrá hacer si el titular es válido.
# ● El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la
# bonificación de la cuenta.
# ● Pensar los métodos heredados de la clase madre que hay que reescribir
class CuentaJoven:
    public Cuenta


{
    int bonificacion
    bool esTitularValido()
    public:
        CuentaJoven(Persona nt, float nc, int nb)
        float get_bonificacion()
        void set_bonificacion(int nb)
        string mostrar()
        void retirar(float ncantidad)
}

CuentaJoven: : CuentaJoven(Persona nt, float nc, int nb): Cuenta(nt, nc)
{
    bonificacion = nb
}

string CuentaJoven: : mostrar()
{
    return "CUENTA JOVEN\n Titular: "+titular.mostrar() + " - Cantidad: " + to_string(cantidad) + " - Bonificaciï¿½n: " + to_string(bonificacion)
}

bool CuentaJoven: : esTitularValido()
{
    return (titular.get_edad() < 25 & & titular.esMayorDeEdad())
}

void CuentaJoven: : retirar(float ncantidad)
{
    if(!esTitularValido())
    cout << "No puedes retirar dineo. Titular no válido" << endl
    else
    cantidad = cantidad - ncantidad
}

int main(int argc, char * argv[]) {
    Persona yo("Jose Domingo", 40, "12345678Z")
    CuentaJoven micuenta(yo, 100, 10)
    cout << micuenta.get_cantidad() << endl
    cout << micuenta.mostrar() << endl
    micuenta.ingresar(50)
    micuenta.retirar(10)

    Persona otro
    otro = micuenta.get_titular()
    otro.set_edad(19)
    micuenta.set_titular(otro)

    micuenta.retirar(10)
    cout << micuenta.mostrar() << endl
    return 0
}
