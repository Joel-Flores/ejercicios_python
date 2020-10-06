'''
Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
'''
def run():
  inversion = int(input('digite la cantidad a invertir: '))
  interes = int(input('digite el interes anual de la inversión: '))
  años = int(input('digite la cantidad de años que invertira: '))
  interes_anual = 0
  for i in range(0,años - 1):
    interes_anual = (interes * inversion) / 100
    print(f'el capital obtenido de la inversion es {interes_anual})
    inversion += interes_anual

if __name__ == '__main__':
  run()