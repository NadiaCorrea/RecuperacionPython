"""Realizar un programa que pida números positivos y negativos 
hasta que se introduzca un 0. Una vez tenemos todos los números se debe llamar 
a una función que debe devolver una lista de unos o menos uno, 
segun el número sea mayor que el siguiente (un 1) o un menor (un -1)"""

numeros =[]
num = 1
result = []
while num != 0: 
    num = int(input("Introduce un número (positivo o negativo) y 0 para salir: "))
    if num != 0:
        numeros.append(num)
    
for i in range(0,len(numeros)-1):
    if numeros[i] > numeros[i+1]:
        result.append(1)
    else:
        result.append(-1)
        
print(result)