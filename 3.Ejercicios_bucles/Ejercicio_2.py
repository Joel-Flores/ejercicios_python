'''
Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''
def run():
  edad = int(input('digite su edad: '))
  print('usted a cumplido todas estas edades')
  for i in range(0,edad - 1):
    print(i + 1)

if __name__ == '__main__':
  run()