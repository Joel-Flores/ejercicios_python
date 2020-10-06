'''
Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''
def carnivora():
  print('I N G R E D I E N T E S\n C A R N I V O R O S')
  print('1. Peperoni \n 2. Salmón. \n 3. Jamón. \n')
  eleccion = int(input('seleccione que llevara su pizza: '))
  if eleccion == 1:
    return('Peperoni')
  elif eleccion == 2:
    return('Salmón')
  elif eleccion == 3:
    return('Jamón')
  else:
    return(break)
  
def vegetariana():
  print('I N G R E D I E N T E S\n V E T A R I A N O S')
  print('1. Pimiento \n 2. Tofu. \n')
  eleccion = int(input('seleccione que llevara su pizza: '))
  if eleccion == 1:
    return('Pimiento')
  elif eleccion == 2:
    return('Tofu')
    else:
      return(break)

def run():
  usuario = input('quiere una pizza vegetariana s/n: ')
  if usuario == 'n':
    ingrediente = carnivora()
    print(f'la pizza no es vegetariana. y los ingredientes son: mozzarella, tomate y {ingrediente}')
  elif usuario == 's':
    ingrediente = vegetariana()
    print(f'la pizza es vegetariana. y los ingredientes son: mozzarella, tomate y {ingrediente}')
  else:
    print('Error no digito correctamente.')
  

if __name__ == '__main__':
  run()