'''
Ejercicio 8

Escribir un programa que pida al usuario una palabra y muestre por pantalla 
si es un palíndromo.
'''
def run():
    palabra = input('digite una palabra: ')
    palindromo = []
    for letra in palabra:
       palindromo.append(letra)

    indice = int(len(palindromo) - 1)
    for caracter in range(len(palabra)):
        if palindromo[caracter] == palindromo[indice]:
            es_palindromo = True
        else:
            es_palindromo = False

        indice -= 1
    if es_palindromo is True:
        print(f'la palabra {palabra}, es palindromo.')
    else:
        print(f'la palabra {palabra}, no es palindromo.')

if __name__ == "__main__":
    run()