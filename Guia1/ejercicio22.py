#Resolucion GUIA Nº1
#01/08/2021

print('TENEMOS: Banana, Manzana, Pera, Naranja ')
frutas = {'Banana':80, 'Manzana':100, 'Pera':120, 'Naranja':150}
fruta = input('¿Qué fruta quieres? ').capitalize()
 
if fruta in frutas:
    kg = float(input('¿Cuántos kilos vas a llevar?  '))#que pasa si es medio?
    print(kg, 'kilos de ', fruta, ' cuestan  ', '$', frutas[fruta]*kg)
else: 
    print('Lo siento,', fruta, ' no tenemos')