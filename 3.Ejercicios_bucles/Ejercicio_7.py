'''
Ejercicio 7
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''
def tabla(numero):
  print(f'tabla de multiplicar de el numero {numero})
  for i in range(1,10):
    print(i * numero '\n')

def run():
  for i in range(1,10):
    tabla(i)
    print()

if __name__ == '__ main__':
  run()