import os

def crear_carpeta():
    if not os.path.exists('discos/'):
        os.makedirs('discos/') #si no existe crear carpeta

def existeArchivo(nombre):
    if (os.path.isfile(f'discos/{nombre}.txt')):
        return True
    else:
        False

def agregar():
    print('Agregando Disco')
    nombre = input('Cual es el nombre del disco: ').upper()
    archivo = existeArchivo(nombre)
    if not archivo:
        with open(f'discos/{nombre}.txt', 'w') as archivo:
            while True:
                try:
                    año = int(input('Cual es el año: '))
                    break
                except ValueError:
                    print('Escribe correctamente el año: ' )
            
            nombre_a = input('Cual es el nombre del artista: ')
        
            archivo.write(f'Nombre del disco: {nombre}\n')
            archivo.write(f'Año: {año}\n')
            archivo.write(f'Artista: {nombre_a}\n')
            #cuantas canciones tiene?
            while True:
                try:
                    n_canciones = int(input('Cuantas canciones: '))
                    break
                except ValueError:
                    print('Escribe un numero de canciones: ' )

                  
                    
            for i in range(n_canciones):
                nombre_c = input(f'nombre de la cancion {i+1} ')
                archivo.write(f'{i+1}.- {nombre_c}\n')

            print('Disco creado')
    else:
        print('Ese disco ya existe')

def editar():
    carpeta = os.listdir('discos/')
    lista_archivos = [a for a in carpeta if a.endswith('txt')]
    if len(lista_archivos) != 0:
        nombre_disco = input('Que disco quieres editar: ').upper()
        disco = existeArchivo(nombre_disco)
        if disco:
            with open(f'discos/{nombre_disco}.txt', 'w') as archivo:
                nombre_nuevo = input('Cual es el nuevo nombre del Disco: ').upper()
                while True:
                    try:
                        año = int(input('Cual es el año: '))
                        break
                    except ValueError:
                        print('Escribe correctamente el año: ' )
                nombre_a = input('Cual es el nombre del artista: ')

                archivo.write(f'Nombre del disco: {nombre_nuevo}\n')
                archivo.write(f'Año: {año}\n')
                archivo.write(f'Artista: {nombre_a}\n')
                #cuantas canciones tiene?
                while True:
                    try:
                        n_canciones = int(input('Cuantas canciones: '))
                        break
                    except ValueError:
                        print('Escribe un numero de canciones: ' )

                for i in range(n_canciones):
                    nombre_c = input(f'nombre de la cancion {i+1} ')
                    archivo.write(f'{i+1}.- {nombre_c}\n')
                viejo = f'discos/{nombre_disco}.txt'
                nuevo = f'discos/{nombre_nuevo}.txt'
            os.rename(viejo,nuevo)
        else:
            print('Ese disco no existe')
    else:
        print('No hay discos')


def mostrar():
    carpeta = os.listdir('discos/')
    lista_archivos = [a for a in carpeta if a.endswith('txt')]
    if len(lista_archivos) != 0:
        print('*'*30)
        print('LISTA DE DISCOS')
        print('*'*30)

        carpeta = os.listdir('discos/')
        lista_archivos = [a for a in carpeta if a.endswith('txt')]
        # for a in carpeta:
        #     if a.endswith('txt'):
        #         lista_archivos.append(a)
        for archivo in lista_archivos:
            with open(f'discos/{archivo}') as disco:
                for linea in disco:
                    print(linea.rstrip())
                print('*'*30)
    else:
        print('No hay discos')

def buscar():

    carpeta = os.listdir('discos/')
    lista_archivos = [a for a in carpeta if a.endswith('txt')]
    if len(lista_archivos) != 0:
        print('*'*30)
        print('BUSCAR DISCOS')
        print('*'*30)
        nombre_disco = input('Que disco quieres buscar: ').upper()
        disco = existeArchivo(nombre_disco)

        if disco:
            print('*'*30)
            with open(f'discos/{nombre_disco}.txt') as archivo:
                for linea in archivo:
                    print(linea.rstrip())

                print('*'*30)
        else:
            print('Ese disco no existe')
    else:
        print('No hay discos')


def eliminar():
    carpeta = os.listdir('discos/')
    lista_archivos = [a for a in carpeta if a.endswith('txt')]
    if len(lista_archivos) != 0:
        print('*'*30)
        print('ELIMINAR DISCO')
        print('*'*30)
        nombre_disco = input('Que disco quieres ELIMINAR: ').upper()
        disco = existeArchivo(nombre_disco)

        if disco:
            os.remove(f'discos/{nombre_disco}.txt')
            print(f'Se elimino el disco: {nombre_disco}')
        else:
            print('Ese disco no existe')
    else:
        print('No hay discos')

def main():
    crear_carpeta()
    while True:
        os.system('cls')
        print('*'*30)
        print('             menu                   ')
        print('*'*30)
        print('1) Agregar disco')
        print('2) Editar disco')
        print('3) Ver discos')
        print('4) Buscar disco')
        print('5) Eliminar disco')
        print('6) Salir')
        opc = int(input('Ingresa una opcion -> '))
        os.system('cls')

        if opc == 1:
            agregar()
        elif opc == 2:
            editar()
        elif opc == 3:
            mostrar()
        elif opc == 4:
            buscar()
        elif opc == 5:
            eliminar()
        elif opc == 6:
            print('Adiosin...')
            break
        else:
            print('Ingresa una opcion valida')

        input("\nPresiona ENTER para continuar...")

main()
