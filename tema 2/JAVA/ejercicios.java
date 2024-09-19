
//ctividad 1: Realiza un programa Java que muestre los ficheros de un directorio. El nombre del directorio se pasará al programa desde la línea de comandos al ejecutarlo

import java.io.File;

public class ListFilesInDirectory {

    public static void main(String[] args) {
        // Verificar si se ha pasado el nombre del directorio como argumento
        if (args.length != 1) {
            System.out.println("Uso: java ListFilesInDirectory <nombre_del_directorio>");
          
        }

        // Obtener el nombre del directorio desde los argumentos
        String directoryPath = args[0];
        File directory = new File(directoryPath);

        // Verificar si el directorio existe y es un directorio
        if (!directory.exists()) {
            System.out.println("El directorio especificado no existe.");
            
        }

        if (!directory.isDirectory()) {
            System.out.println("El camino especificado no es un directorio.");
            
        }

        // Obtener la lista de archivos y subdirectorios
        String[] files = directory.list();

        // Verificar si se pudo obtener la lista de archivos
        if (files != null) {
            System.out.println("Archivos y subdirectorios en " + directoryPath + ":");
            for (String file : files) {
                System.out.println(file);
            }
        } else {
            System.out.println("No se pudo obtener la lista de archivos.");
        }
    }
}

/*Actividad 2: Crea un fichero de texto con algún editor de textos y después realiza un programa
Java que visualice su contenido. Cambia el programa Java para que el nombre del fichero se
acepte al ejecutar desde la línea de comandos
acepte al ejecutar desde la línea de comandos*/


/*Actividad 3: Crea un programa Java que reciba un identificador de empleado desde la línea de
comandos y visualice sus datos. Si el empleado no existe debe visualizar mensaje indicándolo.*/


/*Actividad 4: Crea un programa Java que reciba desde la línea de comandos un identificador
de empleado y un importe. Se debe sumar al salario del empleado el importe tecleado. El
programa debe visualizar el apellido, el salario antiguo y el nuevo. Si el identificador no existe
se visualizará un mensaje indicándolo
se visualizará un mensaje indicándolo*/


/*Actividad 5: A partir del fichero de objetos Persona utilizado anteriormente, crea un documento XML
usando DOM.*/


/*Actividad 6: Utiliza SAX para visualizar el contenido del fichero Empleados.xml creado
anteriormente.*/


/*1 Realiza un programa Java que cree un fichero binario para guardar datos de departamentos, dale
el nombre Departamentos.dat Introduce varios departamentos. Los datos por cada departamento
son;
Número de departamento: entero. Nombre: String. Localidad: String.




/*2 Realiza un programa Java que te permita modificar los datos de un departamento. El programa
recibe desde la línea de comandos el número de departamento a modificar, el nuevo nombre de
departamento y la nueva localidad. Si el departamento no existe visualiza un mensaje
indicándolo. Visualiza también los datos antiguos del departamento y los nuevos datos.



3/* Realiza un programa Java que te permita eliminar un departamento. El programa recibe desde la
línea de comandos el número de departamento a eliminar. Si el departamento no existe visualiza
un mensaje indicándolo. Visualiza también el número total de departamentos que existen en el
fichero.

4 Realiza un programa que copie dos ficheros. El nombre de los dos ficheros, origen y destino, se
introducen desde la línea de comandos al ejecutar el programa.
fichero.*/

