'''
Ejercicio 2

Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
'''
def run():
  curso = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lenguaje']
  for i in range(len(curso)):
    print(f'yo estudio {curso[i]}.')

if __name__ == '__main__':
  run()
