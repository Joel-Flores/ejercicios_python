'''
Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''
def run():
  numero = int(input('digite un numero positivo: '))
  for i in range(numero,0):
    print(f'{i}, ')

if __name__ == '__main__':
  run()