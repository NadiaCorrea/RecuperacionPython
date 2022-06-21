"""Vamos a realizar un programa  para una gasolinera que tiene cuatro surtidores y quiere que cuando 
un coche llegue a nuestra gasolinera se le asigne el surtidor que esté más lleno dentro de su categoría 
(Diesel o Gasolina).
La gasolinera tiene 4 surtidores, dos de gasolina (el 1 y el 2) y dos de diesel, (el 3 y el 4) 
y deberemos realizar un programa con el siguiente menú:
1. Llenar surtidor.
2. LLegada de coche
3. Ver puntos
4. Comprobar ventas.
5. Ver surtidores.
6. Asignar precio de gasolina
7. Asignar precio de diesel
8. Salir.
 
Cuando se pulse la opción 1, nos deberá preguntar qué cantidad se va añadir al depósito del surtidor 
y qué surtidor se va a llenar, y añadir la nueva cantidad a la cantidad que tiene el depósito del surtidor. 
No se pueden introducir cantidades negativas porque no se puede vaciar el surtidor.
Con la opción 2 se deberá preguntar la matrícula del coche (se deberá comprobar que es el formato adecuado, 
4 números y 3 letras), si el coche ya ha estado en nuestra gasolinera debemos ver si es diesel o gasolina, 
preguntarle cuánto dinero quiere gastar en gasolina o diesel (Tendrá que ser cómo mínimo 10 euros y 
cómo máximo dos decimales) quiere y asignarle el surtidor adecuado. Se debe asignar el surtido más lleno 
de los dos disponibles. Si el coche no ha estado en nuestra gasolinera nunca debemos preguntar si es diesel o gasolina, 
lmacenarlo para no tener que preguntarle más veces, preguntar cantidad y asignarle el surtidor. En ambos casos se deberá 
almacenar el dinero gastado ya que vamos a ir dandole puntos según el dinero que se ha gastado en la gasolinera..
En la opción 3 se le pedirá la matrícula y se le dirá los puntos que tiene. Se les dará un punto por cada 10 euros gastados
en nuestra gasolinera. Si la matrícula no está registrado se le dirá que no es un cliente de nuestra gasolinera.
En la opción 4 se deberá mostrar un listado con todos las matriculas de coches que han respostado en nuestra gasolinera 
junto con el total gastado.
En la opción 5 se deberá mostrar la cantidad de gasolina o diesel que hay en cada surtidor.
La opción 6 y 7 servirá para asignar el precio de la gasolina y el diesel. Por supuesto este precio será superior a 1 y 
podrá tener 3 decimales (las gasolineras son así). Al empezar el programa también se deberán pedir los precios para 
poder trabajar con el programa.
La opción 8 termina la ejecución del programa."""

def menu():
    resultado = '1. Llenar surtidor\n2. LLegada de coche\n3. Ver puntos\n4. Comprobar ventas\n5. Ver surtidores\n6. Asignar precio de gasolina\n7. Asignar precio de diesel\n8. Salir'
    return resultado

def comprobarMatricula(matricula):
    result = False
    digito = 0
    letra = 0

    for i in range(0,4):
        if ord(matricula[i]) >= 48 and ord(matricula[i]) <= 57: 
            digito = digito + 1
    
    for j in range(4,len(matricula)):
        if (ord(matricula[j]) >= 65 and ord(matricula[j]) <= 90) or (ord(matricula[j]) >= 97 and ord(matricula[j]) <= 122):
            letra = letra + 1
    
    if digito == 4 and letra == 3: 
        result = True
        
    return result

def comprobarCombustible(matricula):
    tipo = ''
    
    if matricula in matriculasdiesel:
        tipo = 'DIESEL'
    elif matricula in matriculasgasolina:
        tipo = 'GASOLINA'  
    
    return tipo

def asignarSurtidor(tipo, cantidad):
    result = -1
    cantidadprevia = 0 
    
    if tipo == 'GASOLINA':
    
        if surtidores[0] >= surtidores[1]:
            cantidadprevia = surtidores[0]
            surtidores[0] = cantidadprevia -cantidad
            result = 1
            
        else:
            cantidadprevia = surtidores[1]
            surtidores[1] = cantidadprevia -cantidad
            result = 2
    
    elif tipo == 'DIESEL':
        if surtidores[2] >= surtidores[3]:
            cantidadprevia = surtidores[2]
            surtidores[2] = cantidadprevia -cantidad
            result = 3
        else:
            cantidadprevia = surtidores[3]
            surtidores[3] = cantidadprevia -cantidad
            result = 4
    return result

def asignarPuntos(matricula, dinero):
    posicion = -1
    puntosprevios = 0
    puntos = dinero//10
    dineroprevio = 0
    
    if matricula in matriculasdiesel:
        posicion = matriculasdiesel.index(matricula)
        puntosprevios = puntosdiesel[posicion]
        puntosdiesel[posicion] = puntosprevios + puntos
        dineroprevio = dinerodiesel[posicion]
        dinerodiesel[posicion] = dineroprevio + dinero
    elif matricula in matriculasgasolina:
        posicion = matriculasgasolina.index(matricula)
        puntosprevios = puntosgasolina[posicion]
        puntosgasolina[posicion] = puntosprevios + puntos
        dineroprevio = dinerogasolina[posicion]
        dinerogasolina[posicion] = dineroprevio + dinero

