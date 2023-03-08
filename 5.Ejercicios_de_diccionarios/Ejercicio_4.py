'''Ejercicio 4.
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.'''
def run():
    meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
    try:
        fecha_input = input('Introduce una fecha en formato dd/mm/aaaa: ')
        fecha = fecha_input.split('/')
        
        for value in range(len(fecha)):
            fecha[value] = int(fecha[value])
        
        error = None
        if fecha[0] < 1 or fecha[0] > 31:
            print(f'el dia {fecha[0]} no existe')
            error = True
        if not fecha[1] in meses:
            print(f'el mes {fecha[1]} no existe')
            error = True
        if not error is True:
            print(f'{fecha[0]} de {meses[fecha[1]]} del año {fecha[2]}')
    except:
        print('Lo siento hubo un error con los datos que me indicas')
if __name__ == '__main__':
    run()