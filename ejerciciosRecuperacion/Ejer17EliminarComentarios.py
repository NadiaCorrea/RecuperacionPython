"""17.- El preprocesador del lenguaje C, elimina los comentarios (/* ….*/) 
del código fuente antes de compilar. Diseñar un método que reciba una sentencia en C 
y devuelva una cadena eliminando los comentarios."""

def eliminarComenatrio(cadena):
    result = ''
    
    for i in cadena:
        if ord(i) != 47 and ord(i) != 42:
            result = result + i 
    
    return result

comentario = input("Introduce el comentario: ")
print(eliminarComenatrio(comentario))