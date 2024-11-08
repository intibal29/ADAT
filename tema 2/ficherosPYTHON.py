#1. Escribe una función en el lenguaje de programación Python llamada rnd_word(fitxategi1, fitxategi2) que lea el primer archivo línea por línea, seleccione una palabra aleatoria de cada línea y la escriba en el segundo archivo. Utiliza la función choice del módulo random.

import random

def rnd_word(fitxategi1, fitxategi2):
    with open(fitxategi1, 'r') as infile, open(fitxategi2, 'w') as outfile:
        for line in infile:
            words = line.split()
            if words:  # Verificar que la línea no esté vacía
                random_word = random.choice(words)
                outfile.write(random_word + '\n')

# Ejemplo de uso:
# rnd_word('archivo_entrada.txt', 'archivo_salida.txt')

#--------------------------------------------------------------------------------------------------



#Escribe una función en el lenguaje de programación Python que reciba una oración, elija dos palabras aleatorias de ella y forme una nueva palabra usando esas dos palabras. Para crear la nueva palabra, los caracteres se seleccionarán aleatoriamente de cada una de las dos palabras, uno por uno. Ejemplo: si palabra1 = 'casa' y palabra2 = 'voy', el primer carácter de la nueva palabra se elegirá aleatoriamente entre los caracteres de 'c' y 'v'. Supongamos que se elige 'v', entonces el siguiente carácter se elegirá aleatoriamente entre 'c' y 'o'. Repetiendo este procedimiento con todos los caracteres, el resultado podría ser una palabra como 'vcaoysa’

import random

def combine_randomly(oracion):
    # Dividir la oración en palabras
    palabras = oracion.split()
    
    # Verificar que haya al menos dos palabras
    if len(palabras) < 2:
        raise ValueError("La oración debe contener al menos dos palabras.")
    
    # Elegir dos palabras aleatorias
    palabra1, palabra2 = random.sample(palabras, 2)
    
    nueva_palabra = []
    
    # Determinar la longitud máxima de las dos palabras
    max_len = max(len(palabra1), len(palabra2))
    
    for i in range(max_len):
        if i < len(palabra1):
            nueva_palabra.append(random.choice(palabra1))
        if i < len(palabra2):
            nueva_palabra.append(random.choice(palabra2))
    
    return ''.join(nueva_palabra)

# Ejemplo de uso:
oracion = "casa voy perro"
print(combine_randomly(oracion))


#--------------------------------------------------------------------------------------------------------------
     
#Escribe un programa en el lenguaje de programación Python que genere una lista de 1000 números reales pseudo-aleatorios en el rango de -100 a 100 y la guarde en un archivo usando el módulo pickle. Luego, escribe un segundo programa que cargue estos dos archivos (usando pickle nuevamente) y calcule el promedio de las diferencias entre los valores en la misma posición en ambas listas

import pickle
import random

# Generar una lista de 1000 números reales pseudo-aleatorios en el rango de -100 a 100
def generar_lista(n, rango_min, rango_max):
    return [random.uniform(rango_min, rango_max) for _ in range(n)]

# Guardar la lista en un archivo usando pickle
def guardar_lista_en_archivo(lista, archivo):
    with open(archivo, 'wb') as f:
        pickle.dump(lista, f)

# Parámetros
numero_elementos = 1000
rango_min = -100
rango_max = 100
archivo = 'lista_pseudoaleatoria.pkl'

# Generar la lista y guardarla
lista = generar_lista(numero_elementos, rango_min, rango_max)
guardar_lista_en_archivo(lista, archivo)

print(f'Lista guardada en {archivo}')

#-------------------------------------------------------
# Escribe un programa en el lenguaje de programación Python que cree una base de datos de libros para una librería. El programa deberá solicitar el nombre del libro, el autor, el precio del libro, el precio después de un descuento y el número de páginas del libro. Una vez que se haya ingresado la información, el programa preguntará si deseas ingresar información sobre otro libro. Si no quieres ingresar más libros, el programa finalizará; de lo contrario, continuará solicitando datos. Toda la información ingresada se guardará en un archivo de texto utilizando la función repr(). Luego, escribe un segundo programa que lea el archivo con la base de datos de libros y muestre en pantalla el nombre del libro con el mayor descuento (en porcentaje) y el porcentaje de descuento.

def save_book_to_file(book_data, filename="books_database.txt"):
    with open(filename, "a") as file:
        file.write(f"{book_data}\n")

def main():
    while True:
        print("Ingrese la información del libro:")

        name = input("Nombre del libro: ")
        author = input("Autor del libro: ")
        price = float(input("Precio del libro: "))
        discounted_price = float(input("Precio después del descuento: "))
        pages = int(input("Número de páginas del libro: "))

        # Calcular el porcentaje de descuento
        discount_percentage = 0
        if price > 0:
            discount_percentage = ((price - discounted_price) / price) * 100

        # Crear una cadena con la información del libro
        book_data = f"Nombre: {name}, Autor: {author}, Precio: {price}, Precio con descuento: {discounted_price}, Páginas: {pages}, Descuento: {discount_percentage:.2f}%"

        # Guardar en el archivo
        save_book_to_file(book_data)

        # Preguntar si desea ingresar otro libro
        another = input("¿Desea ingresar otro libro? (sí/no): ").strip().lower()
        if another != 'sí':
            break

if __name__ == "__main__":
    main()





#-------------------------------------------------

def read_books_from_file(filename="books_database.txt"):
    books = []
    try:
        with open(filename, "r") as file:
            for line in file:
                books.append(line.strip())
    except FileNotFoundError:
        print("No se encontró el archivo de base de datos.")
    return books

def extract_discount(book_data):
    # Extraer el porcentaje de descuento de la cadena
    parts = book_data.split(", ")
    for part in parts:
        if part.startswith("Descuento:"):
            return float(part.split(": ")[1].replace('%', ''))
    return 0

def main():
    books = read_books_from_file()

    if not books:
        print("No se encontraron libros en la base de datos.")
        return

    # Encontrar el libro con el mayor descuento
    max_discount_book = max(books, key=extract_discount)

    print(f"El libro con el mayor descuento es:")
    print(max_discount_book)

if __name__ == "__main__":
    main()
