'''
Ejercicio 10

Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
'''
def buscar_mayor(precios,mayor):
    for precio in precios:
        if precio > mayor:
            mayor = precio
    return (mayor)

def buscar_menor(precios,menor):
    for precio in precios:
        if precio < menor:
            menor = precio
    return(menor)

def run():
    precios = [50,75,46,22,80,65,8]
    mayor = buscar_mayor(precios,0)
    menor = buscar_menor(precios,mayor)
    print (f'El precio mayor es {mayor}')
    print (f'El precio menor es {menor}')
        
if __name__ == "__main__":
    run()