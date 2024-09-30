# Función para ajustar la clave a la longitud del texto en claro
def ajustar_clave(texto, clave):
    """
    Ajusta la longitud de la clave al tamaño del texto.
    Si la clave es más corta, se repite hasta que coincida con la longitud del texto.
    """
    clave = clave.upper()  # Convertimos la clave a mayúsculas
    texto = texto.upper()  # Convertimos el texto a mayúsculas
    clave_ajustada = clave
    while len(clave_ajustada) < len(texto):  # Si la clave es más corta, la repetimos
        clave_ajustada += clave
    return clave_ajustada[:len(texto)]  # Devolvemos la clave ajustada al tamaño del texto

# Función para cifrar utilizando el cifrado de Vigenère
def cifrar_vigenere(texto, clave):
    """
    Cifra un texto utilizando el algoritmo de Vigenère.
    Cada letra del texto se cifra sumando su posición con la de la clave ajustada.
    """
    texto = texto.upper()  # Convertimos el texto a mayúsculas
    clave_ajustada = ajustar_clave(texto, clave)  # Ajustamos la clave al tamaño del texto
    texto_cifrado = ""
    
    for i in range(len(texto)):
        if texto[i].isalpha():  # Verificamos que sea una letra (omitimos espacios y signos)
            # Convertimos las letras a posiciones (A = 0, B = 1, ..., Z = 25)
            valor_texto = ord(texto[i]) - ord('A')
            valor_clave = ord(clave_ajustada[i]) - ord('A')
            # Ciframos sumando las posiciones y ajustando con módulo 26
            valor_cifrado = (valor_texto + valor_clave) % 26
            # Convertimos de nuevo a letra y agregamos al texto cifrado
            texto_cifrado += chr(valor_cifrado + ord('A'))
        else:
            texto_cifrado += texto[i]  # Si no es una letra, se mantiene igual

    return texto_cifrado

# Función para descifrar utilizando el cifrado de Vigenère
def descifrar_vigenere(texto_cifrado, clave):
    """
    Descifra un texto cifrado utilizando el algoritmo de Vigenère.
    Cada letra del texto cifrado se descifra restando la posición de la clave ajustada.
    """
    texto_cifrado = texto_cifrado.upper()  # Convertimos el texto a mayúsculas
    clave_ajustada = ajustar_clave(texto_cifrado, clave)  # Ajustamos la clave
    texto_descifrado = ""
    
    for i in range(len(texto_cifrado)):
        if texto_cifrado[i].isalpha():  # Verificamos que sea una letra
            # Convertimos las letras a posiciones (A = 0, B = 1, ..., Z = 25)
            valor_cifrado = ord(texto_cifrado[i]) - ord('A')
            valor_clave = ord(clave_ajustada[i]) - ord('A')
            # Desciframos restando las posiciones y ajustando con módulo 26
            valor_descifrado = (valor_cifrado - valor_clave) % 26
            # Convertimos de nuevo a letra y agregamos al texto descifrado
            texto_descifrado += chr(valor_descifrado + ord('A'))
        else:
            texto_descifrado += texto_cifrado[i]  # Si no es una letra, se mantiene igual

    return texto_descifrado

# Función para escribir en un fichero
def escribir_fichero(nombre_fichero, contenido):
    """
    Escribe el contenido en un fichero.
    """
    with open(nombre_fichero, "w") as fichero:
        fichero.write(contenido)

# Función para leer desde un fichero
def leer_fichero(nombre_fichero):
    """
    Lee el contenido de un fichero.
    """
    with open(nombre_fichero, "r") as fichero:
        return fichero.read()

# Prueba del cifrado y descifrado
if __name__ == "__main__":
    # Texto en claro y clave
    texto_claro = "ATAQUE AL AMANECER"
    clave = "CLAVE"
    
    # Cifrar el texto
    texto_cifrado = cifrar_vigenere(texto_claro, clave)
    print(f"Texto cifrado: {texto_cifrado}")
    
    # Guardar el texto cifrado en un fichero
    escribir_fichero("texto_cifrado.txt", texto_cifrado)
    
    # Leer el texto cifrado desde el fichero
    texto_leido = leer_fichero("texto_cifrado.txt")
    print(f"Texto cifrado leído del fichero: {texto_leido}")
    
    # Descifrar el texto
    texto_descifrado = descifrar_vigenere(texto_leido, clave)
    print(f"Texto descifrado: {texto_descifrado}")
    
    # Guardar el texto descifrado en un fichero
    escribir_fichero("texto_descifrado.txt", texto_descifrado)
