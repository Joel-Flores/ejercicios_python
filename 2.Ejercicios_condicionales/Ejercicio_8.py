'''
Ejercicio 8
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
'''
def salario(puntuacion):
  aumento = 0
  if puntuacion == 1:
    print('el puntaje de la evaluación es Inaceptable.')
  elif puntuacion == 2:
    print('el puntaje de la evaluación es Aceptable.')
    aumento = 2400 * 0.4
  elif puntuacion == 3:
    print('el puntaje de la evaluación es Meritorio.')
    aumento = 2400 * 0.6
  else:
    print('el numero que que digito es incorrecto.')
  return(2400 + aumento)

def run():
  print('nivel de puntuacion \n')
  print(' 1. 0.0\n 2. 0.4\n 3. 0.6\n')
  puntuacion = int(input('cula es el puntaje obtenido del empleado: '))
  print('su salario actual es de 2400$')
  dinero = salario(puntuacion)
  print(f'conforme a la evaluacion, su salario es de {dinero}$')

if __name__ == '__main__':
  run()