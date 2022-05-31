"""Realiza un programa que calcule el precio de unas entradas de cine en función del número de personas
y del día de la semana. 
El precio general de una entrada son 8 euros. 
El miércoles (día del espectador), el precio es de 5 euros. 
Los jueves es el día de la pareja, por lo que la entrada para dos cuesta 11 euros.

Por ejemplo, si un jueves, un grupo de 6 personas compran entradas, el precio total sería de 33 euros ya
que son 3 parejas; pero si es un grupo de 7, pagarán 3 entradas de pareja más 1 individual que son 41
euros (33 + 8). Además si dispone de la tarjeta CineJacaranda se obtiene un 10% de descuento."""

numEntradas = int(input("Introduce el número de entradas que deseas: "))
dia = input("Introduce el día se la semana (L,M,X,J,V,S,D): ")
tarjeta = input("¿Tienes tarjeta CineJacaranda (S/N)?: ")
total = 0

if dia == 'X':
    total = numEntradas * 5    
elif dia == 'J':
    total = ((numEntradas//2) * 11) + ((numEntradas%2) * 8)     
else:
    total = numEntradas * 8


if tarjeta == 'S':
        total = total - (total*0.10)
        
print("El precio de su compra es " + str(total) + " euros.")