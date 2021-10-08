#Resolucion GUIA Nº1
#01/08/2021
#Cada payaso pesa 112 g y cada muñeca 75 g. 
#Crear un programa que lea el número de payasos y muñecas
#Calcule el peso total del paquete que será enviado

peso_payaso = 112 #gr
peso_muñeca = 75 #gr

payasos = int(input('Cantidad de payasos a enviar:  '))
muñecas = int(input('Cantidad de muñecas a enviar:  '))

peso_total = peso_payaso * payasos + peso_muñeca * muñecas
#peso_total /= 1000 para convertirlo a kilos

print('El peso total del paquete es  '  + str(peso_total) + 'gramos')

#if peso_payaso >= 1000:
#payaso /= 1000

#print(f'El peso total del paquete a enviar es {peso_total}')
