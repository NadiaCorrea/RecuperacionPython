"""25.- Queremos guardar los nombres y la edades de los alumnos de un curso. 
Realiza un programa que introduzca el nombre y la edad de cada alumno. 
El proceso de lectura de datos terminará cuando se introduzca 
como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:
Todos lo alumnos mayores de edad.
Los alumnos mayores (los que tienen más edad)"""


nombres = []
edades = []
nombre = ''
edad = -1

while nombre != '*': 
    nombre = input("Introduce el nombre del alumno (introduce * para terminar): ")
    if nombre != '*': 
        nombres.append(nombre)
        edad = int(input("Introduce su edad: "))
        edades.append(edad)
        
mayorEdad = []
mayor = edades[0]
for i in range (0, len(edades)):
    if edades[i] > mayor: 
        mayor = edades[i]
    if edades[i] >= 18:
        mayorEdad.append(nombres[i])
 

mayores = []
for j in range (0,len(edades)):
    if edades[j] == mayor:
        mayores.append(nombres[j])
                
print(mayorEdad)       
print(mayores)