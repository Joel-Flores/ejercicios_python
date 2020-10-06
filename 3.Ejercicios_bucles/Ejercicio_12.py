'''
Ejercicio 12
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
'''
def run():
  frase = str(input('degite una frace: '))
  rango = len(frase)
  letra = input('digite una letra: ')
  contador = 0
  for i in range(0,rango):
    if frase[i] == letra:
      contador += 1
  print(f'la letra "{letra}", se repite {contador} veces.\n en la frace: "{frase}".')

if __name__ == '__main__':
  run()