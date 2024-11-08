import java.sql.*;
import java.util.Scanner;

public class OlimpicosApp {

    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        while (true) {
            System.out.println("\nMenú:");
            System.out.println("1. Crear BBDD MySQL");
            System.out.println("2. Listar deportistas en diferentes deportes");
            System.out.println("3. Modificar medalla deportista");
            System.out.println("0. Salir");
            System.out.print("Selecciona una opción: ");
            
            int opcion = scanner.nextInt();
            scanner.nextLine(); // Consumir salto de línea

            switch (opcion) {
                case 1:
                    crearBBDDMySQL();
                    break;
                case 2:
                    listarDeportistasDiferentesDeportes();
                    break;
                case 3:
                    modificarMedallaDeportista();
                    break;
                case 0:
                    System.out.println("¡Hasta luego!");
                    return;
                default:
                    System.out.println("Opción no válida.");
            }
        }
    }

    // Función para crear la base de datos y cargar los datos desde un CSV
    public static void crearBBDDMySQL() {
        System.out.println("Creando la BBDD y cargando datos...");
        try (Connection conn = DBConnection.connect()) {
            Statement stmt = conn.createStatement();
            
            // Crear tablas (si no existen)
            String createAtletas = "CREATE TABLE IF NOT EXISTS atletas (" +
                                   "id INT AUTO_INCREMENT PRIMARY KEY, " +
                                   "nombre VARCHAR(100), " +
                                   "sexo CHAR(1), " +
                                   "altura DECIMAL(5,2), " +
                                   "peso DECIMAL(5,2))";
            stmt.executeUpdate(createAtletas);

            String createParticipaciones = "CREATE TABLE IF NOT EXISTS participaciones (" +
                                           "id INT AUTO_INCREMENT PRIMARY KEY, " +
                                           "atleta_id INT, " +
                                           "temporada CHAR(1), " +
                                           "edicion_olimpica INT, " +
                                           "deporte VARCHAR(100), " +
                                           "evento VARCHAR(100), " +
                                           "medalla VARCHAR(50), " +
                                           "FOREIGN KEY (atleta_id) REFERENCES atletas(id))";
            stmt.executeUpdate(createParticipaciones);

            System.out.println("Estructura de la BBDD creada correctamente.");
        } catch (SQLException e) {
            System.err.println("Error al crear la base de datos: " + e.getMessage());
        }
    }

    // Función para listar los deportistas que han participado en diferentes deportes
    public static void listarDeportistasDiferentesDeportes() {
        try (Connection conn = DBConnection.connect()) {
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(
                "SELECT a.nombre, a.sexo, a.altura, a.peso, p.deporte, p.edicion_olimpica, p.evento, p.medalla " +
                "FROM atletas a " +
                "JOIN participaciones p ON a.id = p.atleta_id " +
                "GROUP BY a.id " +
                "HAVING COUNT(DISTINCT p.deporte) > 1");

            while (rs.next()) {
                System.out.println("Nombre: " + rs.getString("nombre"));
                System.out.println("Sexo: " + rs.getString("sexo"));
                System.out.println("Altura: " + rs.getDouble("altura"));
                System.out.println("Peso: " + rs.getDouble("peso"));
                System.out.println("Deporte: " + rs.getString("deporte"));
                System.out.println("Edición olímpica: " + rs.getInt("edicion_olimpica"));
                System.out.println("Evento: " + rs.getString("evento"));
                System.out.println("Medalla: " + rs.getString("medalla"));
                System.out.println("---------------------------------------------------");
            }
        } catch (SQLException e) {
            System.err.println("Error al listar deportistas: " + e.getMessage());
        }
    }

    // Función para modificar la medalla de un deportista
    public static void modificarMedallaDeportista() {
        System.out.print("Introduce el ID del deportista: ");
        int atletaId = scanner.nextInt();
        scanner.nextLine(); // Consumir salto de línea

        System.out.print("Introduce el ID de la participación a modificar: ");
        int participacionId = scanner.nextInt();
        scanner.nextLine(); // Consumir salto de línea

        System.out.print("Introduce la nueva medalla (Oro, Plata, Bronce, Ninguna): ");
        String nuevaMedalla = scanner.nextLine();

        try (Connection conn = DBConnection.connect()) {
            String query = "UPDATE participaciones SET medalla = ? WHERE id = ?";
            try (PreparedStatement stmt = conn.prepareStatement(query)) {
                stmt.setString(1, nuevaMedalla);
                stmt.setInt(2, participacionId);
                int rowsAffected = stmt.executeUpdate();

                if (rowsAffected > 0) {
                    System.out.println("Medalla actualizada correctamente.");
                } else {
                    System.out.println("No se encontró la participación.");
                }
            }
        } catch (SQLException e) {
            System.err.println("Error al modificar la medalla: " + e.getMessage());
        }
    }
}
