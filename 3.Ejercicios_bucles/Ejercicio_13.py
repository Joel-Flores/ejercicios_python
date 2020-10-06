'''
escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba "salir" que terminara
'''
def run():
  while True:
    palabra = input('digite algo: ')
    if palabra != 'salir':
      print(palabra)
    else:
      break
if __name__ == '__main__':
  run ()
