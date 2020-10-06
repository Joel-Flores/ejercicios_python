'''
Ejercicio 9

Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> 
es el índice de masa corporal calculado redondeado con dos decimales.
'''
def run(peso,altura):
    imc = float(peso / (altura ** 2))
    print(f'tu ndice de masa corporal es: {imc}')

if __name__ == "__main__":
    peso = float(input('cual es tu peso en (kg): '))
    altura = float(input('cuanto mides en (m): '))
    run(peso,altura)