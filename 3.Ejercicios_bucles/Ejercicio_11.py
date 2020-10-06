'''
Ejercicio 11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
'''
def run():
  palabra = input('digite una palabra: ')
  contador = len(palabra)
  while contador > 0:
    print(palabra[contador - 1])
    contador -= 1

if __name__ == '__main__':
  run()