# ============================================================================
# FUNCIONES CARGA Y GUARDADO DE CSV
# =============================================================================

def cargar_paises(nombre_archivo):

    paises= []
    try:
        with open(nombre_archivo,"r",encoding="utf-8") as archivo:
        
            #Lector de archivo
            lector= csv.DictReader(archivo)

            for fila in lector:
                fila["poblacion"] = int(fila["poblacion"])
                fila["superficie"] = int(fila["superficie"])

                paises.append(fila)
    except FileNotFoundError:
        print("\n+ + Advertencia: No se encontró 'paises.csv'. Se iniciará con lista vacía. Puede comenzar a agregar países desde el menú. + +")
    except Exception as e:
        print(f"\n+ + Error al cargar el archivo: {e} + +")
    return paises



def guardar_paises(lista_paises, nombre_archivo):

    # Definimos el orden exacto de las columnas en el CSV
    fieldnames = ["nombre", "poblacion", "superficie", "continente"]

    try:
        with open(nombre_archivo, "w", encoding="utf-8", newline="") as archivo:

            # Escritor de diccionarios
            escritor = csv.DictWriter(archivo, fieldnames=fieldnames)
            
            #Se escriben  la primera fila nombre,poblacion,superficie,continente
            escritor.writeheader()
            
            #Se escriben todas las filas de la lista
            escritor.writerows(lista_paises)
            
    except PermissionError:
        print(f"\n/ / / / / Error: No se pudo guardar '{nombre_archivo}'. Verificá que el archivo no esté abierto en otro programa. / / / / /")
    except Exception as e:
        print(f"\n/ / / / / Error inesperado al guardar: {e} / / / / /")
