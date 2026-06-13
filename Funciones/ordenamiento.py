# =============================================================================
# FUNCIONES PARA ORDENAMIENTO
# =============================================================================

def ordenar_por_nombre(lista_paises, ascendente):
    """
    Ordena la lista de países por nombre usando Bubble Sort.
    Modifica la lista original (no crea una nueva).
    
    Parámetros:
        lista_paises: lista de diccionarios con los países
        ascendente: True para A-Z, False para Z-A
    """
    
    # -------------------------------------------------------------------------
    # PASO 0: Verificar que haya países para ordenar
    # -------------------------------------------------------------------------
    if len(lista_paises) == 0:
        print("\n/ / / / / No hay países cargados para ordenar. / / / / /")
        return
    
    # -------------------------------------------------------------------------
    # PASO 1: Bubble Sort
    # -------------------------------------------------------------------------
    # Obtenemos la cantidad de países para saber cuántas vueltas dar.
    n = len(lista_paises)
    
    # Bucle externo: controla las vueltas.
    # En cada vuelta, el elemento más "pesado" (alfabéticamente mayor)
    # "burbujea" hacia el final de la lista.
    for i in range(n - 1):
        
        # Variable para detectar si hubo intercambios en esta vuelta.
        # Si no hubo, la lista ya está ordenada y podemos salir antes.
        hubo_swap = False
        
        # Bucle interno: compara elementos adyacentes.
        # Vamos de 0 hasta n-1-i porque los últimos i elementos ya están ordenados.
        for j in range(n - 1 - i):
            
            # Obtenemos los nombres de los países a comparar.
            nombre_actual = lista_paises[j]["nombre"]
            nombre_siguiente = lista_paises[j + 1]["nombre"]
            
            # Determinamos si debemos intercambiar.
            # Si ascendente es True: ordenamos A-Z (actual > siguiente → swap)
            # Si ascendente es False: ordenamos Z-A (actual < siguiente → swap)
            if ascendente:
                debe_swap = nombre_actual > nombre_siguiente
            else:
                debe_swap = nombre_actual < nombre_siguiente
            
            # Si debe_swap es True, intercambiamos los diccionarios completos.
            if debe_swap:
                # Guardamos el país actual en una variable temporal.
                temp = lista_paises[j]
                # El siguiente pasa a la posición actual.
                lista_paises[j] = lista_paises[j + 1]
                # El temporal (original) pasa a la posición siguiente.
                lista_paises[j + 1] = temp
                
                # Marcamos que hubo un intercambio.
                hubo_swap = True
        
        # Si no hubo ningún swap en toda la vuelta, la lista ya está ordenada.
        # Salimos del bucle externo para no hacer vueltas de más.
        if not hubo_swap:
            break
    
    # -------------------------------------------------------------------------
    # PASO 2: Mostrar resultado
    # -------------------------------------------------------------------------
    # Determinamos el texto según el orden.
    orden_texto = "A-Z" if ascendente else "Z-A"
    
    print(f"\n{'='*50}")
    print(f"   PAÍSES ORDENADOS POR NOMBRE ({orden_texto})")
    print(f"{'='*50}")
    
    for indice, pais in enumerate(lista_paises, start=1):
        print(f"\n  [{indice}] {pais['nombre']}")
        print(f"       Población:  {pais['poblacion']:,} habitantes")
        print(f"       Superficie: {pais['superficie']:,} km²")
        print(f"       Continente: {pais['continente']}")
    
    print(f"\n{'='*50}")


def ordenar_por_poblacion(lista_paises, ascendente):
    """
    Ordena la lista por población usando el método .sort() de Python.
    Modifica la lista original.
    
    Parámetros:
        lista_paises: lista de diccionarios con los países
        ascendente: True para menor a mayor, False para mayor a menor
    """
    
    # -------------------------------------------------------------------------
    # PASO 0: Verificar que haya países
    # -------------------------------------------------------------------------
    if len(lista_paises) == 0:
        print("\n/ / / / / No hay países cargados para ordenar. / / / / /")
        return
    
    # -------------------------------------------------------------------------
    # PASO 1: Ordenar con .sort()
    # -------------------------------------------------------------------------
    # key=lambda pais: pais["poblacion"] le dice a Python:
    # "Para cada elemento de la lista, usá el valor de 'poblacion' como criterio"
    # reverse=True invierte el orden (mayor a menor).
    lista_paises.sort(key=lambda pais: pais["poblacion"], reverse=not ascendente)
    # Explicación de reverse=not ascendente:
    #   Si ascendente es True → reverse=False → orden menor a mayor
    #   Si ascendente es False → reverse=True → orden mayor a menor
    
    # -------------------------------------------------------------------------
    # PASO 2: Mostrar resultado
    # -------------------------------------------------------------------------
    orden_texto = "MENOR a MAYOR" if ascendente else "MAYOR a MENOR"
    
    print(f"\n{'='*50}")
    print(f"   PAÍSES ORDENADOS POR POBLACIÓN ({orden_texto})")
    print(f"{'='*50}")
    
    for indice, pais in enumerate(lista_paises, start=1):
        print(f"\n  [{indice}] {pais['nombre']}")
        print(f"       Población:  {pais['poblacion']:,} habitantes")
        print(f"       Superficie: {pais['superficie']:,} km²")
        print(f"       Continente: {pais['continente']}")
    
    print(f"\n{'='*50}")


def ordenar_por_superficie(lista_paises, ascendente):
    """
    Ordena la lista por superficie usando .sort().
    Es idéntica a ordenar_por_poblacion, pero cambia el campo del diccionario.
    
    Parámetros:
        lista_paises: lista de diccionarios con los países
        ascendente: True para menor a mayor, False para mayor a menor
    """
    
    # -------------------------------------------------------------------------
    # PASO 0: Verificar que haya países
    # -------------------------------------------------------------------------
    if len(lista_paises) == 0:
        print("\n/ / / / / No hay países cargados para ordenar. / / / / /")
        return
    
    # -------------------------------------------------------------------------
    # PASO 1: Ordenar con .sort()
    # -------------------------------------------------------------------------
    # CAMBIO CLAVE: usamos pais["superficie"] en vez de pais["poblacion"]
    lista_paises.sort(key=lambda pais: pais["superficie"], reverse=not ascendente)
    
    # -------------------------------------------------------------------------
    # PASO 2: Mostrar resultado
    # -------------------------------------------------------------------------
    orden_texto = "MENOR a MAYOR" if ascendente else "MAYOR a MENOR"
    
    print(f"\n{'='*50}")
    print(f"   PAÍSES ORDENADOS POR SUPERFICIE ({orden_texto})")
    print(f"{'='*50}")
    
    for indice, pais in enumerate(lista_paises, start=1):
        print(f"\n  [{indice}] {pais['nombre']}")
        print(f"       Superficie: {pais['superficie']:,} km²")
        print(f"       Población:  {pais['poblacion']:,} habitantes")
        print(f"       Continente: {pais['continente']}")
    
    print(f"\n{'='*50}")

