'''
Ejercicio 10

Escribir un programa que pida al usuario dos números enteros y muestre por pantalla 
la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos
por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
'''
def run():
    dividendo = int(input('digite el dividendo: '))
    divisor = int(input('digite el divisor: '))
    cociente = dividendo / divisor
    resto = dividendo % divisor
    print(f"entre {dividendo} / {divisor} da un cociente de {cociente} y un resto de {resto}")

if __name__ == "__main__":
    run()