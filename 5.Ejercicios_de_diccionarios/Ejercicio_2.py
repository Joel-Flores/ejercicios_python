'''Ejercicio 2.
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.'''
def run():
    try:
        datos = dict()
        datos['nombre'] = input('introduce tu nombre: ').capitalize()
        datos['edad'] = int(input('introduce tu edad: '))
        datos['dirección'] = input('introduce tu dirección: ').capitalize()
        datos['teléfono'] = int(input('introduce tu teléfono: '))
        
        print(f'{datos["nombre"]} tiene {datos["edad"]} años, vive en {datos["dirección"]} y su número de teléfono es {datos["teléfono"]}.')
    except:
        print('digitaste uno de tus datos incorrectamente.')
    
if __name__ == '__main__':
    run()