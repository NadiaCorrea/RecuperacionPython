"""15.- Realizar un método que reciba como argumento una cadena y un carácter
 y nos devuelva el número de caracteres que hay 
entre la primera y la última aparición de un carácter concreto."""

def contarCaracteres(cadena, caracter):
    posiciones = []
    i = 0 
    
    while i < len(cadena): 
        if cadena[i] == caracter:
            posiciones.append(i) #guardo todos los que encuentre 
        i = i + 1
        
    if len(posiciones) <= 1: 
        result = -1
    else: 
        result = posiciones[len(posiciones) -1 ] - posiciones[0]  
            
    return result

def contarCaracteres2(cadena, caracter):
    result = -1
    primer = -1
    ultimo = -1 
    
    for i in range(0, len(cadena)):
        if cadena[i] == caracter:
            if primer == -1:
                primer = i
            ultimo = i
    
    if primer != ultimo:
        result = ultimo - primer
    else:
        result = -1
    
    return result



palabra = input("Introduce una palabra: ")
letra = input("Introduce una letra: ")

print(contarCaracteres(palabra, letra))
print(contarCaracteres2(palabra, letra))