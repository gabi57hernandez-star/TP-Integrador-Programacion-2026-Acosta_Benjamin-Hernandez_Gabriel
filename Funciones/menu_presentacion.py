# =============================================================================
# FUNCIONES DE MENÚ Y PRESENTACIÓN
# =============================================================================

def mostrar_menu():
    """
    Muestra el menú principal de opciones en consola.
    """
    
    print("\n" + "=" * 50)
    print("    G E S T I Ó N   D E   P A Í S E S")
    print("=" * 50)
    print("\n  [1]  Agregar país")
    print("  [2]  Actualizar país")
    print("  [3]  Buscar país")
    print("  [4]  Filtrar países")
    print("  [5]  Ordenar países")
    print("  [6]  Mostrar estadísticas")
    print("  [7]  Mostrar todos los países")
    print("  [0]  Salir y guardar")
    print("\n" + "=" * 50)


def mostrar_paises(lista_paises):
    """
    Muestra una tabla con todos los países de la lista recibida.
    Si la lista está vacía, muestra un mensaje de advertencia.
    """
    # -------------------------------------------------------------------------
    # Se verifica que haya países para mostrar
    # -------------------------------------------------------------------------
    if len(lista_paises) == 0:
        print("\n/ / / / / No hay países cargados para mostrar. / / / / /")
        return  # Salimos de la función, no hay nada que mostrar
    
    # -------------------------------------------------------------------------
    # Se muestra el encabezado de la tabla
    # -------------------------------------------------------------------------
    # Usamos caracteres especiales para dibujar líneas y separadores.
    # El :<15 alinea el texto a la izquierda con 15 espacios.
    # El :>12 alinea el número a la derecha con 12 espacios.
    print("\n" + "=" * 80)
    print(f" {'N°':<4} │ {'NOMBRE':<15} │ {'POBLACIÓN':>12} │ {'SUPERFICIE':>12} │ {'CONTINENTE':<12}")
    print("=" * 80)
    
    # -------------------------------------------------------------------------
    # Se recorre la lista y mostrar cada país
    # -------------------------------------------------------------------------
    for indice, pais in enumerate(lista_paises, start=1):
        # Formateamos cada columna con el ancho correcto.
        # :, agrega separadores de miles a los números.
        print(f" [{indice:<2}] │ {pais['nombre']:<15} │ {pais['poblacion']:>12,} │ {pais['superficie']:>12,} │ {pais['continente']:<12}")
    
    # -------------------------------------------------------------------------
    # Se muestra pie de tabla con el total
    # -------------------------------------------------------------------------
    print("=" * 80)
    print(f" Total: {len(lista_paises)} país(es)")
    print("=" * 80)