"""21.- Programa que declare un vector de diez elementos enteros 
y pida números para rellenarlo hasta que se llene el vector 
o se introduzca un número negativo. 
Entonces se debe imprimir el vector (sólo los elementos introducidos)."""

arrayNum = []
num = 1

while len(arrayNum) < 10 and num > 0:
    num = int(input("Introduce un número positivo(número negativo para salir): "))
    if num > 0:
        arrayNum.append(num)    
        
print(arrayNum)