"""Ejercicio 2: 
El índice de masa corporal o IMC es una medida que se utiliza para evaluar 
el riesgo de enfermedad cardiovascular. 
Para su cálculo se divide el peso en kilogramos 
por la altura en metros elevados al cuadrado, de forma que un peso normal o normopeso 
estaría situado en un valor de IMC entre 18,5 y 24,9. 
Crea un programa que pida la altura,peso y edad de una persona y calcule e informe 
del valor y tipo de IMC obtenido atendiendo al siguiente criterio: 
<18,5 Peso insuficiente 
18,5-24,9 Normopeso 
25-29,9 Sobrepeso 
30-39,9 Obesidad 
>40Obesidad mórbida 
Además de facilitar el IMD, debe proporcionar un mensaje de recomendación sanitaria 
si la edad de la persona es superior a 45 y excede el normopeso (IMC >25), 
o bien, si ésta tiene obesidad (IMC >30). Por ejemplo: 
Para un peso de 90 kilogramos y una talla de 1.80metros, su IMC es: 27.78 
Usted se encuentra en el grupo: Sobrepeso. 
Caso 1 - Dada suedadeIMCes recomendable que cuide su salud cardiovascular 
Caso 2 - Dado suIMCes muy recomendable que cuide su salud cardiovascular 
Este programa debe validar la información proporcionada 
y terminar cuando se introduzca un valor negativo en cualquier medida 
(edad, peso o tamaño). """

edad = 1
altura = 1
peso = 1
resultadoImc = ''
mensaje =''

def tipoImc(imc):

    if imc < 18.5:
        resultado= 'Peso insuficiente'
    elif imc > 18.5 and imc < 25:
        resultado = 'Normopeso'
    elif imc >= 25 and imc <30: 
        resultado = 'Sobrepeso'
    elif imc >= 30 and imc < 40:
        resultado = 'Obesidad'
    else:
        resultado = 'Obesidad mórbida'
    
    return resultado

while (edad > 0) and (altura > 0) and (peso > 0):
    edad = int(input("Introduce la edad: "))
    if edad > 0:
        altura = float(input("Introduce la altura: "))
        if altura > 0:
            peso =  int(input("Introduce el peso: "))
    
    imc = peso/ (altura**2)
    resultadoImc = tipoImc(imc)
    
    if imc > 25 and edad > 45:
            mensaje = 'Dada su edad e IMC es recomendable que cuide su salud cardiovascular.'
    elif imc > 30 and edad < 46:
        mensaje = 'Dado su IMC es muy recomendable que cuide su salud cardiovascular. '
        
    print('Su IMC es: ' + str(round(imc,2)) + ' ' + resultadoImc + '.\n' + mensaje)
    