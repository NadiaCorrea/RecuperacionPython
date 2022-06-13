"""Un juguete tiene tres botones, dos de melodías: A y B 
(con dos músicas por botón) y otro P de apagado. 
Cada botón de melodía activa el juguete y al ser pulsado sucesivamente 
cambia de una a otra melodía. 
Es decir, si se pulsa el botón A una vez suena la melodía A1 
y si se vuelve a pulsar, la A2, y de igual modo sucede con el botón B. 
Crea un programa que lea por teclado el botón que se ha pulsado 
(independientemente de si es mayúscula o minúscula) 
y escriba la melodía que suena (melodía A1, ... melodía B2) 
y se apague cuando se pulse el botón P."""

boton = ''
melodiaA ='A2'
melodiaB = 'B2'

boton = input('Selecciona un botón A o B para escuchar una melodía y P para apagarlo:')

while boton != 'P' and boton != 'p': 
    if boton == 'A' or boton == 'a':
        if melodiaA != 'A1':
            melodiaA = 'A1'
        else: 
            melodiaA = 'A2'
        print('Suena la melodía ' + melodiaA)    
    elif boton == 'B' or boton == 'b':
        if melodiaB != 'B1':
            melodiaB = 'B1'
        else: 
            melodiaB = 'B2'
        print('Suena la melodía ' + melodiaB)
    else: 
        print('Opción no válida.')
        
    boton = input('Selecciona un botón A o B para escuchar una melodía y P para apagarlo:')

