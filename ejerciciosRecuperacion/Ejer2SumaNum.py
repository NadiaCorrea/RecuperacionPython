
"""Realizar un programa que lea números enteros hasta que se pulse un número negativo
 y muestre la suma de la suma de los números introducidos, 
 desde 1 al número al que se ha introducido. Por ejemplo, 
 si se introduce el 3, el 5, el 10 y el -2. 
Se deberá sumar 1+2+3+1+2+3+4+5+1+2+3+4+5+6+7+8+9+10 """

suma = 0
num = int(input("Introduce un número positivo (para salir introduce un número negativo): "))
while (num > 0):
    for i in range(1,num +1):
        suma = suma + i
    num = int(input("Introduce un número positivo (para salir introduce un número negativo): "))   

print("La suma es: " + str(suma))