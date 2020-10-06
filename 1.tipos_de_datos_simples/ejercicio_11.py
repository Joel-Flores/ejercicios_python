'''
Ejercicio 11

Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
'''
def run():
    inversion = float(input('digite la contidad de inversion: '))
    interes = float(input('digite el interes de la inverson: '))
    años = int(input('digite la cantidad de años que sera invertido :'))
    interes_total = ((interes * inversion) / 100) * años
    retorno_inversion = inversion + interes_total
    print(f'su inversion de {inversion} a un interes anual de {interes}% por {años} años. \n le da un retorno total de {retorno_inversion}')

if __name__ == "__main__":
    run()