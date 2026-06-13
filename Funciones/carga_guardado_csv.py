# ============================================================================
# FUNCIONES CARGA Y GUARDADO DE CSV
# =============================================================================

def cargar_paises():

    paises= []
    try:
        with open(ARCHIVO_CSV,"r",encoding="utf-8") as archivo:
        
            #Lector de archivo
            lector=csv.DictReader(archivo)

            for fila in lector:
                fila["poblacion"] = int(fila["poblacion"])
                fila["superficie"] = int(fila["superficie"])

                paises.append(fila)
    except FileNotFoundError:
        print("\n+ + Advertencia: No se encontró 'paises.csv'. Se iniciará con lista vacía. Puede comenzar a agregar países desde el menú. + +")
    return paises



def guardar_paises(lista_paises):
    pass
