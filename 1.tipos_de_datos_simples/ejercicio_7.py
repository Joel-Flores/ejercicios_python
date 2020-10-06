'''
Ejercicio 7

Escribir un programa que pregunte al usuario por el número de horas trabajadas
y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
'''
def run():
    horas = int(input('cuantas horas trabajas: '))
    costo = int(input('cuanto cobras por hora: '))
    print(f"la paga que te corresponde por dia es {horas * costo}")

if __name__ == "__main__":
    run()