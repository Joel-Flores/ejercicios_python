'''
Ejercicio 5

Escribir un programa que pregunte el nombre del usuario en la consola 
y después de que el usuario lo introduzca muestre por pantalla <NOMBRE>
tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas 
y <n> es el número de letras que tienen el nombre.
'''

def run():
    nombre = input("cual es tu nombre: ")
    print(nombre.upper())
    print(f"el nombre {nombre},tiene {len(nombre)} letras")


if __name__ == "__main__":
    run()