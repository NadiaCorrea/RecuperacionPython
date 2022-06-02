"""8.- Se desea realizar un programa para validar la identificación de la seguridad social. 
El número  siempre está formado por 2 partes que llamaremos parte A y parte B. 
El separador de las partes es un guión ‘-’. 
La parte A está formada sólo por caracteres alfabéticos en mayúsculas, al menos dos. 
La parte B está formada sólo por caracteres numéricos, al menos 2.
Tanto la parte A como la parte B pueden ser la primera. 
Se pide realizar un programa en pseudocódigo que solicite la identificación de la seguridad social 
e informe de si es o no válida. """


def buscarGuion(cadena):
    pos = -1
    for i in range(0,len(cadena)): 
        if cadena[i] == '-':
            pos = i 
    return pos


def obtenerParte1 (cadena, pos): 
    parte = ''   
    i = 0
    while i < pos:
        parte = parte + cadena[i]
        i = i+1
    return parte


def obtenerParte2(cadena, pos):
    parte = ''
    i = pos + 1
    while i < len(cadena):
        parte = parte + cadena[i]
        i = i + 1
    return parte
        
def compararA(cadena):
    result = False
    mayus = 0 
    otros = 0
    
    for i in cadena:
        if (ord(i) >= 65) and (ord(i) <= 90):
            mayus = mayus + 1
        else:
            otros = otros + 1
            
    if (mayus >= 2) and (otros == 0): 
        result = True    
    return result

def compararB(cadena):
    result = False
    num = 0 
    otros = 0 
    
    for i in cadena:
        if (ord(i) >=48) and (ord(i) <= 57):
            num = num + 1
        else:
            otros = otros + 1
    
    if num >= 2 and otros == 0: 
        result = True 
    return result

segsocial = input("Introduce la identificación se la seguridad social: ")

posicion = buscarGuion(segsocial)
parte1 = obtenerParte1(segsocial, posicion)
parte2 = obtenerParte2(segsocial, posicion)

if (compararA(parte1) and compararB(parte2)) or (compararB(parte1) and compararA(parte2)):
    print('Es correcta.')
else:
    print('Es incorrecta.')


"""Ejemplos de ejecución:

Introduzca la identificación de la SS: AB-345
Es correcta

Introduzca la identificación de la SS: 345-AB
Es correcta

Introduzca la identificación de la SS: 3A45-AB
Es incorrecta

Introduzca la identificación de la SS: 3-45-AB
Es incorrecta"""

