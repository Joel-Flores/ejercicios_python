'''
Ejercicio 4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''
def run():
  numero = int(input('digite un numero: '))
  if numero % 2 == 0:
    print(f'el numero {numero} es par.')
  else:
    print(f'el numero {numero} es impar.')

if __name__ == '__main__':
  run()