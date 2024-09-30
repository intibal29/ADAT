import os
import shutil

class GestorArchivos:
    def __init__(self):
        pass

    # 1. Crear un directorio
    def crear_directorio(self):
        ruta_base = input("Introduce la ruta donde se creará el nuevo directorio: ")
        nombre_directorio = input("Introduce el nombre del nuevo directorio: ")
        ruta_completa = os.path.join(ruta_base, nombre_directorio)

        try:
            os.makedirs(ruta_completa)
            print(f"Directorio '{nombre_directorio}' creado en {ruta_base}")
        except FileExistsError:
            print("El directorio ya existe.")
        except Exception as e:
            print(f"Error al crear el directorio: {e}")

    # 2. Listar un directorio
    def listar_directorio(self):
        ruta = input("Introduce la ruta del directorio que quieres listar: ")

        if os.path.exists(ruta) and os.path.isdir(ruta):
            contenido = os.listdir(ruta)
            print(f"Contenido de {ruta}:")
            for item in contenido:
                item_path = os.path.join(ruta, item)
                if os.path.isdir(item_path):
                    print(f"[DIR]  {item}")
                else:
                    print(f"[FILE] {item}")
        else:
            print("El directorio no existe o no es una carpeta válida.")

    # 3. Copiar un archivo
    def copiar_archivo(self):
        origen = input("Introduce la ruta del archivo original: ")
        destino = input("Introduce la ruta del directorio de destino: ")

        if os.path.isfile(origen) and os.path.exists(destino) and os.path.isdir(destino):
            try:
                shutil.copy(origen, destino)
                print(f"Archivo copiado de {origen} a {destino}")
            except Exception as e:
                print(f"Error al copiar el archivo: {e}")
        else:
            print("La ruta del archivo o el directorio de destino no es válida.")

    # 4. Mover un archivo
    def mover_archivo(self):
        origen = input("Introduce la ruta del archivo a mover: ")
        destino = input("Introduce la ruta del directorio de destino: ")

        if os.path.isfile(origen) and os.path.exists(destino) and os.path.isdir(destino):
            try:
                shutil.move(origen, destino)
                print(f"Archivo movido de {origen} a {destino}")
            except Exception as e:
                print(f"Error al mover el archivo: {e}")
        else:
            print("La ruta del archivo o el directorio de destino no es válida.")

    # 5. Eliminar un archivo/directorio
    def eliminar_archivo_o_directorio(self):
        ruta = input("Introduce la ruta del archivo o directorio a eliminar: ")

        if os.path.isfile(ruta):
            try:
                os.remove(ruta)
                print(f"Archivo '{ruta}' eliminado.")
            except Exception as e:
                print(f"Error al eliminar el archivo: {e}")
        elif os.path.isdir(ruta):
            if not os.listdir(ruta):  # Comprobar si el directorio está vacío
                try:
                    os.rmdir(ruta)
                    print(f"Directorio '{ruta}' eliminado.")
                except Exception as e:
                    print(f"Error al eliminar el directorio: {e}")
            else:
                print(f"El directorio '{ruta}' no está vacío. No se puede eliminar.")
        else:
            print("La ruta especificada no es válida o no existe.")

    # Método que inicia el menú interactivo
    def iniciar(self):
        while True:
            print("\nMenú de opciones:")
            print("1. Crear un directorio")
            print("2. Listar un directorio")
            print("3. Copiar un archivo")
            print("4. Mover un archivo")
            print("5. Eliminar un archivo/directorio")
            print("6. Salir")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                self.crear_directorio()
            elif opcion == '2':
                self.listar_directorio()
            elif opcion == '3':
                self.copiar_archivo()
            elif opcion == '4':
                self.mover_archivo()
            elif opcion == '5':
                self.eliminar_archivo_o_directorio()
            elif opcion == '6':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intenta de nuevo.")

# Iniciar el programa
if __name__ == "__main__":
    gestor = GestorArchivos()
    gestor.iniciar()
