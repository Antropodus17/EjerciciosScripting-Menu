#!/usr/bin/python3
import os


permisosValidos=("0","1","2","3","4","5","6","7")

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
        4) Eliminar un elemento 
        5) Crear un directorio
        6) Salir
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
            if (os.access(fichero, os.R_OK)):
                fichero=open(fichero)
                if (fichero.readable):
                    print(fichero.read())
                else:
                    print("No se puede leer el archivo")
                
            else:
                print("No tienes aceso a este archivo")
                
        case 3:
            while(mostrar_ocultos not in ("N","n","Y","y")):
                mostrar_ocultos=input("Desea cambiarle el nombre al archivo? Y/N  ")
            if(mostrar_ocultos in ("N","n")):
                ruta_fichero=input("Introduzca el nombre del fichero a mover: ")
                ruta_destino=input(f"Ruta de destino sin espacios ni barras finales del fichero {ruta_fichero}: ")
                ruta_destino+="/"+ruta_fichero
                os.rename(ruta_fichero,ruta_destino)
            else:
                ruta_fichero=input("Introduzca el nombre del fichero a mover: ")
                ruta_destino=input(f"Ruta de destino sin espacios ni barras finales del fichero {ruta_fichero}: ")
                os.rename(ruta_fichero,ruta_destino)
                
        case 4:
            elemento_a_eliminar=input("Introduzca la ruta del fichero a eliminar: ")
            try:
                os.remove(elemento_a_eliminar)
            except:
                try:
                    os.rmdir(elemento_a_eliminar)
                except:
                    print("No existe el elemento a eliminar")
        case 5:
            print('''           ***IMPORTANTE***
    No se crearan las carpetas padres.
    Hay que ir una por una.
    ''')
            ruta_directorio=input("Introduzca la ruta del directorio sin barras laterales finales: ")
            nombre_directorio=input("Introduzca el nombre del directorio: ")
            if (ruta_directorio.rstrip(" ")==""):
                directorio_final=nombre_directorio.lstrip(" ")
            else:
                directorio_final=ruta_directorio.rstrip(" ")+"/"+nombre_directorio.lstrip(" ")
            try:
                print(f"Creando: {directorio_final}")
                os.mkdir(directorio_final)
                print("El directorio se ha creado con exito.")
            except FileExistsError:
                print("El directorio ya existe")
            
            except:
                print("No se ha podido crear el directorio")
        case 6:
            mostrar_menu=0
            
