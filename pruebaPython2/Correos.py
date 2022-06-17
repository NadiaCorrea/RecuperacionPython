"""3. Un oficial de correos decide optimizar el trabajo de su oficina cortando todas las palabras 
de más de cinco letras a sólo cinco letras 
(e indicando que una palabra fue cortada con el agregado de una arroba). 
Además también elimina todos los espacios en blanco de más.
Por ejemplo, al texto » Llego mañana alrededor del mediodía » 
se transcribe como «Llego mañan@ alred@ del medio@». 
Por otro lado cobra un valor para las palabras cortas y 
otro valor para las palabras largas (que deben ser cortadas). 

Escribir una función que reciba un texto, la longitud máxima de las palabras 
(en el caso anterior eran 5 letras) y devuelva como resultado el texto del telegrama.
 
Extra: Escribir una segunda función que devuelva el costo del texto. 
Esta función deberá recibir como argumento el costo de cada palabra corta, 
el costo de cada palabra larga y el texto del telegrama, es decir, el texto ya cifrado. """

def eliminarEspacio(texto, longitud):
    result = ''
    palabra = ''
    palabraCortada = ''
    
    for i in texto: 
        
        if ord(i) == 32: 
            if len(palabra) >= 1:
                
                if len(palabra) > longitud: 
                    palabra = cortarPalabra(palabra, longitud)
                    result = result + palabra + ' '
                    palabra = ''
                
                else: 
                    result = result + palabra + ' '
                    palabra = ''
                
        else:
            palabra = palabra + i
        
        
    result = result[0:len(result)-1]
    return result
    

def cortarPalabra(palabra, longitud):
    palabraCortada = ''
    result = ''    
    
    if len(palabra) > longitud: 
        for j in range (0,longitud):
            palabraCortada = palabraCortada + palabra[j]
        
        result = palabraCortada + '@'
    
    return result

"""Extra: Escribir una segunda función que devuelva el costo del texto. 
Esta función deberá recibir como argumento el costo de cada palabra corta, 
el costo de cada palabra larga y el texto del telegrama, es decir, el texto ya cifrado."""

def costoTexto(corta, larga, cifrado):
    totalCorta = 0
    totalLarga = 0
    ultimo = ''
    resultado = 0
    
    for i in cifrado: 
        if ord(i) != 32: 
            ultimo = i
            
        else:
            if ord(ultimo) == 64:
                totalLarga = totalLarga + larga
            else:
                totalCorta = totalCorta + corta 
             
    if ord(ultimo) == 64:
        totalLarga = totalLarga + larga
    else:
        totalCorta = totalCorta + corta 
    
    
    resultado = totalCorta + totalLarga
    return resultado  


frase = input("Introduce la frase a enviar: ")
longitud = int(input("Introduce el número de caracteres de las palabras largas: "))
cortas = int(input("Introduce el precio de las palabras cortas: "))
largas = int(input("Introduce el precio de las palabras largas: "))

cifrado = eliminarEspacio(frase, longitud)
costo = costoTexto(cortas, largas, cifrado)

print('El texto a enviar es: ' + cifrado)
print('El precio total es: ' + str(costo))



