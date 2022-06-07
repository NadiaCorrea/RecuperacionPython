"""Crea una programa que tenga muestre un mensaje para elegir las siguientes opciones: 
1. esCapicua: Devuelve verdadero si el n�mero que se pasa como par�metro es capic�a y falso en caso contrario. 
2. siguientePrimo: Devuelve el menor primo que es mayor al n�mero que se pasa como par�metro. 
3. digitos: Cuenta el n�mero de d�gitos de un n�mero entero. 6. voltea: Le da la vuelta a un n�mero. 
4. digitoN: Devuelve el d�gito que est� en la posici�n n de un n�mero entero. Se empieza contando por el 0 y de izquierda a derecha. 
5. posicionDeDigito: Da la posici�n de la primera ocurrencia de un d�gito dentro de un n�mero entero. Si no se encuentra, devuelve -1. 
6. quitaPorDetras: Le quita a un n�mero n d�gitos por detr�s (por la derecha). 
7. quitaPorDelante: Le quita a un n�mero n d�gitos por delante (por la izquierda). 
8. pegaPorDetras: A�ade un d�gito a un n�mero por detr�s. 
9. pegaPorDelante: A�ade un d�gito a un n�mero por delante. 
10. trozoDeNumero: Toma como par�metros las posiciones inicial y final dentro de un n�mero y devuelve el trozo correspondiente. 
11. juntaNumeros: Pega dos n�meros para formar uno."""
from test.badsyntax_future3 import result


#Devuelve verdadero si el n�mero que se pasa como par�metro es capic�a y falso en caso contrario.
def esCapicua(cadena):
    result = 'Falso'
    numaux = ''
    i = len(cadena) -1
    while i >= 0:
        numaux = numaux + cadena[i]
        i= i -1
        
    if numaux == cadena:
        result = 'Verdadero' 
        
    return result    
#Devuelve el menor primo que es mayor al n�mero que se pasa como par�metro.
#def siguientePrimo(num):


#Cuenta el n�mero de d�gitos de un n�mero entero.
def digitos(cadena):
    counter = 0 
    for i in cadena:
        if ord(i) >= 48 and ord(i) <= 57:
            counter = counter + 1
    
    return counter

#Devuelve el d�gito que est� en la posici�n n de un n�mero entero. Se empieza contando por el 0 y de izquierda a derecha.    
def digitoN(cadena, posicion):
    result = ''
    if posicion >=0 and posicion < len(cadena):
        result = cadena[posicion] 
        
    return result

#Da la posici�n de la primera ocurrencia de un d�gito dentro de un n�mero entero. 
#Si no se encuentra, devuelve -1.
    
def posicionDeDigito(cadena, digito):
    result = -1
    i = 0 
    encontrado = False
    
    while i < len(cadena) and encontrado == False:
        if cadena [i] == digito:
            result = i 
            encontrado = True
    
    return result

#Le quita a un n�mero n d�gitos por detr�s (por la derecha).    
def quitaPorDetras(cadena, digito):
    if digito < len(cadena):
        i = len(cadena) - digito
        result = cadena[0:i]
    
    return result
    
    
    
    
"""    
#Le quita a un n�mero n d�gitos por delante (por la izquierda).    
def quitaPorDelante(num):
    
#A�ade un d�gito a un n�mero por detr�s.
def pegaPorDetras(num):

#A�ade un d�gito a un n�mero por delante.    
def pegaPorDelante(num):
#Toma como par�metros las posiciones inicial y final dentro de un n�mero y devuelve el trozo correspondiente.    
def TrozoDeNumero(num):
#Pega dos n�meros para formar uno.    
def juntaNumeros(num):"""

def menu():
    print("1. esCapicua\n2. siguientePrimo\n3. digitos\n4. digitoN\n5. posicionDeDigito\n6. quitaPorDetras\n7. quitaPorDelante\n8. pegaPorDetras\n9. pegaPorDelante\n10. TrozoDeNumero\n11. juntaNumeros\n12. Salir")

menu()
opc = int(input("�Qu� quieres hacer?: "))

while opc != 12:
    if opc == 1: 
        num = input("Introduce un n�mero: ")
        print(esCapicua(num))
        
    #elif opc == 2:
     #   num = input("Introduce un n�mero: ")
      #  print(siguientePrimo(num))
        
    elif opc == 3:
        num = input("Introduce un n�mero: ")
        print(digitos(num))
        
    elif opc == 4:
        num = input("Introduce un n�mero: ")
        print(digitoN(num))
        
    elif opc == 5:
        num = input("Introduce un n�mero: ")
        print(posicionDeDigito(num))
        
    elif opc == 6:
        num = input("Introduce un n�mero: ")
        print(quitaPorDetras(num))
    """elif opc == 7:
        num = input("Introduce un n�mero: ")
        print(quitaPorDelante(num))
        
    elif opc == 8:
        num = input("Introduce un n�mero: ")
        print(pegaPorDetras(num))
        
    elif opc == 9:
        num = input("Introduce un n�mero: ")
        print(pegaPorDelante(num))
        
    elif opc == 10:
        num = input("Introduce un n�mero: ")
        print(TrozoDeNumero(num))
        
    elif opc == 11:
        num = input("Introduce un n�mero: ")
        print(juntaNumeros(num))"""
        
    elif opc == 12:
        print('Adi�s.')
    else: 
        print('Opci�n no valida.')
        
    menu()
    opc = int(input("�Qu� quieres hacer?: "))
