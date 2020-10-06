'''
Ejercicio 14
Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, 
el descuento que se le hace por no ser fresca y el coste final total.
el descuento que se le hace por no ser fresca y el coste final total.
el descuento que se le hace por no ser fresca y el coste final total.
'''
def run():
  barra_pan = 3.49
  pan_descuento = (60 * barra_pan) / 100
  pan_vendido = int(input('cuantas barras de pan que no son del dia se vendio: '))
  total_pagar = (barra_pan - pan_descuento) * pan_vendido
  print(f'la barra de pan del dia esta a {barra_pan}$ \n el pan pasado tiene un descuento de {pan_descuento}$ \n el total a pagar es {round(total_pagar,2)}$')


if __name__ == '__main__':
  run()