def conocerPuntos(matricula):
    puntos = -1
    
    if matricula in matriculasdiesel:
        posicion = matriculasdiesel.index(matricula)
        puntos = puntosdiesel[posicion]
        
    elif matricula in matriculasgasolina:
        posicion = matriculasgasolina.index(matricula)
        puntos = puntosgasolina[posicion]
    
    return puntos   

def mostrarListado():
    result =''
     
    for i in range(0, len(matriculasdiesel)):
        result = result + str(matriculasdiesel[i]) + ': ' + str(dinerodiesel[i]) + '\n'
    for j in range(0, len(matriculasgasolina)):
        result = result + str(matriculasgasolina[j]) +': ' +  str(dinerogasolina[j]) + '\n' 
 
    return result

def mostrarSurtidor():
    result = 'Surtidores\n'
    
    for i in range(0, len(surtidores)):
        result = result + str(i+1) + ': ' + str(surtidores[i]) + '\n' 
    
    return result

#principal
surtidores = [0,0,0,0]
matriculasdiesel = ['5961HBY', '4121BDV']
matriculasgasolina = ['3949JHK', '3456GDB' ]
puntosdiesel = [5, 2]
puntosgasolina =[5,7]
dinerodiesel = [50, 20]
dinerogasolina = [50, 70]
repostaje = 0
opc = 1

gasolina = float(input('Introduce el precio de la gasolina: '))
while gasolina < 1:
    print('El precio no puede ser menor que 1.')
    gasolina = float(input('Introduce el precio de la gasolina: '))
    
diesel = float(input("Introduce el precio del diesel: "))
while diesel <1:
    print('El precio no puede ser menor que 1.')
    diesel = float(input("Introduce el precio del diesel: "))

while opc != 8: 
    print(menu())
    opc = int(input("¿Qué opción deseas realizar?: "))

    if opc == 1: 
        
        cantidad = int(input('Introduce la cantidad a rellenar: '))
        while cantidad < 0: 
            cantidad = int(input('Introduce la cantidad a rellenar: '))
            
        print('Gasolina: 1 y 2\nDiesel: 3 y 4')
        tipo = int(input('¿Qué surtidor deseas llenar?: '))
        while tipo < 0 or tipo > 4:
            print('Gasolina: 1 y 2\nDiesel: 3 y 4')
            tipo = int(input('¿Qué surtidor deseas llenar?: '))
            
        surtidor = surtidores [tipo -1]
        surtidores[tipo -1] = surtidor + cantidad
        print('Surtidor' + str(tipo) + 'llenado.')
            
    elif opc == 2:
        
        combustibe = ''
        matricula = input('Introduce la matricula: ')
        while len(matricula) > 7 or len(matricula) < 0:
            matricula = input('Introduce la matricula: ')
            
        if comprobarMatricula(matricula) == True:
            combustibe = comprobarCombustible(matricula)
            if combustibe == '':
                combustibe = input('Introduce el tipo de combustible (diesel o gasolina): ')
                while combustibe.upper() != 'DIESEL' and combustibe.upper() != 'GASOLINA':
                    combustibe = input('Introduce el tipo de combustible (diesel o gasolina): ')
                
                if combustibe == 'DIESEL':
                    matriculasdiesel.append(matricula)
                elif combustibe == 'GASOLINA':
                    matriculasgasolina.append(matricula)
            
             
            repostaje = float(input('Introduce la cantidad que quieres repostar: '))
            while repostaje < 10: 
                print('El importe deber ser 10 euros mínimos.')
                repostaje = float(input('Introduce la cantidad que quieres repostar: '))
            
            surtidor = asignarSurtidor(combustibe, repostaje)
            asignarPuntos(matricula, repostaje)
            print('Ya puede repostar en el surtidor ' + str(surtidor))
        else: 
            print('La matricula no es valida.')
                        
    elif opc == 3:
        
        matricula = input('Introduce la matricula: ')
        while len(matricula) > 7 or len(matricula) < 0:
            matricula = input('Introduce la matricula: ')
            
        if comprobarMatricula(matricula) == True:
            puntos = conocerPuntos(matricula)
            print('Usted tiene ' + str(puntos) + ' acumulados.')
        
        else: 
            print('Lo sentimos, no es un cliente registrado.')
        
    elif opc == 4:
        print(mostrarListado())
    elif opc == 5:
        print(mostrarSurtidor())
    elif opc == 6:
        gasolina = float(input('Introduce el precio de la gasolina: '))
        while gasolina < 1:
            print('El precio no puede ser menor que 1.')
            gasolina = float(input('Introduce el precio de la gasolina: '))
    elif opc == 7:
        diesel = float(input("Introduce el precio del diesel: "))
        while diesel <1:
            print('El precio no puede ser menor que 1.')
            diesel = float(input("Introduce el precio del diesel: "))
    elif opc == 8:
        print('Adiós')
    else:
        print('Opción no válida.')  

#matriculasdiesel = ['5961HBY', '4121BDV']
#matriculasgasolina = ['3949JHK', '3456GDB' ]
