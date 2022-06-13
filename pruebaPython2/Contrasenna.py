"""1. Crear función que reciba una cadena como parámetro 
y que devuelva si es una contraseña FUERTE (True) o DÉBIL (False). 
Se considera que una contraseña es fuerte si contiene 8 o más caracteres, 
y entre ellos al menos hay una mayúscula, una minúscula y un dígito."""

def buscarMayuscula(caracter):
    mayu = False
    if ord(caracter) >= 65 and ord(caracter)<= 90: 
        mayu = True    
    return mayu
    
def buscarDigito(caracter):
    digito = False
    if ord(caracter)>= 48 and ord(caracter)>= 57: 
        digito = True
    return digito
    
def buscarMinuscula(caracter):
    minu = False
    if ord(caracter) >= 97 and ord(caracter) <= 122: 
        minu = True
    return minu

def contrasennaTipo(contrasenna):
    result = False
    totalMayusculas = 0 
    totalMinusculas = 0 
    totalNumeros = 0
    
    if len(contrasenna) >= 8:
        for i in contrasenna:
            if buscarMayuscula(i) == True:
                totalMayusculas = totalMayusculas + 1
            elif buscarMinuscula(i) == True:
                totalMinusculas = totalMinusculas + 1
            elif buscarDigito(i) == True:
                totalNumeros = totalNumeros + 1

            if totalMayusculas >= 1 and totalMinusculas >= 1 and totalNumeros >= 1:
                result = True
    return result    


clave = input("Introduce la contraseña: ")

resultado = contrasennaTipo(clave)

if resultado == True:
    print('La contraseña es Fuerte.')
else:
    print('La contraseña es Débil.')


