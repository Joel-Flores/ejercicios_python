'''
Ejercicio 1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''
def run():
  edad = int(input('cual es tu edad: '))
  if edad > 18:
    print('tu eres mayor de edad')
  else:
    print('tu eres menor de edad')

if __name__ == '__main__':
  run()