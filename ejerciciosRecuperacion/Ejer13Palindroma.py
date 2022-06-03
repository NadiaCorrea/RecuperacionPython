"""13.- Escribir un programa que tenga una función que determine si una cadena de caracteres 
es palíndroma o no 
(se lee igual de izquierda a derecha que de la derecha a izquierda)."""

def leerDerecha(cadena):
    derecha = ''
    
    i = len(cadena) -1
    while i >= 0:
        derecha = derecha + cadena[i]
        i = i -1
    return derecha

palabra = input("Introduce una palabra: ")

if palabra == leerDerecha(palabra):
    print('Es palíndroma.')
else: 
    print('No es palíndroma.')
    
