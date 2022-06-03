"""19.- Crear un vector de 5 elementos de cadenas de caracteres, 
inicializa el vector con datos leídos por el teclado. 
Copia los elementos del vector en otro vector pero en orden inverso, 
y muéstralo por la pantalla."""

arrayCadenas = []
arrayAux = []

for i in range (0,5):
    cadena = input("Introduce un palabra: ")
    arrayCadenas.append(cadena)

j = len(arrayCadenas) - 1

while j >= 0:
    arrayAux.append(arrayCadenas[j])
    j = j -1

print(arrayAux) 
