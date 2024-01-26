#!/bin/bash

#LIMPIEZA DEL TERMINAL

SEGUIRMENU=1

##FUNCION DE SUMAR NUEMROS

function sumarNumeros(){
    for((i=2))
}


##MENU
echo `clear`
while (( $SEGUIRMENU ))
do
    read -p "      Benvido
    Seleccione á opcion:
        1) Busqueda de archivos
        2) Mostrar contenido de un archivo
        3) Mover archivo
        4) Sumar numeros 
        5) Multiplicar numeros
        6) Salir
        " OPCION
    
    case $OPCION in
        1)
        read -p "Introduzca el nombre del archivo ('filename'):" FILENAME
        read -p "Introduzca la ruta donde buscarlo ('path')" PATH
        source busqueda.sh
        busqueda $FILENAME $PATH
        ;;
        2)
        read -p "Introduzca la ruta del archivo " ARCHIVO
        source mostrarArchivo.sh
        mostrado $ARCHIVO
        ;;
        3)
        read -p "Indique la ruta del archivo a mover " FILENAME
        read -p "Indique la ruta del destino " DESTINY
        echo `mv $FILENAME $DESTINY`
        ;;
        4)

        ;;
        6)
        SEGUIRMENU=0
        ;;
        *)
        echo "la opcion $OPCION no es valida, intentelo de nuevo"
    esac
done
echo "Hasta la próxima"