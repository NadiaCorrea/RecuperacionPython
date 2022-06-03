"""14.- Realizar un método que convierta una cadena de caracteres 
en su valor entero correspondiente."""

def darValor(cadena):
    result = 0
    
    for i in cadena:
        result = result + ord(i)
    return result


palabra = input("Introduce una palabra: ")

print(darValor(palabra))