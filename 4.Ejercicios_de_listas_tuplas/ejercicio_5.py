'''
Ejercicio 5

Escribir un programa que almacene en una lista los números del 1 al 10 
y los muestre por pantalla en orden inverso separados por comas.
'''
def run():
    numeros = []
    for i in range(10):
        numeros.append(i + 1)
    numeros.reverse()
    print(numeros)

if __name__ == "__main__":
    run()