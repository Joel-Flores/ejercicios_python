'''
Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''
def impares(numero):
  for i in range(1,numero):
    if i % 2 != 0:
      print(i)

def run():
  numero = int(input('digite un numero positivo: '))
  if numero > 0:
    impares(numero)
  else:
    print(f'error, lo que digito no es un numero.)

if __name__ == '__main__':
  run()