'''
Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
'''
def trabajo():
  pregunta = input('usted trabaja, si o no?: ')
  if pregunta == si:
    ingresos = float(input('digite la cantidad de ingresos que persive: '))
    return(ingresos)
  else:
    return(0)


def run():
  edad = int(input('digite su edad: '))
  if edad >= 18:
    ingresos = trabajo()
    if ingresos >= 1000:
      print('usted tributa impuestos.')
    else:
            print('usted tributa impuestos.')
  else:
    print('usted es menor de edad.')


if __name__ == '__main__':
  run()