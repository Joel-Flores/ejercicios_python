'''
Ejercicio 4

Escribir un programa que pregunte el nombre del usuario en la consola 
y un número entero e imprima por pantalla en líneas distintas 
el nombre del usuario tantas veces como el número introducido.
'''
def run():
    nombre = input("cual es tu nombre: ")
    numero = int(input("introduce un numero: "))
    print((nombre + "\n") * numero)


if __name__ == "__main__":
    run()