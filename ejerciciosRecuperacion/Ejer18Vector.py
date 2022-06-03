"""18.- Realizar un programa que defina un vector llamado “vector_numeros” de 10 enteros, 
a continuación lo inicialice con valores aleatorios (del 1 al 10) 
y posteriormente muestre en pantalla cada elemento del vector 
junto con su cuadrado y su cubo."""
from random import randint

VECTOR_NUMEROS = 10

numAleatorios = []
cuadrado = 0
cubo = 0

for i in range (0, VECTOR_NUMEROS):
    numAleatorios.append(randint(1,10))

for i in numAleatorios:
    cuadrado = i**2 
    cubo = i**3
    print(str(i) + ' al cuadrado es: ' + str(cuadrado) + ' y al cubo es: ' + str(cubo))