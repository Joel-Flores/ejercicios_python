'''
Ejercicio 7

Escribir un programa que almacene el abecedario en una lista, 
elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
y muestre por pantalla la lista resultante.
'''
def run():
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for indice in range(2, len(abecedario),3):
        abecedario[indice] = ''

    indice = 0
    while indice != len(abecedario):
        if abecedario[indice] == '':
            abecedario.pop(indice)

        indice += 1

    print(abecedario)

if __name__ == "__main__":
    run()