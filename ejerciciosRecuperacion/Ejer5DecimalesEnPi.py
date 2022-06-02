"""5.- Escribir un programa que pregunte cuántas decimales (máximo 4 decimales) 
queremos en el número pi, y muestre el número pi con los decimales adecuados. 
Para calcular el número pi  se puede utilizar la siguiente fórmula pi = 4* (1 -1/3 + 1/5 -1/7 ….) """
from math import pi

numDecimales = int(input("¿cuántos decimales quieres en el número pi?: "))

result = round(pi, numDecimales);
print(result)

