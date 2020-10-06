'''
Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''
def run():
  dividendo = int(input('introduzca un numero: '))
  divisor = int(input('introduzca un numero: '))
  if divisor > 0:
    cociente = divid / divisor
    print(f'la division entre {divisor} entre {divisor} es {cociente}.)
  else:
    print('error')

if __name__ == '__main__':
  run()