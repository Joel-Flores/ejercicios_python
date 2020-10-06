'''
Ejercicio 6
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido
'''
def run():
  numero = int(input('Digite un numero: '))
  for i in range(0,numero):
    print('*' * (i+1))
    print()

if __name__ == '__main__':
  run()