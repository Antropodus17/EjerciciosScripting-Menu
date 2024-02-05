#!/usr/bin/python3
import os


os.system("clear")
print("          Benvido")
mostrar_menu=1
while(mostrar_menu):
    opcion=-1
    while (opcion<1 or opcion>7):
        opcion=int(input('''Seleccione á opcion:
        1) Listado de archivos
        2) Mostrar contenido de un archivo
        3) Mover archivo
        4) Sumar  dos números 
        5) Multiplicar dos números
        6) Chuletas UD-01 SI
        7) Salir
        '''))

    match opcion:
        case 1:
            mostrar_ocultos=-1
            while(mostrar_ocultos not in ("N","n","Y","y")):
                mostrar_ocultos=input("Quiere visualizar los archivos ocultos? Y/N  ")
            if(mostrar_ocultos in ("N","n")):
                lista = os.listdir(os.getcwd())
                for i in lista:
                    if (i[0]!="."):
                        print(i)
            else:
                lista = os.listdir(os.getcwd())
                for i in lista:
                    print(i)
        case 2:
            fichero=input("Introduzca la ruta del fichero a leer: ")
            #if (os.is)
            fichero=open(fichero)
            if (fichero.readable):
                print(open("menu.sh").read())
            else:
                print("No se puede leer el archivo")
        case 3:
            ruta_fichero=input("Introduzca el nombre del fichero a mover: ")
            ruta_destino=input(f"Ruta de destino del fichero {ruta_fichero}: ")
            os.system
        case 7:
            mostrar_menu=0
            
