'''
Ejercicio 6

Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura 
y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla
 las asignaturas que el usuario tiene que repetir.
'''
def run():
    curso = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lenguaje']
    reprobados = []
    notas = []
    for asignatura in range(len(curso)):
        notas.append(float(input(f'digite la nota que tiene en {curso[asignatura]}: ')))

    indice = 0
    while True:
        if notas[indice] >= 6:
            curso.pop(indice)
            notas.pop(indice)

        else:
            indice += 1

        if indice == len(notas):
            break

    print(f'usted debe repetir las asignaturas de {curso}')


if __name__ == "__main__":
    run()