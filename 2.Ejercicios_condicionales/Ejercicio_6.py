'''
Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
'''
def mujeres(nombre):
  if  nombre[0].upper() <= 'M':
    return(True)
  else:
    return(False)
def hombres(nombre):
  if  nombre[0].upper() >= 'N':
    return(True)
  else:
    return(False)

def grupo(nombre,sexo):
  if sexo.lower() == 'hombre':
    return(hombres(nombre))
  else:
    return(mujeres(nombre))
  
def run():
  nombre = input('digite su nombre: ')
  sexo = input('digite si es hombre o mujer: ')
  grupo(nombre,sexo)
  if grupo is True:
    print('usted pertenece al grupo A')
  else:
    print('usted pertenece al grupo B')


if __name__ == '__main__':
  run()