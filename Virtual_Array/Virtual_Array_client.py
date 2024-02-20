from Virtual_Array import Virtual_Array

def mostrar_opciones():
    return """Opciones: 
              ASIGNAR POS VAL
              CONSULTAR POS
              LIMPIAR
              SALIR"""
def main():
    n = int(input('Ingrese cantidad de elementos: '))

    if n <= 0:
        print('Cantidad de elementos inesperada.')
        return
    
    virtual_arr = Virtual_Array(n)


    while (True):
        print(mostrar_opciones())

        input_usuario = input('Ingrese accion: ')

        if input_usuario == '':
            print('Ingrese una accion valida')
            continue

        input_usuario = input_usuario.split(' ')

        accion = input_usuario[0]

        if accion == 'ASIGNAR':
            pos, val = int(input_usuario[1]), int(input_usuario[2])

            if not virtual_arr.asignar(pos, val):
                print(f'Error al asignar el valor {val} a la posicion {pos}')

        if accion == 'CONSULTAR':
            pos = int(input_usuario[1])

            res, val = virtual_arr.consultar(pos)

            if not res:
                print(f'Error consultando la posicion {pos}')

            elif val is None:
                print(f'La posicion {pos} no se encuntra inicializada')

            else:
                print(f'T[{pos}] = {val}') 

        if accion == 'LIMPIAR':
            virtual_arr.limpiar()

        if accion == 'SALIR':
            break


if __name__ == '__main__':
    print('Abriendo cliente...')
    try:
        main()

    except:
        print('Error inesperado')

    print('Cerrando cliente...')