'''
Ejercicio 1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces
'''
def run():
  palabra = input('digite una palabra: ')
  for i in range(0,9):
    print(palabra)

if __name__ == '__main__':
  run()