"""26.- Queremos guardar la temperatura mínima y máxima de 5 días. 
realiza un programa que de la siguiente información:
La temperatura media de cada día
Los días con menos temperatura
Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima 
coincide con ella. si no existe ningún día se muestra un mensaje de información."""

tempMin = []
tempMax = []
tempMedia = []
diasMenos = []
media = 0
minima = 100

for i in range(0,5):
    diaMin = int(input("Introduce la temperatura mínima del día: "))
    tempMin.append(diaMin)
    if diaMin < minima:
        minima = diaMin
    diaMax = int(input("Introduce la temperatura máxima del día: "))
    tempMax.append(diaMax)
    media = (diaMax + diaMin)/2
    tempMedia.append(media)

for i in range(0, len(tempMin)): 
    if tempMin[i] == minima:
        diasMenos.append(i + 1)
    
print('Las temperaturas medias de cada día son: '+ str(tempMedia))
print('Día(s) con menos temperatura: ' + str(diasMenos))

temp = int(input("Inserta una temperatura: "))

diasMax = []

for i in range(0,len(tempMax)):
    if tempMax[i] == temp:
        diasMax.append(i + 1)
    
if len(diasMax) > 0:
    print('Día(s) que coinciden con la temperatura: ' + str(diasMax))
else:
    print('No existe ningún día con esa temperatura.')