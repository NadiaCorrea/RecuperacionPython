"""7.- Escribir un programa que pida un número entero y escriba el número en binario."""

num = int(input("Introduce un número: "))
cadena = ''
cadenaBinario =''

dividendo = num 
divisor = 2
cociente = dividendo // divisor

while (cociente > 1):
    resto = dividendo % divisor   
    cociente = dividendo // divisor
    if cociente == 1: 
        cadena = cadena + str(resto) + str(cociente)
    else: 
        cadena = cadena + str(resto)
    dividendo = cociente
    
    
i = len(cadena)-1

while i >= 0: 
    cadenaBinario = cadenaBinario + str(cadena[i])
    i= i-1
    
print(cadenaBinario)
    