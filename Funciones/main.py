"""
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                TRABAJO PRÁCTICO INTEGRADOR | PROGRAMACIÓN 1 | UTN
                                    ACOSTA BENJAMÍN 42.912.227| HERNÁNDEZ GABRIEL DNI:42.532.318
                                        GESTIÓN DE DATASET PAÍSES
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""

# =============================================================================
# IMPORTS
# =============================================================================
# Solo importamos lo que realmente se usa en main.py

# carga_guardado_csv: para leer y escribir el archivo CSV
from carga_guardado_csv import cargar_paises, guardar_paises

# agregar_buscar_actualizar_paises: para modificar datos (agregar, actualizar, buscar)
from agregar_buscar_actualizar_paises import agregar_pais, buscar_pais, actualizar_pais

# filtrado: funciones de Benjamín para filtrar países
from filtrado import filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie

# ordenamiento: funciones de Benjamín para ordenar países
from ordenamiento import ordenar_por_nombre, ordenar_por_poblacion, ordenar_por_superficie

# estadisticas: función de Benjamín para mostrar estadísticas
from estadisticas import mostrar_estadisticas

# menu_presentacion: funciones de Benjamín para mostrar menú y tabla
from menu_presentacion import mostrar_menu, mostrar_paises

# =============================================================================
# CONSTANTE
# =============================================================================
# Nombre del archivo CSV donde se guardan los datos.
# Está en la misma carpeta que el programa.
ARCHIVO_CSV = "paises.csv"

# =============================================================================
# FUNCIÓN PRINCIPAL
# =============================================================================
def main():
    """
    Función principal del programa.
    Controla el flujo completo: carga datos, muestra menú, ejecuta opciones,
    guarda cambios y cierra el programa.
    """
    
    # -------------------------------------------------------------------------
    # PASO 1: Cargar países desde el CSV al iniciar
    # -------------------------------------------------------------------------
    # Llamamos a cargar_paises() de Gabriel, pasándole el nombre del archivo.
    # Si el archivo no existe, devuelve lista vacía y muestra advertencia.
    lista_paises = cargar_paises(ARCHIVO_CSV)
    
    print(f"\n>>> Se cargaron {len(lista_paises)} país(es) desde '{ARCHIVO_CSV}'.")
    
    # -------------------------------------------------------------------------
    # PASO 2: Bucle principal del menú (while True)
    # -------------------------------------------------------------------------
    # Este bucle se repite infinitamente hasta que el usuario elija 0 (Salir).
    # En cada vuelta muestra el menú, espera la opción, y ejecuta la acción.
    while True:
        
        # Mostramos el menú con las opciones (función de Benjamín).
        mostrar_menu()
        
        # Pedimos la opción al usuario.
        # .strip() quita espacios accidentales al principio/final.
        opcion = input("\nSeleccione una opción: ").strip()
        
        # ---------------------------------------------------------------------
        # Validación de opción: debe ser un número entre 0 y 7
        # ---------------------------------------------------------------------
        # Verificamos si la opción está en la lista de opciones válidas.
        # Usamos strings para no tener problemas con input() que siempre devuelve texto.
        if opcion not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            print("\n/ / / / / Opción inválida. Debe ser un número entre 0 y 7. / / / / /")
            continue  # Volvemos al inicio del while, mostramos el menú de nuevo
        
        # Convertimos a entero para usar en los if/elif.
        opcion = int(opcion)
        
        # ---------------------------------------------------------------------
        # OPCIÓN 1: Agregar país
        # ---------------------------------------------------------------------
        if opcion == 1:
            # Llamamos a la función de Gabriel.
            # Le pasamos la lista y el nombre del archivo para que guarde automáticamente.
            agregar_pais(lista_paises, ARCHIVO_CSV)
            # Gabriel ya guarda dentro de su función, no necesitamos llamar guardar_paises() acá.
        
        # ---------------------------------------------------------------------
        # OPCIÓN 2: Actualizar país
        # ---------------------------------------------------------------------
        elif opcion == 2:
            # Igual que agregar, Gabriel maneja todo y guarda automáticamente.
            actualizar_pais(lista_paises, ARCHIVO_CSV)
        
        # ---------------------------------------------------------------------
        # OPCIÓN 3: Buscar país
        # ---------------------------------------------------------------------
        elif opcion == 3:
            # Solo busca, no modifica nada, no necesita guardar.
            buscar_pais(lista_paises)
        
        # ---------------------------------------------------------------------
        # OPCIÓN 4: Filtrar países
        # ---------------------------------------------------------------------
        elif opcion == 4:
            # Submenú de filtrado: elige qué tipo de filtro quiere.
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
        
        # ---------------------------------------------------------------------
        # OPCIÓN 5: Ordenar países
        # ---------------------------------------------------------------------
        elif opcion == 5:
            # Submenú de ordenamiento: primero elige el criterio, luego el orden.
            print("\n--- Ordenar por ---")
            print("  [1] Nombre")
            print("  [2] Población")
            print("  [3] Superficie")
            
            sub_opcion = input("\nSeleccione una opción: ").strip()
            
            # Validamos que sea 1, 2 o 3
            if sub_opcion not in ["1", "2", "3"]:
                print("\n/ / / / / Opción de ordenamiento inválida. / / / / /")
                continue  # Volvemos al menú principal
            
            # Pedimos ascendente o descendente
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
                continue  # Volvemos al menú principal
            
            # Ejecutamos el ordenamiento según el criterio elegido
            if sub_opcion == "1":
                ordenar_por_nombre(lista_paises, ascendente)
            elif sub_opcion == "2":
                ordenar_por_poblacion(lista_paises, ascendente)
            elif sub_opcion == "3":
                ordenar_por_superficie(lista_paises, ascendente)
        
        # ---------------------------------------------------------------------
        # OPCIÓN 6: Mostrar estadísticas
        # ---------------------------------------------------------------------
        elif opcion == 6:
            mostrar_estadisticas(lista_paises)
        
        # ---------------------------------------------------------------------
        # OPCIÓN 7: Mostrar todos los países
        # ---------------------------------------------------------------------
        elif opcion == 7:
            mostrar_paises(lista_paises)
        
        # ---------------------------------------------------------------------
        # OPCIÓN 0: Salir y guardar
        # ---------------------------------------------------------------------
        elif opcion == 0:
            # Guardamos la lista actual en el CSV por si acaso.
            # Aunque Gabriel ya guarda en agregar/actualizar, esto asegura que
            # cualquier ordenamiento quede guardado si el usuario quiere.
            guardar_paises(lista_paises, ARCHIVO_CSV)
            print("\n+ + + + + Datos guardados. ¡Hasta luego! + + + + +")
            break  # Rompe el while True y termina el programa


# =============================================================================
# INICIO DEL PROGRAMA
# =============================================================================
# Esta línea es estándar en Python. Significa:
# "Si este archivo se ejecuta directamente (no se importa), llamá a main()"
if __name__ == "__main__":
    main()