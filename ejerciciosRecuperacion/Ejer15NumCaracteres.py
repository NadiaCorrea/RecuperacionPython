"""15.- Realizar un método que reciba como argumento una cadena y un carácter
 y nos devuelva el número de caracteres que hay 
entre la primera y la última aparición de un carácter concreto."""

def contarCaracteres(cadena, caracter):
    result = 0 
    encontrado = False
    i = 0
    posicion1 = -1
    
    while i < len(cadena) and encontrado == False: #para encontrar la primera 
        if cadena[i] == caracter:
            encontrado == True
            posicion1 = i
    
    return result





palabra = input("Introduce una palabra: ")
letra = input("Introduce una letra: ")