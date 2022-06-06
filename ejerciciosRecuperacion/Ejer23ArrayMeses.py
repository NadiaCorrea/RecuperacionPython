"""23.- Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) 
y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar un vector. 
Para simplificarlo vamos a suponer que febrero tiene 28 días."""

meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mesNum = int(input("Introduce un número del 1 al 12: "))


#buscar el mes y días
mes = meses[mesNum -1]
numDias = dias [mesNum -1]

print('El mes es: ' + str(mes) + ' y tiene ' + str(numDias) + ' días.') 
