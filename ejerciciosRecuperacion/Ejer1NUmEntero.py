# 1.- Realizar un programa que lea un número entero por teclado e indique si el número se puede expresar
# como el cuadrado de un número entero.

import math
num = int (input("Introduce un número entero: "))

result = math.sqrt(num) 

if result % 1  == 0:
    print("Se puede expresar como el cuadrado de un número entero.")
else:
    print("No se puede expresar como el cuadrado de un número entero.")