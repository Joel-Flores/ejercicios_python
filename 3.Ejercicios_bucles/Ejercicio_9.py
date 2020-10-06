'''
Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''
CONTRASEÑA = 'soy tu perra'

def error(intentos,conf_contraseña):
  while conf_contraseña != CONTRASEÑA:
    print('error la contraseña es incorrecta')
    intentos += 1 
    conf_contraseña = input('di que eres mi perra: ')
    if conf_contraseña == CONTRASEÑA:
      print(f'lo intentaste {intentos} veces.')
    
def run():
  conf_contraseña = input('di que eres mi perra: ')
  if conf_contraseña == CONTRASEÑA:
    print(' bienvenido')
  else:
    error(int(1),conf_contraseña)

if __name__ == '__main__':
  run()