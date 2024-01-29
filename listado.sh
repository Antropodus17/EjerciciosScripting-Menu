#!/bin/bash

#PROGRAMA DE LISTADO

function listar(){
   if [ $# -ge 2 ]
   then
      echo `ls -a`
   else 
      echo `ls`
   fi
}