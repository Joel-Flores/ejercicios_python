''' Escribir un programa que almacene las matrices

A=((1, 4, 2), (5, 3, 6)), B = ((-1, 0), (1, 0), (1, 1))

en una tupla y muestre por pantalla su producto.
Nota: Para representar matrices mediante tuplas usar tuplas anidadas, representando cada vector fila en una tupla. '''

def for_in_for(contador_a, matriz_a, matriz_b):
    # Esta función toma tres argumentos: el índice de una fila específica de la matriz_a, la matriz_a y la matriz_b
    result = list()  # Creamos una lista vacía para almacenar los resultados
    for i in range(len(matriz_b[0])):  # Iteramos sobre el número de columnas de la matriz_b
        producto = 0  # Inicializamos el producto en cero
        for j in range(len(matriz_b)):  # Iteramos sobre el número de filas de la matriz_b
            producto += matriz_a[contador_a][j] * matriz_b[j][i]  # Calculamos el producto entre la fila específica de matriz_a y la columna i de matriz_b
        result.append(producto)  # Agregamos el resultado a la lista de resultados
    return result  # Devolvemos la lista de resultados

def product(matriz_a, matriz_b):
    # Esta función toma dos argumentos: la matriz_a y la matriz_b
    result = list()  # Creamos una lista vacía para almacenar los resultados
    for i in range(len(matriz_a)):  # Iteramos sobre el número de filas de la matriz_a
        result.append(for_in_for(i, matriz_a, matriz_b))  # Calculamos el producto de la fila i de la matriz_a con la matriz_b, utilizando la función for_in_for, y agregamos el resultado a la lista de resultados
    return result  # Devolvemos la lista de resultados

def tam_matriz(matriz):
    # Esta función toma una matriz como argumento
    result = None  # Inicializamos el resultado en None
    tam = len(matriz)  # Obtenemos el número de filas de la matriz
    for i in range(tam-1):  # Iteramos sobre el número de filas de la matriz, excepto la última
        if len(matriz[i]) == len(matriz[i+1]):  # Verificamos si la cantidad de columnas de la fila i es igual a la cantidad de columnas de la fila i+1
            result = True  # Si es así, asignamos True al resultado
        else:
            result = False  # Si no es así, asignamos False al resultado
    return result  # Devolvemos el resultado

def run():
    matriz_a = ((1, 2, 3), (4, 5, 6))  # Creamos una matriz_a de 2x3
    matriz_b = ((-1, 0), (0, 1), (1, 1))  # Creamos una matriz_b de 3x2
    result_a = tam_matriz(matriz_a)  # Verificamos si la matriz_a tiene un tamaño válido
    result_b = tam_matriz(matriz_b)  # Verificamos si la matriz_b tiene un tamaño válido

    if result_a is True and result_b is True:  # Si ambas matrices tienen un tamaño válido
        result = product(matriz_a, matriz_b)  # Calculamos el producto de las matrices utilizando la función product
        for porduct in result:  # Iteramos sobre la lista de resultados
            print(tuple(porduct))  # Imprimimos cada resultado como una tupla
    else:
        print('las matrices non tienen los mismos tamaños')  # Si

if __name__ == '__main__':
    run()