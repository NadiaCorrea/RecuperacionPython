"""9. Realizar un método que reciba una frase e informe de si es “chachi” o no. Se considera. 
Se considera “chachi” si las 4 primeras letras y las 4 últimas son iguales entre sí. 
Si es “chachi” devolverá true y false en caso contrario.
Si la cadena no tiene 8 caracteres no podrá ser “chachi”.
El número 4 debe crearse como constante de manera que el programa siga funcionando si se cambia el valor de dicha constante.

Ejemplo de frases “chachis”:
“Manolo juega al balonmano”
“Ponedle más marcarpone”

En el main pedir al menos una frase al usuario y decir utilizando el metodo si es “chachi” o no."""


def obtenerPrimeras(cadena):
    result = ''
    for i in range(0, 4):
        result = result + cadena[i]
    return result
    
    
def obtenerUltimas (cadena): 
    result = ''
    for i in range (len(cadena)-4, len(cadena)):
        result = result + cadena[i]    
    return result

frase = input("Introduce una frase: ")

print(obtenerPrimeras('Manolo juega al balonmano'))
print(obtenerUltimas('Manolo juega al balonmano'))
