'''
Ejercicio 13

Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final
de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
introducida por el usuario. Después el programa debe calcular y mostrar por pantalla 
la cantidad de ahorros tras el primer, segundo y tercer años. 
Redondear cada cantidad a dos decimales.
'''
def calcular_interes(ahorros):
    return(((4 * ahorros)/100)+ahorros)

def run():
    deposito = float(input('digite la cantidad depositada a la cuenta de ahorros: '))
    año_uno = calcular_interes(deposito)
    año_dos = calcular_interes(año_uno)
    años_tres = calcular_interes(año_dos)
    print(f'tus ahorros mas el interes el primer año es {round(año_uno,2)}')
    print(f'tus ahorros mas el interes el segundo año es {round(año_dos,2)}')
    print(f'tus ahorros mas el interes el tercer año es {round(años_tres,2)}')

if __name__ == "__main__":
    run()