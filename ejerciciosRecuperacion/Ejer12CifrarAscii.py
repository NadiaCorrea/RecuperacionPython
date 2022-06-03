"""12.-  Escribir un programa que tenga un método que permita cifrar cadena de caracteres 
usando el algoritmo de cifrado simple consistente en asignar a cada carácter aquel que resulte 
de sumar un valor a su código ASCII.  
El método deberá tener como argumento la cadena a cifrar y el número a sumar 
(ambos valores deberán pedirse por teclado antes de llamar a la función). 
El método debe pasar la cadena a mayúsculas y devolver la clave cifrada. 
Nota. El valor de la Z es 90, por lo que si algún valor da por ejemplo 91 
se debe asignar la A que es el 65."""


def pasarMayuscula(cadena):
    cadenaAux = ''
    
    for i in cadena:
        letra = ord(i) - 32
        cadenaAux = cadenaAux + chr(letra)
    return cadenaAux

def cifrarAscii(cadena, num):
    cifrado = ''
    cadenaAux = pasarMayuscula(cadena)
    
    for i in cadenaAux: 
        result = ord(i) + 20
        
        if result > 90:
            result = result - 25
        
        cifrado = cifrado + chr(result)
    
    return cifrado 

frase = input("Introduce la palabra a cifrar: ")
num = int(input("Introduce en número a sumar: "))

print(cifrarAscii(frase, num))
