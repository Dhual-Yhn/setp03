# Set de problemas #3
# Problema 2.
# Lenguaje y Tecnicas de Programacion
# Profesor: Igor Caracci
# Profesor(Ayudante): Andres Caro
# Universidad de Santiago de Chile
# 10 de mayo del 2013
#
# Descripcion:
#
# Cree una función recursiva cuenta_palabras(dict) que tome como entrada
# el diccionario re-sultante del ejecicio Funes del Set de Problemas #2 y
# muestre cuántas palabras hay en el texto

import re   # Libreria para expresiones regulares
import sys  # Libreria que permite aumentar la profundidad de la recursion 

# Sin el sys.set nos dara un error por "profundidad maxima de recursion supero en comparacion, por lo que es necesario si o si
# En realidad lo que pasa es que por proteccion, el sistema le pone limites a la recursion, ya que si no se podria acabar la
# memoria disponible
sys.setrecursionlimit(10000)

# Funcion recursiva que cuenta cuantas palabras hay en el texto
def cuenta_palabras(dict):
   if ( len(dict) > 0 ):
      palabra, cantidad = dict.popitem()
      return( cuenta_palabras(dict) + int(cantidad) )
   else:
      return( 0 )
# el popitem elimina el elemento del diccionario en cada vuelta, elimino elemento y lo sumo. al no quedarme ningun elemento
# retorno 0 y no invoco mas la funcion
#  en cada iteración obtenemos un elemento y su valor (dict.popitem))

dic_cuento={} # Declaro diccionario

# Abro archivo 
# (encoding='utf-8)sirve para considerar los acentos de las palabras
archivo = open('funes.txt','r',encoding='utf-8')
 
conten = archivo.read().lower()               # Paso todo a minusculas
archivo.close()                               # Cierro archivo
palabras = re.split('[^a-záéíóúñü]*',conten)  # Busco palabras

for pal in palabras:                          # Recorro lista palabras
    if (pal in dic_cuento):                   # Chequeo si las conte
        dic_cuento[pal]=dic_cuento[pal]+1     # Si ya figura, incremento
    else:
        dic_cuento[pal]=1                     # Si no figura, la agrego

# Ordena diccionario de mayor a menor y lo recorro
print("Total de palabras de este archivo es", cuenta_palabras(dic_cuento))
