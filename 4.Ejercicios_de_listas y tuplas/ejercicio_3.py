'''
Ejercicio 3

Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura, 
y después las muestre por pantalla con el mensaje 
En <asignatura> has sacado <nota> donde <asignatura> 
es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas
 introducidas por el usuario.
'''
def run():
    curso = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lenguaje']
    for asignatura in range(len(curso)):
        notas = float(input(f'digite la nota que tiene en {curso[asignatura]}: '))
        print(f'En {curso[asignatura]} has sacado {notas}.')

if __name__ == "__main__":
    run()