"""16.- Realizar un método que reciba un String y 
devuelva el resultado de sumar todos los dígitos que hay en el mismo. 
Por ejemplo si recibe “Peras 23, Manzanas 8” devolverá 13 (2+3+8)"""

def esDigito(caracter):
    digito = False
    
    if ord(caracter) >= 48 and ord(caracter) <=57:
        digito = True
    return digito
    
def sumaDigitos(cadena):
    suma = 0
        
    for i in cadena:
        if esDigito(i) == True:
            suma = suma + int(i)
        
    return suma


frase = input("Introduce la frase: ")
print(sumaDigitos(frase))