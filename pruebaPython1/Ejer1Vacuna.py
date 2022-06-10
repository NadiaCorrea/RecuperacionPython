"""1.- Realiza un programa que le pida al usuario su edad 
y que le pregunte si ha pasado el Covid o no, 
así como si ha recibido la vacuna de Pfizer, Moderna o Astrazeneca. 
En función de la respuesta se debe   informar   al   usuario   
si   debe   volver   a   vacunarse   o   no   
teniendo   en   cuenta   las   siguientes condiciones: 

• Si ha recibido Astrazeneca, haya pasado el covid o no 
e independientemente de la edad debe volver a vacunarse. 
• Si ha recibido Moderna y es mayor de 60 años, 
sólo debe volver a vacunarse si no ha pasado el covid. 
En otro caso, lo que han recibido Moderna no deben volver a vacunarse. 
• Si ha recibido Pfizer y no ha pasado el covid, debe volver a vacunarse,
 y si lo ha pasado sólo se vacunará si es mayor de 70 años.

Si el usuario no introduce los valores correctos, 
se debe mostrar un mensaje de error y volver a solicitar los datos 
hasta que el usuario introduzca los datos de forma correcta. """
  

edad = int(input("Introduce tu edad: "))
while edad < 0: 
    print('Error. La edad debe ser mayor que 0.')
    edad = int(input("Introduce tu edad: "))

covid = input("Has pasado el covid(S/N): ")
while covid != 'S' and covid != 'N':
    print('Error. La respuesta debe ser S para sí y N para no.')
    covid = input("Has pasado el covid(S/N): ")

vacuna = input("¿Qué vacuna has recibido? Pfizer, Moderna o Astrazeneca: ")
while vacuna != 'Pfizer' and vacuna != 'Moderna' and vacuna != 'Astrazeneca':
    print('Error. Las vacunas han de ser Pfizer, Moderna o Astrazeneca.')
    vacuna = input("¿Qué vacuna has recibido? Pfizer, Moderna o Astrazeneca: ")
 
#Si ha recibido Astrazeneca, haya pasado el covid o no e independientemente de la edad debe volver a vacunarse.
if vacuna == 'Astrazeneca':
    print('Debe volver a vacunarse.')

#Si ha recibido Moderna y es mayor de 60 años, sólo debe volver a vacunarse si no ha pasado el covid.
#En otro caso, lo que han recibido Moderna no deben volver a vacunarse.
elif vacuna == 'Moderna':
    if edad > 60 and covid == 'N':
        print('Debe volver a vacunarse.')
    else:
        print('No debe volver a vacunarse.')

#Si ha recibido Pfizer y no ha pasado el covid, debe volver a vacunarse,
#y si lo ha pasado sólo se vacunará si es mayor de 70 años.    
elif vacuna == 'Pfizer':
    if covid == 'N':
        print('Debe volver a vacunarse.')
    elif covid == 'S' and edad > 70:
        print('Debe volver a vacunarse.')
    else: 
        print('No debe volver a vacunarse.')

    
