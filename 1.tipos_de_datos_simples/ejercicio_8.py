'''
Ejercicio 8

Escribir un programa que lea un entero positivo, n, introducido por el usuario y después
muestre en pantalla la suma de todos los enteros desde 1 hasta n. 
La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
'''
def suma_de_numero(numero):
    suma_total = 0
    for i in range(numero):
        suma_total += i+1
    return(suma_total)


def run():
    numero = int(input('digite un numero: '))
    if numero > 0:
        resultado = int(suma_de_numero(numero))
        suma = (resultado * (resultado + 1))/2
        print(f'el resultado de la operacion es: {suma}')
    else:
        print(f'el numero {numero} que digito no es positivo')


if __name__ == "__main__":
    run()