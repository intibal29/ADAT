"""
1. Crea un programa en Python que pida al usuario 10 números y los guarde en una lista.
Imprime la lista.
"""
<<<<<<< HEAD
=======
# Crear una lista 
numeros = []

for i in range(10):
    numero = float(input(f"Introduce el número {i+1}: "))
    numeros.append(numero)  # Añadir el número a la lista

# Imprimir la lista de números
print("Los números que introdujiste son:", numeros)
>>>>>>> 1664f00 (1)


"""2. Modifica el programa anterior, de manera que al terminar de guardar los números en la lista
se impriman la lista, el sumatorio y la media de todos los número de dicha lista."""


<<<<<<< HEAD
=======
numeros = []  # Lista vacía para almacenar los números
sumatorio = 0  

for i in range(10):
    numero = float(input(f"Introduce el número {i+1}: "))  
    numeros.append(numero)  # Añadir el número a la lista
    sumatorio += numero  # Sumar el número al sumatorio

# Calcular la media
media = sumatorio / 10

print("Los números que introdujiste son:", numeros)
print("El sumatorio es:", sumatorio)
print("La media es:", media)


>>>>>>> 1664f00 (1)

"""3. Modifica el programa anterior de forma que la lista de 10 números sean números impares.
(hay que asegurarse de que lo que se introduce en la lista son números)."""


<<<<<<< HEAD
=======
numeros = [] 
sumatorio = 0  

# Función para verificar si un número es impar
def es_impar(numero):
    return numero % 2 != 0  


i = 0
while i < 10:
    try:
        numero = int(input(f"Introduce el número impar {i+1}: "))
        
        # Verificar si el número es impar
        if es_impar(numero):
            numeros.append(numero)  # Añadir el número a la lista
            sumatorio += numero  
            i += 1 
        else:
            print("Por favor, introduce un número impar.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")


media = sumatorio / 10

print("Los números impares que introdujiste son:", numeros)
print("El sumatorio es:", sumatorio)
print("La media es:", media)

>>>>>>> 1664f00 (1)

"""4. Adapta y amplia el programa anterior para que una vez introducidos los 10 números
impares, se muestre un menú en pantalla con 5 opciones:
¿Que desea hacer con la lista?
1. Sumatorio
2. Media
3. Máximo
4. Mínimo
0. Salir
Y después muestre el resultado de la opción seleccionada."""


<<<<<<< HEAD
=======
def es_impar(numero):
    return numero % 2 != 0  # Devuelve True si el número es impar

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\n¿Qué desea hacer con la lista?")
    print("1. Sumatorio")
    print("2. Media")
    print("3. Máximo")
    print("4. Mínimo")
    print("0. Salir")

