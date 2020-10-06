'''
Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''
def run():
  contraseña_guardada = 'nunca pares de aprender'
  contraseña = input('cual es su contraseña: ')
  if contraseña == contraseña_guardada:
    print('la contradeña es correcta.')
  else:
    print('la contraseña es incorrecta')

if __name__ == '__main__':
  run()
