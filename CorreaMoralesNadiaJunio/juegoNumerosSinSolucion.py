''' Se quiere simular un juego en el que participan 2 jugadores y otra persona que 
hace de árbitro. Cada jugador elige 10 números en el rango [1, 100], pudiendo estar repetidos. 
A continuación, el árbitro, sin conocer los números que ha elegido cada jugador, 
selecciona 2 números A y B.

El programa debe ser capaz de calcular cuántos números de los seleccionados por cada jugador 
están comprendidos entre los valores A y B. Ganará el jugador que más números tenga en dicho 
intervalo. Para realizar el juego se pide realizar los siguientes métodos y el programa 
principal para el juego.'''

import random
from Tools.demo.spreadsheet import colnum2name

NUM_NUMEROS = 10
VALOR_MINIMO_NUMEROS = 1
VALOR_MAXIMO_NUMEROS = 100

## Funcion de devuelve un número aleatorio entre el valor mínimo y el valor máximo. 
## Esta función se utilizará para elegir los números que debe elegir el árbitro.

def getNumero():
    numero = random.randint(VALOR_MINIMO_NUMEROS, VALOR_MAXIMO_NUMEROS)
    return numero
        
## Función que solicita y devuelve un número comprendido entre el valor mínimo y el valor máximo.
## Si el valor que introduce el usuario no es válido se deberá pedir otra vez hasta que se 
## introduzca un valor válido
def solicitarNumero():
    num = int(input('Introduce un número: '))
    while num < VALOR_MINIMO_NUMEROS or num > VALOR_MAXIMO_NUMEROS: 
        print('Error. El número debe estar comprendido entre: ' + str(VALOR_MINIMO_NUMEROS) + ' ' + str(VALOR_MAXIMO_NUMEROS))
        num = int(input('Introduce un número: '))
    return num

## Función que recibe como argumento una lista (que estará vacia) y rellena esta lista con los 
## números que se le piden al usuario. Es decir, se deben solicitar Num_numeros e irlos almacenando
## en la lista.
def pedirNumeros(lista):
    for i in range(0, NUM_NUMEROS):
        lista.append(solicitarNumero())

## Función que devuelve el valor mínimo de los dos que se le pasa como argumento
def minimo(num1, num2):
    min = num1
    
    if num2 < min:
        min = num2
    
    return min 

## Función que devuelve el valor máximo de los dos que se le pasa como argumento
def maximo(num1, num2):
    max = num1
    
    if num2 > max:
        max = num2 
    
    return max

## Función que devuelve el número de números de la lista que está comprendido entre el 
## número A y el número B.
def aciertos(lista, numeroA, numeroB):
    min = minimo(numeroA, numeroB)
    max = maximo(numeroA, numeroB)
    contador = 0
    
    for i in lista: 
        if i >= min and i <= max: 
            contador = contador + 1
            
    return contador 

## Función que devuelve una cadena con los números de la lista separados por espacio.
def imprimirNumeros(lista):
    mensaje = ''
    for num in lista:
        mensaje = mensaje + str(num) + ' '
    return mensaje
        
 
## Programa principal        
numerosJugador1 = []
numerosJugador2 = []
numeroA = getNumero()
numeroB = numeroA
while numeroB == numeroA:
    numeroB = getNumero()
print("Jugador número 1")
pedirNumeros(numerosJugador1)
print("Jugador número 2")
pedirNumeros(numerosJugador2)
print(imprimirNumeros(numerosJugador1))
print(imprimirNumeros(numerosJugador2))
aciertosJugador1 = aciertos(numerosJugador1, numeroA, numeroB)
aciertosJugador2 = aciertos(numerosJugador2, numeroA, numeroB)
if aciertosJugador1 == aciertosJugador2:
    print("Empate")
elif aciertosJugador1 < aciertosJugador2:
    print("Gana el jugador 2")
else:
    print("Gana el jugador 1")
  

