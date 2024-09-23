"""
1. Crea un programa en Python que pida al usuario 10 números y los guarde en una lista.
Imprime la lista.
"""


"""2. Modifica el programa anterior, de manera que al terminar de guardar los números en la lista
se impriman la lista, el sumatorio y la media de todos los número de dicha lista."""



"""3. Modifica el programa anterior de forma que la lista de 10 números sean números impares.
(hay que asegurarse de que lo que se introduce en la lista son números)."""



"""4. Adapta y amplia el programa anterior para que una vez introducidos los 10 números
impares, se muestre un menú en pantalla con 5 opciones:
¿Que desea hacer con la lista?
1. Sumatorio
2. Media
3. Máximo
4. Mínimo
0. Salir
Y después muestre el resultado de la opción seleccionada."""



"""5. Modifica el programa anterior de forma que cada una de las funcionalidades del programa se
ejecute mediante una función."""



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