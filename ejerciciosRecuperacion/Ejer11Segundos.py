"""11.- Escribir un programa que solicite un número de segundos y 
muestre por pantalla dicha cantidad de tiempo en horas, minutos y segundos. 
1 hora = 60 minutos = 3600 segundos​ 
1 minuto = 60 segundos."""

segundos =  int (input('Introduce la cantidad en segundos: '))

minutos = 0
horas = 0

if segundos > 60:
    minutos = segundos//60
    segundos = segundos % 60
    if minutos > 60:
        horas = minutos//60 
        minutos = minutos % 60
        
print('Son ' +str(horas) + ' hora(s), ' + str(minutos) + ' minuto(s) y ' + str(segundos) + ' segundo(s).')
