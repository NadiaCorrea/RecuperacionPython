"""EJERCICIO 1
Se desea realizar un programa que calcule el sueldo de un trabajador dependiendo 
de número de horas mensuales trabajadas. 
Se solicitará el número de horas base trabajado, la categoría 
y el número de años trabajado en la empresa,
en función de la categoría se pagará 
30 euros la hora si la categoría es “APRENDIZ”, 
40 euros la hora si la categoría es “MAESTRO” y 
50 euros la hora si la categoría es “SUPER MAESTRO”.
 
También se deberá tener en cuenta lo siguiente:

• Si lleva 10 o más años en la empresa se le aplica un aumento del 10.2%.
• Si lleva menos de 10 años pero 5 o más se le aplica un aumento del 7%.
• Si lleva menos de 5 años se le aplica un aumento del 5%.
• El número máximo de años que puede estar en la empresa es 50
El programa debe pedir los datos y si no son correctos volver a pedirlos."""

def calcularPagoCategoria(categoria, horas):
    result = 0
    
    if categoria.upper() == 'APRENDIZ':
        result = horas * 30
    elif categoria.upper() == 'MAESTRO':
        result = horas * 40
    else:
        result = horas * 50
    
    return result  
    
def calcularPagoFinal(pago, annos):
    result = 0
    
    if annos > 10: 
        result = pago + (pago * 0.102)
    elif annos >= 5 and annos <= 9:
        result = pago + (pago * 0.07)
    else: 
        result = pago + (pago * 0.05)

    return result


#Principal - petición y comprobación de datos 

horas = int(input('Introduce el número de horas trabajadas: '))
while horas <= 0: 
    print('Error. el número de horas debe ser mayor que 0.')
    horas = int(input('Introduce el número de horas trabajadas: '))

categoria = input('Introduce la categoría (APRENDIZ, MAESTRO, SUPER MAESTRO): ')
while categoria.upper() != 'APRENDIZ' and categoria.upper() !=  'MAESTRO' and categoria.upper() != 'SUPER MAESTRO':
    print('Error. La categoría no es válida')
    categoria = input('Introduce la categoría (APRENDIZ, MAESTRO, SUPER MAESTRO): ')

annos = int(input('Introduce el número de años trabajados: '))
while annos <= 0 or annos > 50: 
    print('Error. Lo años trabajados deben ser mayor que 0 y menor que 50')
    annos = int(input('Introduce el número de años trabajados: '))

pagoSinPlus = calcularPagoCategoria(categoria, horas)
pagoFinal = calcularPagoFinal(pagoSinPlus, annos)

print('El sueldo final es: ' + str(pagoFinal))




