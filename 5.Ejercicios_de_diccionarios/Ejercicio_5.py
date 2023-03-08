'''Ejercicio 5.
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.'''
def run():
    asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    creditos_total = 0
    for asignatura, credito in asignaturas.items():
        creditos_total += credito
        print(f'La asignatuta {asignatura} tiene {credito} credito/s')
    print(f'La cantidad de creditos totales de las materias es {creditos_total}')
if __name__ == '__main__':
    run()