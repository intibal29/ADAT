import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.security.SecureRandom;

public class AESFileEncryption {

    // Tamaño del bloque para AES (en bytes)
    private static final int BLOCK_SIZE = 16;  // AES usa bloques de 16 bytes 

    // Método para generar una clave secreta AES
    private static SecretKey generarClaveAES() throws Exception {
        // Generador de claves AES
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128);  // AES de 128 bits
        return keyGen.generateKey();  // Retorna la clave secreta
    }

    // Método para generar un vector de inicialización (IV)
    private static IvParameterSpec generarIV() {
        // Vector de inicialización de tamaño 16 bytes (128 bits)
        byte[] iv = new byte[BLOCK_SIZE];
        SecureRandom random = new SecureRandom();
        random.nextBytes(iv);  // Llena el IV con valores aleatorios
        return new IvParameterSpec(iv);
    }

    // Método para cifrar un fichero
    public static void cifrarFicheroAES(File inputFile, File outputFile, SecretKey clave, IvParameterSpec iv) throws Exception {
        // Instancia del cifrador AES en modo CBC con relleno PKCS5
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, clave, iv);  // Inicializar para cifrar
        
        // Leer el contenido del fichero
        FileInputStream fis = new FileInputStream(inputFile);
        byte[] inputBytes = new byte[(int) inputFile.length()];
        fis.read(inputBytes);
        fis.close();

        // Cifrar los datos leídos
        byte[] outputBytes = cipher.doFinal(inputBytes);

        // Escribir el fichero cifrado
        FileOutputStream fos = new FileOutputStream(outputFile);
        fos.write(outputBytes);
        fos.close();
    }

    // Método para descifrar un fichero
    public static void descifrarFicheroAES(File inputFile, File outputFile, SecretKey clave, IvParameterSpec iv) throws Exception {
        // Instancia del descifrador AES en modo CBC con relleno PKCS5
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.DECRYPT_MODE, clave, iv);  // Inicializar para descifrar
        
        // Leer el contenido del fichero cifrado
        FileInputStream fis = new FileInputStream(inputFile);
        byte[] inputBytes = new byte[(int) inputFile.length()];
        fis.read(inputBytes);
        fis.close();

        // Descifrar los datos leídos
        byte[] outputBytes = cipher.doFinal(inputBytes);

        // Escribir el fichero descifrado
        FileOutputStream fos = new FileOutputStream(outputFile);
        fos.write(outputBytes);
        fos.close();
    }

    public static void main(String[] args) {
        try {
            // Fichero de entrada y salida
            File inputFile = new File("texto_cifrado.txt");
            File encryptedFile = new File("texto_cifrado_aes.bin");
            File decryptedFile = new File("texto_descifrado.txt");

            // Generar clave y vector de inicialización (IV)
            SecretKey claveAES = generarClaveAES();
            IvParameterSpec iv = generarIV();

            // Cifrar el fichero
            System.out.println("Cifrando el fichero...");
            cifrarFicheroAES(inputFile, encryptedFile, claveAES, iv);
            System.out.println("Fichero cifrado guardado como: " + encryptedFile.getName());

            // Descifrar el fichero
            System.out.println("Descifrando el fichero...");
            descifrarFicheroAES(encryptedFile, decryptedFile, claveAES, iv);
            System.out.println("Fichero descifrado guardado como: " + decryptedFile.getName());
        } catch (Exception e) {
            e.printStackTrace();
            
        }
    }
}
