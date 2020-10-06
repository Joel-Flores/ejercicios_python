'''
Ejercicio 2

Escribir un programa que almacene la cadena ¡Hola {tu nombre}! en una variable 
y luego muestre por pantalla el contenido de la variable.
'''

def run():
    nombre = input("cual es tu nombre: ")
    imprimir = "hola " + nombre +"!"
    print(imprimir)


if __name__ == "__main__":
    run()