# Crear una función que pida dos años y escriba cuántos años bisiestos hay entre esas
# dos fechas incluidos los dos años.
print('Contador de años bisiestos')
anio = int(input("Escriba un año: "))
print(f"Escriba otro año posterior a", anio,  end="")
final = int(input())
while final < anio:
    print(final, 'NO es mayor que  ', anio)
    print('Prueba de nuevo', end='')
    final = int(input())


def es_bisiesto(tiempo):
    return tiempo % 400 == 0 or (tiempo % 100 != 0 and tiempo % 4 == 0)


contador = 0
for i in range(anio, final + 1):
    if es_bisiesto(i):
        contador += 1

print("De", anio, "a", final, "hay", final - anio +
      1, "años,", contador, "de ellos bisiestos.")
