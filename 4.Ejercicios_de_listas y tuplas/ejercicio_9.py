'''
Ejercicio 9

Escribir un programa que pida al usuario una palabra y muestre por pantalla 
el número de veces que contiene cada vocal.
'''
def listado_de_palabras(palabra):
    letras = []
    for letra in palabra:
        letras.append(letra)
    return (letras)
def run():
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0
    palabra = input('digite una palabra: ')
    palabra = palabra.lower()
    letras = listado_de_palabras(palabra)
    for i in letras:
        if i == 'a':
            contador_a += 1
        elif i == 'e':
            contador_e += 1
        elif i == 'i':
            contador_i += 1
        elif i == 'o':
            contador_o += 1
        elif i == 'u':
            contador_u += 1
    print(f'la letra a se repite {contador_a}')
    print(f'la letra e se repite {contador_e}')
    print(f'la letra i se repite {contador_i}')
    print(f'la letra o se repite {contador_o}')
    print(f'la letra u se repite {contador_u}')

if __name__ == "__main__":
    run()