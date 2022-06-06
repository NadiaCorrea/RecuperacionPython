""" 6.- Escribir un programa que lea un número entero y lo descomponga en factores primos. 
Por ejemplo 18 = 2  * 3 *3"""
from setuptools._distutils.util import subst_vars

num = int(input("Introduce un número: "))

cociente = num
dividendo = 2
factoresPrimos = []

while cociente != 1:
    if cociente%dividendo == 0:
        factoresPrimos.append(dividendo)
        cociente = cociente//dividendo
        dividendo = 2
    else:
        dividendo = dividendo + 1

result = str(num) + ' = '
for i in factoresPrimos:
    result = result + str(i) + ' * '

result = result[0:len(result)-2]

print(result)