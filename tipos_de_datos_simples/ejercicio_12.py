'''
Ejercicio 12

Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido 
y calcule el peso total del paquete que será enviado.
'''
def peso_paquete(payasos,muñecas):
    peso_payasos = payasos * 112
    peso_muñecas = muñecas * 75
    return(peso_payasos + peso_muñecas)

def run():
    payasos = int(input('cuantos payasos se vendio: '))
    muñecas = int(input('cuantas muñecas se vendio: '))
    peso = peso_paquete(payasos,muñecas)
    print(f'el peso total del paquete es {peso}g.')

if __name__ == "__main__":
    run()