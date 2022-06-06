"""24.- Programa que declare tres vectores ‘vector1’, ‘vector2’ y ‘vector3’ 
de cinco enteros cada uno, 
pida valores para ‘vector1’ y ‘vector2’ 
y calcule vector3=vector1+vector2."""

vector1 = []
vector2 = []
vector3 = []

print('Vamos a introducir 5 número para crear el primer grupo: ')
for i in range (0,5):
    numV1 = int(input("Introduce un número: "))
    vector1.append(numV1)

print('Vamos a introducir 5 número para crear el segundo grupo: ')
for j in range (0,5):
    numV2 = int(input("Introduce un número: "))
    vector2.append(numV2)
    
for x in range(0,5):
    result = vector1[x] + vector2[x]
    vector3.append(result)

print(vector3)

