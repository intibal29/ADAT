# Escribe un programa que pase números decimales a binarios.
def decimal_binario(decimal):
    if decimal >=0:
        return bin(decimal)[2:]# para eliminar ob
    else:
        return "-" + bin(decimal) [3:] # para manejarnumeros negativos
    
    decimal = int(input("introduce unnumero decimal"))
    print(f"elnumero {decimal} en binarioes {decimal_binario(decimal)}")


#Escribe un programa que añada espacios antes de la palabra, el número de espacios deberá ser el doble del tamaño de la palabra.


def añadir_espacios(palabra):
    espacios=" "*(2*len(palabra))
    return espacios + palabra 



#Escribe un programa que devuelva True cuando una palabra no contenga ‘a’ y false en caso contrario.

def no_a(palabra):
    for  letra in palabra:
        if letra == 'a' or letra == 'A':
            return False
        else 
        return True
    

#Escribe un programa que pida por pantalla un texto y calcule el porcentaje de palabras que no tienen a.
def calcular_porcentaje_sin_a(texto):
    # Dividir el texto en palabras
    palabras = texto.split()
    
    # Contar el número total de palabras
    total_palabras = len(palabras)
    
    # Contar las palabras que no contienen la letra 'a'
    palabras_sin_a = sum(1 for palabra in palabras if 'a' not in palabra.lower())
    
    # Calcular el porcentaje
    if total_palabras > 0:
        porcentaje = (palabras_sin_a / total_palabras) * 100
    else:
        porcentaje = 0
    
    return porcentaje

# Solicitar un texto al usuario
texto_usuario = input("Introduce un texto: ")

# Calcular el porcentaje de palabras sin 'a'
porcentaje_sin_a = calcular_porcentaje_sin_a(texto_usuario)

# Mostrar el resultado
print(f"El porcentaje de palabras que no contienen la letra 'a' es: {porcentaje_sin_a:.2f}%")

------------------------------------------------------------------------------------------------ 

#Escribe un programa que busque el índice de una letra en una palabra y si no contiene la letra devuelva -1. (sin utilizar la función find y utilizando la función find)
def buscar_indice_con_find(palabra, letra):
    # Utiliza el método find para buscar el índice de la letra
    return palabra.find(letra)

# Solicitar entrada del usuario
palabra = input("Introduce una palabra: ")
letra = input("Introduce la letra a buscar: ")

# Buscar el índice de la letra
indice = buscar_indice_con_find(palabra, letra)

# Mostrar el resultado
print(f"El índice de la letra '{letra}' en la palabra '{palabra}' es: {indice}")
--------------------------------------------------------------------------------------------


#Crea una función que recorra un diccionario y busque si un elemento se encuentra en el mismo.

#Crea un diccionario que contenga los caracteres ascii y su correspondiente valor numérico