"""4.- Escribir un programa que calcule el mínimo, el máximo y la media de una lista de números enteros 
positivos introducidos por el usuario. 
La lista debe finalizar cuando se produzca un número negativo. """

num = int(input("Introduce un número positivo (para salir introduce un número negativo): "))
listaNum = []
while num > 0: 
    listaNum.append(num)
    num = int(input("Introduce un número positivo (para salir introduce un número negativo): "))

menor = listaNum[0]
mayor = listaNum[0]
suma = 0 
for i in listaNum: 
    if i < menor: 
        menor = i
    if i > mayor: 
        mayor = i
    suma = suma + i

media = suma / len(listaNum)

print("El número mínimo de la lista es: " + str(menor))
print("El número máximo de la lista es: " + str(mayor))
print("La media de la lista es " + str(media))

