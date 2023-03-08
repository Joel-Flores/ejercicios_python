'''Ejercicio 3.
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.'''

def run():
    frutas = {'Platano' : 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja' : 0.70}
    try:
        fruta = str(input('que fruta queres saber su precio: ')).capitalize()
        if not fruta in frutas:
            print(f'Lo siento no tengo el precio de la fruta {fruta}.')
        else:
            cantidad = float(input('cuantos kilos son: '))
            precio = frutas[fruta]*cantidad
            print(f'{cantidad}Kg. de {fruta} tiene un precio de: {round(precio, 2)}')
    except:
        print('Lo siento los datos que me pides son incorrectos.')

if __name__ == '__main__':
    run()