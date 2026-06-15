"""
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                TRABAJO PRÁCTICO INTEGRADOR | PROGRAMACIÓN 1 | UTN
                                    ACOSTA BENJAMÍN 42.912.227| HERNÁNDEZ GABRIEL DNI:42.532.318
                                        GESTIÓN DE DATASET PAÍSES
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""


# IMPORTS

# Solo importamos lo que realmente se usa en main.py

# carga_guardado_csv: para leer y escribir el archivo CSV
from carga_guardado_csv import cargar_paises, guardar_paises

# agregar_buscar_actualizar_paises: para modificar datos (agregar, actualizar, buscar)
from agregar_buscar_actualizar_paises import agregar_pais, buscar_pais, actualizar_pais

# filtrado: funciones  para filtrar países
from filtrado import filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie

# ordenamiento: funciones para ordenar países
from ordenamiento import ordenar_por_nombre, ordenar_por_poblacion, ordenar_por_superficie

# estadisticas: función  para mostrar estadísticas
from estadisticas import mostrar_estadisticas

# menu_presentacion: funciones para mostrar menú y tabla
from menu_presentacion import mostrar_menu, mostrar_paises


# CONSTANTE
# Nombre del archivo CSV donde se guardan los datos.
# Está en la misma carpeta que el programa.
ARCHIVO_CSV = "paises.csv"


# FUNCIÓN PRINCIPAL
def main():
    
    # Llamamos a cargar_paises(), pasándole el nombre del archivo.
    # Si el archivo no existe, devuelve lista vacía y muestra advertencia.
    lista_paises = cargar_paises(ARCHIVO_CSV)
    
    print(f"\n>>> Se cargaron {len(lista_paises)} país(es) desde '{ARCHIVO_CSV}'.")
    
    
    # Bucle principal del menú 
    while True:
        
        # Mostramos el menú con las opciones.
        mostrar_menu()
        
        # Pedimos la opción al usuario.
        # .strip() quita espacios accidentales al principio/final.
        opcion = input("\nSeleccione una opción: ").strip()
        
        #Validación de opción: debe ser un número entre 0 y 7
        #Verificamos si la opción está en la lista de opciones válidas.
        if opcion not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            print("\n/ / / / / Opción inválida. Debe ser un número entre 0 y 7. / / / / /")
            continue 
        
        # Convertimos "opcion" a entero para usar en los if/elif.
        opcion = int(opcion)
        
        #Agregar país
        if opcion == 1:
            # Llamamos a la función.
            # Le pasamos la lista y el nombre del archivo para que guarde automáticamente.
            agregar_pais(lista_paises, ARCHIVO_CSV)
            # Ya guarda dentro de su función, no necesitamos llamar guardar_paises() acá.
        
        #Actualizar país
        elif opcion == 2:
            # Igual que agregar,guarda automáticamente.
            actualizar_pais(lista_paises, ARCHIVO_CSV)
        
       
        #Buscar país
        elif opcion == 3:
            buscar_pais(lista_paises)
        
        
        #Filtrar países
        elif opcion == 4:
            #elige qué tipo de filtro quiere.
            print("\n--- Filtrar por ---")
            print("  [1] Continente")
            print("  [2] Población")
            print("  [3] Superficie")
            
            sub_opcion = input("\nSeleccione una opción: ").strip()
            
            if sub_opcion == "1":
                filtrar_por_continente(lista_paises)
            elif sub_opcion == "2":
                filtrar_por_poblacion(lista_paises)
            elif sub_opcion == "3":
                filtrar_por_superficie(lista_paises)
            else:
                print("\n/ / / / / Opción de filtrado inválida. / / / / /")
        
        #Ordenar países
        elif opcion == 5:
            #primero elige el criterio, luego el orden.
            print("\n--- Ordenar por ---")
            print("  [1] Nombre")
            print("  [2] Población")
            print("  [3] Superficie")
            
            sub_opcion = input("\nSeleccione una opción: ").strip()
            
            # Validamos
            if sub_opcion not in ["1", "2", "3"]:
                print("\n/ / / / / Opción de ordenamiento inválida. / / / / /")
                continue 
            
            print("\n--- Orden ---")
            print("  [1] Ascendente (A-Z / Menor a Mayor)")
            print("  [2] Descendente (Z-A / Mayor a Menor)")
            
            orden = input("\nSeleccione una opción: ").strip()
            
            if orden == "1":
                ascendente = True
            elif orden == "2":
                ascendente = False
            else:
                print("\n/ / / / / Opción de orden inválida. / / / / /")
                continue  
            
            # Ejecutamos el ordenamiento según el criterio elegido
            if sub_opcion == "1":
                ordenar_por_nombre(lista_paises, ascendente)
            elif sub_opcion == "2":
                ordenar_por_poblacion(lista_paises, ascendente)
            elif sub_opcion == "3":
                ordenar_por_superficie(lista_paises, ascendente)
        
        #Mostrar estadísticas
        elif opcion == 6:
            mostrar_estadisticas(lista_paises)
        
        #Mostrar todos los países
        elif opcion == 7:
            mostrar_paises(lista_paises)
        
        #Salir y guardar
        elif opcion == 0:
            guardar_paises(lista_paises, ARCHIVO_CSV)
            print("\n+ + + + + Datos guardados. ¡Hasta luego! + + + + +")
            break 

#INICIO DEL PROGRAMA
if __name__ == "__main__":
    main()