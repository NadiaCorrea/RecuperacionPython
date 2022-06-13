"""Juan recibe un regalo económico de su familia todos sus cumpleaños, 
de forma que cada año recibe 15€ más que en el anterior. 
Elabora un programa que pida una edad y calcule cuánto dinero en total 
ha recibido Juan en regalos de cumpleaños hasta esa edad 
sabiendo que en el primer cumpleaños le regalaron 20€. 
Ejemplo 1: 1 año ⇒ 20€  (recibe el 1º año) 
Ejemplo 2: 2 años  ⇒ 55€ (= 20€ tenía +35€ recibe el 2º año) 
Ejemplo 3: 3 años  ⇒ 105€ (=   55€ tenía +50€ recibe el 3º año) 
Ampliación: modifica el programa anterior para que tanto 
la cantidad que se incrementa cada año como el regalo inicial 
cambien en cada programa. """


REGALOINCIAL = 20
INCREMENTO = 15
suma = REGALOINCIAL
annoAnterior = REGALOINCIAL
annoActual = 0 

edad = int(input("Introduce tu edad: "))

for i in range (2,edad +1):
    annoActual = annoAnterior + INCREMENTO
    suma = suma + annoActual
    annoAnterior = annoActual

print('El dinero total recibido es: ' + str(suma))