'''Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos tuplas y muestre por pantalla su producto escalar.'''
def product(v1, v2):
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result

def run():
    vector_1 = (1, 2, 3)
    vector_2 = (-1, 0, 2)
    if len(vector_1) == len(vector_2):
        result = product(vector_1, vector_2)
        print(f'el producto de {vector_1} y {vector_2} es : {result}')
    else:
        print('los vectores no son iguales')
        
if __name__ == '__main__':
    run()