'''Ejercicio 1.
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''
def run():
    monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    divisa = input('Introduce una divisa: ').capitalize()
    if divisa in monedas:
        print(f'El símbolo de {divisa} es {monedas[divisa]}')
    else:
        print(f'La divisa {divisa} no está en el diccionario.')
    

if __name__ == '__main__':
    run()