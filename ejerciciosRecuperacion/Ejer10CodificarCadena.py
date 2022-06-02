"""Realizar los siguientes métodos:

Un método llamado codificar que reciba la cadena a codificar y la clave de codificación 
y devuelva un String con la cadena codificada.
Un método llamado descodificar que reciba la cadena codificada y la clave de codificación 
y devuelva un String con la cadena descodificada."""

clave = [3,6,5,1,8,2,9,4,7,0]

#Si deseamos codificar “2380”. La cadena codificada es “5173”. 
#Como vemos, cada número se sustituye por el que ocupa su posición en la clave de codificación.

def codificar(cadena, clave):
    result = ''
    
    for i in cadena: 
        result = result + str(clave[int(i)])
    return result

def descodificar(cadena, clave):
    result = ''
    
    for i in cadena:
        result = result + str(clave[int(i)])
    return result

#Principal 

print('1. Codificar\n2. Descodificar\n3.Salir')
opc = int(input("¿Qué quieres hacer?"))

while (opc != 3):

    if opc == 1:
        cadena = input('Introduce la cadena a codificar: ')
        print(codificar(cadena, clave))
    
    elif opc ==2:
        cadenaCod = input('Introduce la cadena a descodificar:')
        print(descodificar(cadenaCod, clave))
    
    else:
        print('Error. Opción no válida.')
    
    print('1. Codificar\n2. Descodificar\n 3.Salir')
    opc = int(input("¿Qué quieres hacer?"))
        