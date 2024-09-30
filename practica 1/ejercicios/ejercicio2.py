import pandas as pd
import os

class GestorOlimpiadas:
    def __init__(self):
        self.archivo_eventos_atletas = "athlete_events.csv"
        self.archivo_olimpiadas = "olimpiadas.csv"

    # 1. Generar fichero csv de olimpiadas
    def generar_fichero_csv(self):
        # Cargar el archivo de eventos de atletas
        try:
            df = pd.read_csv(self.archivo_eventos_atletas)
            # Seleccionar las columnas relevantes
            olimpiadas_df = df[['Games', 'Year', 'Season', 'City']].drop_duplicates()
            # Guardar en un nuevo archivo CSV
            olimpiadas_df.to_csv(self.archivo_olimpiadas, index=False)
            print(f"Archivo '{self.archivo_olimpiadas}' generado con éxito.")
        except FileNotFoundError:
            print(f"El archivo '{self.archivo_eventos_atletas}' no se encontró.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    # 2. Buscar deportista
    def buscar_deportista(self):
        nombre_deportista = input("Introduce el nombre del deportista a buscar: ").strip()
        df = pd.read_csv(self.archivo_eventos_atletas)

        # Filtrar por nombre del deportista
        resultados = df[df['Name'].str.contains(nombre_deportista, case=False, na=False)]

        if not resultados.empty:
            print(f"\nResultados de la búsqueda para '{nombre_deportista}':")
            print(resultados[['Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'NOC', 'Event', 'Medal']])
        else:
            print(f"No se encontraron deportistas con el nombre '{nombre_deportista}'.")

    # 3. Buscar deportistas por deporte y olimpiada
    def buscar_deportistas_por_deporte_y_olimpiada(self):
        deporte = input("Introduce el deporte: ").strip()
        año = input("Introduce el año olímpico: ").strip()
        temporada = input("Introduce la temporada (Verano/Invierno): ").strip()

        df = pd.read_csv(self.archivo_eventos_atletas)
        # Filtrar los resultados
        resultados = df[(df['Sport'].str.contains(deporte, case=False, na=False)) &
                        (df['Year'] == int(año)) &
                        (df['Season'].str.contains(temporada, case=False, na=False))]

        if not resultados.empty:
            info_juegos = resultados[['Games', 'City']].drop_duplicates().values[0]
            print(f"\nEdición Olímpica: {info_juegos[0]} en {info_juegos[1]} para el deporte: {deporte}")
            print("\nDeportistas participantes:")
            print(resultados[['Name', 'Event', 'Medal']])
        else:
            print(f"No se encontraron deportistas en el deporte '{deporte}' para el año {año} en la temporada {temporada}.")

    # 4. Añadir deportista
    def añadir_deportista(self):
        nombre = input("Introduce el nombre del deportista: ")
        sexo = input("Introduce el sexo del deportista (M/F): ")
        edad = int(input("Introduce la edad del deportista: "))
        altura = float(input("Introduce la altura del deportista en cm: "))
        peso = float(input("Introduce el peso del deportista en kg: "))
        equipo = input("Introduce el equipo del deportista: ")
        noc = input("Introduce el NOC del deportista: ")
        deporte = input("Introduce el deporte: ")
        evento = input("Introduce el evento: ")
        medalla = input("Introduce la medalla (Oro/Plata/Bronce/Ninguna): ")

        # Crear un DataFrame con el nuevo deportista
        nuevo_deportista = pd.DataFrame({
            'Name': [nombre],
            'Sex': [sexo],
            'Age': [edad],
            'Height': [altura],
            'Weight': [peso],
            'Team': [equipo],
            'NOC': [noc],
            'Event': [evento],
            'Medal': [medalla]
        })

        # Añadir al archivo existente
        try:
            nuevo_deportista.to_csv(self.archivo_eventos_atletas, mode='a', header=False, index=False)
            print(f"Deportista '{nombre}' añadido con éxito.")
        except Exception as e:
            print(f"Ocurrió un error al añadir el deportista: {e}")

    # Método que inicia el menú interactivo
    def iniciar(self):
        while True:
            print("\nMenú de opciones:")
            print("1. Generar fichero CSV de olimpiadas")
            print("2. Buscar deportista")
            print("3. Buscar deportistas por deporte y olimpiada")
            print("4. Añadir deportista")
            print("5. Salir")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                self.generar_fichero_csv()
            elif opcion == '2':
                self.buscar_deportista()
            elif opcion == '3':
                self.buscar_deportistas_por_deporte_y_olimpiada()
            elif opcion == '4':
                self.añadir_deportista()
            elif opcion == '5':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intenta de nuevo.")

# Iniciar el programa
if __name__ == "__main__":
    gestor = GestorOlimpiadas()
    gestor.iniciar()
