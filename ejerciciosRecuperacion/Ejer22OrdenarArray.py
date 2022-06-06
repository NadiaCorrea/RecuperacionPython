"""22.- Hacer un programa que inicialice un vector de números con valores aleatorios, 
y posterior ordene los elementos de menor a mayor."""
from random import randint

#uso esta variable por si luego queremos cambiar el total de número en el array
TOTAL_NUM = 7
numRandom = []

#añado numeros aleatorios del 1 al 25 al array

for i in range(0,TOTAL_NUM):
    numRandom.append(randint(1,25))

print(numRandom)
print(sorted(numRandom))



