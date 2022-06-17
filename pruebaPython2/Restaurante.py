"""Un restaurante te ha encargado una aplicación para colocar a los clientes en sus mesas. 
En una mesa se pueden sentar de 0 (mesa vacía) a 4 comensales (mesa llena). 
Cuando llega un cliente se le pregunta cuántos son 
(dando un mensaje de error si el número de clientes es superior a 4). 
Para el grupo que llega, se busca siempre la primera mesa libre (con 0 personas). 
Si no quedan mesas libres, se busca donde haya un hueco para todo el grupo, 
por ejemplo si el grupo es de dos personas, se podrá colocar donde haya una 
o dos personas. 
Cada vez que se sientan nuevos clientes se debe mostrar la mesa en la que se sientan 
y el estado de las mesas (Libre u ocupada con x comensales). 
Si no hay sitio se deberá mostrar el mensaje “Restaurante completo” 
y el estado de las mesas 
Los grupos no se pueden romper aunque haya huecos sueltos suficientes. 
El programa terminará cuando se quiera sentar a -1 comensal. 
En nuestro restaurante habrá 10 mesas, pero deja preparado el programa para 
que se pueda ampliar fácilmente el número de mesas. """

TOTALMESAS = 3
mesas = []
mesaAsignada = -1
# CREO EL ARRAY CON EL TOTAL DE LAS MESAS 
for i in range (0,TOTALMESAS):
    mesas.append(0)
    
#PARA SABER SI HAY MESAS LIBRES EN EL ARRAY
def mesasLibres(mesas):
    result = -1
    i = 0 
    while i < len(mesas) and result == -1:
        if mesas[i] == 0: 
            result = i
        i = i + 1
    return result 

def mesasComensales(mesas):
    result = ''
    
    for i in range(0, len(mesas)):
        result = result + ' Mesa ' + str(i + 1) + ': ' + str(mesas[i]) + ' comensales.\n' 
    return result

comensales = 0

while comensales != -1:
    comensales = int(input("Introduce el número de comensales: "))
    
    if comensales == -1: 
        print('Adios')
    elif comensales > 4: 
        print('Error. El número de comensales tiene que ser menor o igual a 4.')
    else:
        
        libre = mesasLibres(mesas)
        if libre != -1: 
            mesas[libre] = comensales
            mesaAsignada = libre
        else:     
            disponible = False   
            j = 0
            while j < len(mesas) and disponible == False:
                if mesas[j] + comensales <= 4:
                    mesas[j] = mesas[j] + comensales
                    disponible = True
                    mesaAsignada = j
                j = j + 1 
            
            if disponible == False:
                mesaAsignada = -1
                
        if mesaAsignada == -1: 
            print('Restaurante completo.')
            comensales = -1
        else:    
            print('Mesa asignada: ' + str(mesaAsignada + 1))
            print('Listado de mesas y comensales:\n' + str(mesasComensales(mesas)))
            
            
            
            