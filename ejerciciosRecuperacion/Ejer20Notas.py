"""20.- Se quiere realizar un programa que lea por teclado las 5 
notas obtenidas por un alumno (comprendidas entre 0 y 10). 
A continuación debe mostrar todas las notas, la nota media, 
la nota más alta que ha sacado y la menor."""

notas = []

for i in range(1,6):
    nota = int (input("Introduce la nota " + str(i) + ': '))
    while nota < 0 or nota > 10:
        print('Nota no valida.')
        nota = int (input("Introduce la nota " + str(i) + ': '))
    notas.append(nota)
        
menor = 11
mayor = 0
suma = 0

for i in notas:
    if i < menor:
        menor = i
    if i > mayor:
        mayor = i
    suma = suma + int(i)

media = suma / 5     

print('Notas: ' + str(notas) + '\nnota media: ' + str(media) + '\nnota más alta: ' + str(mayor) + '\nnota más baja: ' + str(menor))


