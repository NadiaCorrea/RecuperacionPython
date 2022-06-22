""" EJERCICIO 2
Realizar un programa que solicitará cuantos alumnos tiene la clase. 
El programa validará que este dato es correcto, y si
no volverá a solicitarlo. Para cada uno de ellos solicitará su nota.
El programa informará de la mejor nota así como la nota media de los aprobados. 
Si no hay aprobados se mostrará el
mensaje “No hay aprobados. No puede calcularse la media"""


notas = []

#solicito el total de alumnos
totalAlum = int(input('Introduce el total de alumnos: '))
while  totalAlum  <= 0:  
    print('Error. El total de alumnos debe ser superior a 0.')
    totalAlum = int(input('Introduce el total de alumnos: '))

#solicito las notas y las guardo en el array
for i in range (0, totalAlum):
    nota = int(input('Introduce la nota: '))
    notas.append(nota)
    
#para saber cual es la mejor nota asigno la primera nota del array como mejor para poder compararla    
mejor = notas[0]
suma = 0
contador = 0

for j in notas:
    if j > mejor:
        mejor = j
    if j >= 5:
        suma = suma + j
        contador = contador + 1

print('la mejor nota es: ' + str(mejor))

if suma == 0:
    print('No hay aprobados. No puede calcularse la media')
else: 
    media = suma/contador
    media = round(media,2)
    print('La media es: ' + str(media))
        
        
        
        
        