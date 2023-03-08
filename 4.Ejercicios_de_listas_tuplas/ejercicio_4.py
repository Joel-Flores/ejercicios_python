'''
Ejercicio 4

Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
'''
def run():
    numeros = []
    while True:
        numero_ganador = input('Digite los numeros ganadores de la loteria: ')
        if numero_ganador == 'salir':
            break
        else:
            numeros.append(int(numero_ganador))
    numeros.sort()
    print(f'los numeros ganadores son: {numeros}')

if __name__ == "__main__":
    run()