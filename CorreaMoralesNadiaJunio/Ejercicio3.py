"""EJERCICIO 3
Realizar una funcion que reciba como parametro una cadena y dos caracteres 
y devuelva la cadena inicial pero sustituyendo en ella 
el primer caracter por el segundo. 
NO se pueden usar las funciones de cadena de python"""


def sustituirCaracteres(cadena, car1, car2):
    result = ''
    
    for i in cadena:
        if i == car1:
            i = car2
            result = result + i
        else: 
            result = result + i
    
    return result

print(sustituirCaracteres('maria', 'a', 'o'))