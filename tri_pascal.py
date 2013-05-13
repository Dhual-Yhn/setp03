# Set de problemas #3
# Problema 1.
# Lenguaje y Tecnicas de Programacion
# Profesor: Igor Caracci
# Profesor(Ayudante): Andres Caro
# Universidad de Santiago de Chile
# 10 de mayo del 2013
#
# Descripcion:
#
# Construya una función recursiva tri_pascal(n) que tome como argumento
# el grado del binomio asociado a los coeficientes binomiales y construya
# el triángulo de Pascal mostrando hasta los coeficientes del polinomio de
# grado n resultante.

# Funcion del triangulo pascal recursivo
def tri_pascal(n): 

    # En el caso de la parte base del triangulo 
    if n == 0: 
        return [] 
    if n == 1:
        return[[1]] 

    # Parte del triangulo en forma recursiva 
    ultimo_triangulo = tri_pascal(n-1) 
    current_triangulo = [1] 
    for i in range(1, n-1): 
        current_triangulo.append(ultimo_triangulo[n-2][i-1] + ultimo_triangulo[n-2][i]) 
    current_triangulo.append(1)
    ultimo_triangulo.append(current_triangulo)
    return ultimo_triangulo

def ultimo_triangulo(n):
    triangulo = tri_pascal(n)
    return triangulo[n-1]

while True:
    grado = input("Grado del triangulo : ")
    if ( not grado.isnumeric() ):
         print("Error, ",grado," no es un numero ")
    elif ( int(grado) < 1 ):
         print("Error, numero ",grado," menor a 1")
    else:
        triangulos = tri_pascal(int(grado))
        i = 0
        for fila in triangulos:
            print("n =",i,":",end="")
            i = i + 1
            for coef in fila:
                print(coef," ",end="")
            print()
        break
