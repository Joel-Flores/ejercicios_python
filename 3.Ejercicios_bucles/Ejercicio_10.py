'''
Ejercicio 10
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
'''
def primo(numero):
  contador = 0
  for i in range(0,numero):
    if numero % (i + 1) == 0:
      contador = contador + 1
  if contador <= 2:
    return(True)
  else:
    return(False)

def run(numero):

  for i in range(numero+1):
    if i % 2 != 0:
      confirmar = primo(i)
      if confirmar is True:
        print(i)

if __name__ == '__main__':
  numero = int(input('Digite un numero: '))
  run(numero)
