#!/bin/bash

#LIMPIEZA DEL TERMINAL

SEGUIRMENU=1

##FUNCION DE SUMAR NUEMROS

function sumarNumeros(){
    if [ $# -le 3 ]
    then
        echo `expr $1 + $2`
    else
        echo No has introducido dos números
    fi
}

##FUNCION DE MULTIPLICAR NÚMEROS

function multiplicarNumeros(){
    if [ $# -le 3 ]
    then
        return `expr $1 \* $2`
    else
        echo No has introducido dos números
    fi
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
        4) Sumar  dos números 
        5) Multiplicar dos números
        6) Chuletas UD-01 SI
        7) Salir
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
        read -p "Introduzca 2 números a sumar 
            \"Separelos por un espacio\"" SECUENCIA
        sumarNumeros $SECUENCIA
        ;;
        5)
        read -p "Introduzca 2 números a sumar 
            \"Separelos por un espacio\"" SECUENCIA
        multiplicarNumeros $SECUENCIA
        echo $?
        ;;
        6)
        xdg-open "https://www.instagram.com/reel/C09H-fFuHRY/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" >/dev/null 
        ;;
        7)
        SEGUIRMENU=0
        ;;
        *)
        echo "la opcion $OPCION no es valida, intentelo de nuevo"
    esac
done
echo Hasta la próxima