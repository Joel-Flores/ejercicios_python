'''
Ejercicio 7
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
'''
def tipo_impositivo(renta):
  if renta < 10000:
    return(int(5))
  elif renta >=1000 and renta <20000:
    return(int(15))
  elif renta >=20000 and renta <35000:
    return(int(20))
  elif renta >=35000 and renta <60000:
    return(int(30))
  else:
    return(45)

def run():
  renta = int(input('digite su renta anual: '))
  procentaje_correspondiente = tipo_impositivo(renta)
  print(f'el tipo de renta impositivo correspondiente a {renta}$ es del {procentaje_correspondiente}%.')

if __name__ == '--main__':
  run()