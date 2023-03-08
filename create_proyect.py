def crear_archivo(nombre_archivo, numero):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f"'''Ejercicio {numero}.'''")
    archivo.close()

def run():
    for i in range(11):
        nombre_archivo = f'Ejercicio_{i+1}.py'
        crear_archivo(nombre_archivo, i+1)
                      
if __name__ == '__main__':
    run()