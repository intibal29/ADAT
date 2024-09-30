
//ctividad 1: Realiza un programa Java que muestre los ficheros de un directorio. El nombre del directorio se pasará al programa desde la línea de comandos al ejecutarlo

import java.io.File;

public class ListFilesInDirectory {

    public static void main(String[] args) {
        // Verificar si se ha pasado el nombre del directorio como argumento
        if (args.length != 1) {
            System.out.println("Uso: java ListFilesInDirectory <nombre_del_directorio>");
          
        }

        // Obtener el nombre del directorio desde los argumentos
<<<<<<< HEAD
        String directoryPath = args[0];
        File directory = new File(directoryPath);
=======
        String path = args[0];
        File directory = new File(path);
>>>>>>> 1664f00 (1)

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
<<<<<<< HEAD
            System.out.println("Archivos y subdirectorios en " + directoryPath + ":");
=======
            System.out.println("Archivos y subdirectorios en " + path + ":");
>>>>>>> 1664f00 (1)
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

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadFile {

    public static void main(String[] args) {
        // Verificar si se ha pasado el nombre del archivo como argumento
        if (args.length != 1) {
            System.out.println("Uso: java ReadFile <nombre_del_archivo>");
        }

        // Obtener el nombre del archivo desde los argumentos
        String fileName = args[0];

        // Intentar leer el contenido del archivo
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            // Leer el archivo línea por línea
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("Error al leer el archivo: " + e.getMessage());
        }
    }
}


/*Actividad 3: Crea un programa Java que reciba un identificador de empleado desde la línea de
comandos y visualice sus datos. Si el empleado no existe debe visualizar mensaje indicándolo.*/
<<<<<<< HEAD
import java.util.HashMap;
import java.util.Map;

public class EmployeeLookup {

    // Simulación de una "base de datos" de empleados usando un HashMap
    private static final Map<String, String> employees = new HashMap<>();

    static {
        // Inicializar algunos datos de empleados para la demostración
        employees.put("E001", "Juan Pérez, Developer, IT");
        employees.put("E002", "Ana Gómez, Analyst, Marketing");
        employees.put("E003", "Luis Fernández, Manager, HR");
=======


import java.util.HashMap;
import java.util.Map;

public class Empleados {

    // Simulación de una "base de datos" de empleados usando un HashMap
    private static final Map<String, String> empleados = new HashMap<>();

    static {
        // Inicializar algunos datos de empleados para la demostración
        empleados.put("E001", "Juan Pérez, Desarrollador, IT");
        empleados.put("E002", "Ana Gómez, Analista, Marketing");
        empleados.put("E003", "Luis Fernández, Gerente, RRHH");
>>>>>>> 1664f00 (1)
    }

    public static void main(String[] args) {
        // Verificar si se ha pasado el identificador del empleado como argumento
        if (args.length != 1) {
            System.out.println("Uso: <identificador_del_empleado>");
<<<<<<< HEAD
            
        }

        // Obtener el identificador del empleado desde los argumentos
        String employeeId = args[0];

        // Buscar y mostrar los datos del empleado
        String employeeData = employees.get(employeeId);

        if (employeeData != null) {
            System.out.println("Datos del empleado con ID " + employeeId + ": " + employeeData);
        } else {
            System.out.println("Empleado con ID " + employeeId + " no existe.");
=======
            System.exit(1);  // Terminar el programa si no se proporciona el ID correcto
        }

        // Obtener el identificador del empleado desde los argumentos
        String identificadorEmpleado = args[0];

        // Buscar y mostrar los datos del empleado
        String datosEmpleado = empleados.get(identificadorEmpleado);

        if (datosEmpleado != null) {
            System.out.println("Datos del empleado con ID " + identificadorEmpleado + ": " + datosEmpleado);
        } else {
            System.out.println("Empleado con ID " + identificadorEmpleado + " no existe.");
>>>>>>> 1664f00 (1)
        }
    }
}



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

