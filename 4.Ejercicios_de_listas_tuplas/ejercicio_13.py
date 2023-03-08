'''Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.'''
from math import sqrt

def suma_cuadrado(numeros, media):
    producto = list()
    for numero in numeros:
        producto.append((numero - media) ** 2)
    producto = sum(producto)
    return producto

def run():
    # Pedir al usuario que ingrese una muestra de números separados por comas
    list_num = input("Introduce una muestra de números separados por comas: ")
    numeros = list()
    error = None
    char = list()
    
    # Convertir la entrada en una lista de números
    for numero in list_num.split(","):
        try:
            numeros.append(float(numero))
        except:
            char.append(numero)
            error = True
            
    if error is None:
        # Calcular la media
        media = sum(numeros) / len(numeros)
        # Calcular la suma de cuadrados
        cuadrado = suma_cuadrado(numeros, media)
        # Calcular la desviación típica
        desviacion_tipica = sqrt(cuadrado / (len(numeros) - 1))
        # Mostrar los resultados
        print("Media: ", media)
        print("Desviación típica: ", desviacion_tipica)
    else:
        print(f'{char} no son numeros.')


if __name__ == '__main__':
    run()