# Función principal
def main():
    numeros = [] 
    sumatorio = 0 

    i = 0
    while i < 10:
        try:
            numero = int(input(f"Introduce el número impar {i+1}: ")) 

            if es_impar(numero):
                numeros.append(numero) 
                sumatorio += numero  
                i += 1  
            else:
                print("Por favor, introduce un número impar.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

    media = sumatorio / 10
    maximo = max(numeros)  
    minimo = min(numeros)  

    # Menú de opciones
    while True:
        mostrar_menu()  # Mostrar el menú
        opcion = input("Selecciona una opción: ")

        if opcion == '1': 
            print(f"El sumatorio de los números es: {sumatorio}")
        elif opcion == '2': 
            print(f"La media de los números es: {media}")
        elif opcion == '3':  
            print(f"El número máximo es: {maximo}")
        elif opcion == '4':  
            print(f"El número mínimo es: {minimo}")
        elif opcion == '0':  # Opción 0: Salir
            print("Saliendo del programa.")
            break  # Salir del bucle y terminar el programa
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")

# Ejecutar el programa
if __name__ == "__main__":
    main()

>>>>>>> 1664f00 (1)

"""5. Modifica el programa anterior de forma que cada una de las funcionalidades del programa se
ejecute mediante una función."""

<<<<<<< HEAD
=======
# Función para verificar si un número es impar
def es_impar(numero):
    """Devuelve True si el número es impar."""
    return numero % 2 != 0

# Función para pedir 10 números impares al usuario
def solicitar_numeros():
    """Solicita al usuario 10 números impares y los devuelve en una lista."""
    numeros = []
    i = 0
    while i < 10:
        try:
            numero = int(input(f"Introduce el número impar {i+1}: "))
            if es_impar(numero):
                numeros.append(numero)
                i += 1
            else:
                print("Por favor, introduce un número impar.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")
    return numeros

# Función para calcular el sumatorio de los números
def calcular_sumatorio(numeros):
    """Devuelve el sumatorio de una lista de números."""
    return sum(numeros)

# Función para calcular la media de los números
def calcular_media(numeros):
    """Devuelve la media de una lista de números."""
    return sum(numeros) / len(numeros)

# Función para encontrar el máximo de los números
def encontrar_maximo(numeros):
    """Devuelve el número máximo de una lista."""
    return max(numeros)

# Función para encontrar el mínimo de los números
def encontrar_minimo(numeros):
    """Devuelve el número mínimo de una lista."""
    return min(numeros)

# Función para mostrar el menú de opciones
def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n¿Qué desea hacer con la lista?")
    print("1. Sumatorio")
    print("2. Media")
    print("3. Máximo")
    print("4. Mínimo")
    print("0. Salir")

# Función principal del programa
def main():
    numeros = solicitar_numeros()  
    while True:
        mostrar_menu() 
        opcion = input("Selecciona una opción: ")

        if opcion == '1': 
            sumatorio = calcular_sumatorio(numeros)
            print(f"El sumatorio de los números es: {sumatorio}")
        elif opcion == '2':  
            media = calcular_media(numeros)
            print(f"La media de los números es: {media}")
        elif opcion == '3': 
            maximo = encontrar_maximo(numeros)
            print(f"El número máximo es: {maximo}")
        elif opcion == '4': 
            minimo = encontrar_minimo(numeros)
            print(f"El número mínimo es: {minimo}")
        elif opcion == '0': 
            print("Saliendo del programa.")
            break  
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
>>>>>>> 1664f00 (1)


"""6. Crea una clase Criptográfo que contenga dos métodos: encriptar y desencriptar. Los dos
métodos recibirán un texto y devolverán otro texto. El funcionamiento de los métodos es el
siguiente:
◦ encriptar(txt): El texto recibido se encriptará sustituyendo cada uno de los
caracteres por el siguiente caracter según su valor ASCII.
◦ desencriptar(txt): Realizará la acción inversa al metodo anterior, es decir sustituirá
cada carácter por el anterior según su valor ASCII.
Nota: Para realizar este ejercicio son muy útiles las funciones ord() y chr()."""



"""7. Haz una clase llamada Persona que siga las siguientes condiciones:
 Sus atributos son: nombre, edad, DNI, sexo (H hombre, M mujer), peso y altura.
No queremos que se accedan directamente a ellos. Si quieres añadir algún atributo
puedes hacerlo.
 Por defecto, todos los atributos menos el DNI serán valores por defecto según su tipo
(0 números, cadena vacía para String, etc.). Sexo sera hombre por defecto, usa una
constante para ello.
 Los métodos que se implementaran son:
 calcularIMC(): calculara si la persona esta en su peso ideal (peso en
kg/(altura^2 en m)), si esta fórmula devuelve un valor menor que 20, la
función devuelve un -1, si devuelve un número entre 20 y 25 (incluidos),
significa que esta por debajo de su peso ideal la función devuelve un 0 y si
devuelve un valor mayor que 25 significa que tiene sobrepeso, la función
devuelve un 1. Te recomiendo que uses constantes para devolver estos
valores.
 esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.
 toString(): devuelve toda la información del objeto.
 generaDNI(): genera un número aleatorio de 8 cifras, genera a partir de este
su número su letra correspondiente. Este método sera invocado cuando se
construya el objeto. Puedes dividir el método para que te sea más fácil. No
será visible al exterior.
 Métodos set de cada parámetro, excepto de DNI."""



"""8. Ahora, crea un programa ejecutable que haga lo siguiente:
◦ Crea 3 objetos de la clase anterior.
◦ Para cada objeto, deberá comprobar si esta en su peso ideal, tiene sobrepeso o por debajo
de su peso ideal con un mensaje.
◦ Indicar para cada objeto si es mayor de edad.
◦ Por último, mostrar la información de cada objeto. _"""