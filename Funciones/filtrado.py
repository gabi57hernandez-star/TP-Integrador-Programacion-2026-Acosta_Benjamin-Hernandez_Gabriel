# =============================================================================
# FUNCIONES PARA FILTRAR
# =============================================================================

from validaciones import validar_texto, validar_numero

def filtrar_por_continente(lista_paises):
    
    # Verificar que haya países cargados
    
    if len(lista_paises) == 0:
        print("\n/ / / / / No hay países cargados para filtrar. / / / / /")
        return
    
    # Obtener los continentes que EXISTEN en el dataset
    # Creamos una lista con los continentes únicos (sin repetidos).
    # Recorremos todos los países y, si el continente no está en la lista,
    # lo agregamos.
    continentes_existentes = []
    for pais in lista_paises:
        if pais["continente"] not in continentes_existentes:
            continentes_existentes.append(pais["continente"])
    
    # Pedir continente al usuario hasta que sea válido
    while True:
        
        continente_buscado = validar_texto("\nIngrese el continente a filtrar: ")
        
        # Verificamos si el continente ingresado está en la lista de existentes.
        # Usamos .title() para que "asia" y "Asia" sean iguales.
        if continente_buscado.title() in continentes_existentes:
            break  
        
        print(f"\n/ / / / / '{continente_buscado}' no es un continente válido. / / / / /")
        print(f"\n  Continentes disponibles en el dataset:")
        for continente in continentes_existentes:
            print(f"     • {continente}")
        print(f"\n  Por favor, intente nuevamente.")
    
    #lista vacía para los resultados
    resultados = []
    
    
    #Recorrer y filtrar
    for pais in lista_paises:
        # Comparamos con .title() para asegurar que coincidan.
        if pais["continente"].title() == continente_buscado.title():
            resultados.append(pais)
    
    
    #Mostrar resultados 
    print(f"\n{'='*50}")
    print(f"   PAÍSES ENCONTRADOS EN: {continente_buscado.upper()}")
    print(f"{'='*50}")
    
    for indice, pais in enumerate(resultados, start=1):
        print(f"\n  [{indice}] {pais['nombre']}")
        print(f"       Población:  {pais['poblacion']:,} habitantes")
        print(f"       Superficie: {pais['superficie']:,} km²")
    
    print(f"\n{'='*50}")
    print(f"   Total: {len(resultados)} país(es) encontrado(s)")
    print(f"{'='*50}")


def filtrar_por_poblacion(lista_paises):

    # Verificar que haya países cargados
    if len(lista_paises) == 0:
        print("\n/ / / / / No hay países cargados para filtrar. / / / / /")
        return
    
    #Obtener rango real de población en el dataset
    #le decimos cuál es el rango existente.
    poblacion_minima_dataset = lista_paises[0]["poblacion"]
    poblacion_maxima_dataset = lista_paises[0]["poblacion"]
    
    for pais in lista_paises:
        if pais["poblacion"] < poblacion_minima_dataset:
            poblacion_minima_dataset = pais["poblacion"]
        if pais["poblacion"] > poblacion_maxima_dataset:
            poblacion_maxima_dataset = pais["poblacion"]
    
    
    #Pedir rango de población
    print("\n--- Filtro por rango de población ---")
    print(f"  (Rango existente en el dataset: {poblacion_minima_dataset:,} a {poblacion_maxima_dataset:,})")
    
    min_poblacion = validar_numero("Ingrese población MÍNIMA: ")
    max_poblacion = validar_numero("Ingrese población MÁXIMA: ")
    

    while min_poblacion > max_poblacion:
        print("\n/ / / / / Error: El mínimo no puede ser mayor que el máximo. / / / / /")
        min_poblacion = validar_numero("Ingrese población MÍNIMA: ")
        max_poblacion = validar_numero("Ingrese población MÁXIMA: ")
    
    
    #lista vacía para resultados
    resultados = []
    
    
    #Recorrer y filtrar
    for pais in lista_paises:
        if min_poblacion <= pais["poblacion"] <= max_poblacion:
            resultados.append(pais)
    
    
    if len(resultados) == 0:
        print(f"\n/ / / / / No se encontraron países con población entre {min_poblacion:,} y {max_poblacion:,}. / / / / /")
        print(f"\n  Rango de población en el dataset: {poblacion_minima_dataset:,} a {poblacion_maxima_dataset:,}")
        print(f"  Intente con un rango dentro de esos valores.")
        return
    
    
    #Mostrar resultados
    print(f"\n{'='*50}")
    print(f"   PAÍSES CON POBLACIÓN ENTRE {min_poblacion:,} Y {max_poblacion:,}")
    print(f"{'='*50}")
    
    for indice, pais in enumerate(resultados, start=1):
        print(f"\n  [{indice}] {pais['nombre']}")
        print(f"       Población:  {pais['poblacion']:,} habitantes")
        print(f"       Superficie: {pais['superficie']:,} km²")
        print(f"       Continente: {pais['continente']}")
    
    print(f"\n{'='*50}")
    print(f"   Total: {len(resultados)} país(es) encontrado(s)")
    print(f"{'='*50}")


def filtrar_por_superficie(lista_paises):
    
    #Verificar que haya países cargados
    if len(lista_paises) == 0:
        print("\n/ / / / / No hay países cargados para filtrar. / / / / /")
        return
    
    #Obtener rango real de superficie en el dataset
    superficie_minima_dataset = lista_paises[0]["superficie"]
    superficie_maxima_dataset = lista_paises[0]["superficie"]
    
    for pais in lista_paises:
        if pais["superficie"] < superficie_minima_dataset:
            superficie_minima_dataset = pais["superficie"]
        if pais["superficie"] > superficie_maxima_dataset:
            superficie_maxima_dataset = pais["superficie"]
    
    #Pedir rango de superficie
    print("\n--- Filtro por rango de superficie ---")
    print(f"  (Rango existente en el dataset: {superficie_minima_dataset:,} a {superficie_maxima_dataset:,} km²)")
    
    min_superficie = validar_numero("Ingrese superficie MÍNIMA (km²): ")
    max_superficie = validar_numero("Ingrese superficie MÁXIMA (km²): ")
    
    while min_superficie > max_superficie:
        print("\n/ / / / / Error: El mínimo no puede ser mayor que el máximo. / / / / /")
        min_superficie = validar_numero("Ingrese superficie MÍNIMA (km²): ")
        max_superficie = validar_numero("Ingrese superficie MÁXIMA (km²): ")
    
    
    #lista vacía para resultados
    resultados = []
    
    
    #Recorrer y filtrar
    for pais in lista_paises:
        if min_superficie <= pais["superficie"] <= max_superficie:
            resultados.append(pais)
    
    
    
    if len(resultados) == 0:
        print(f"\n/ / / / / No se encontraron países con superficie entre {min_superficie:,} y {max_superficie:,} km². / / / / /")
        print(f"\n  Rango de superficie en el dataset: {superficie_minima_dataset:,} a {superficie_maxima_dataset:,} km²")
        print(f"  Intente con un rango dentro de esos valores.")
        return
    
    
    #Mostrar resultados
    print(f"\n{'='*50}")
    print(f"   PAÍSES CON SUPERFICIE ENTRE {min_superficie:,} Y {max_superficie:,} KM²")
    print(f"{'='*50}")
    
    for indice, pais in enumerate(resultados, start=1):
        print(f"\n  [{indice}] {pais['nombre']}")
        print(f"       Superficie: {pais['superficie']:,} km²")
        print(f"       Población:  {pais['poblacion']:,} habitantes")
        print(f"       Continente: {pais['continente']}")
    
    print(f"\n{'='*50}")
    print(f"   Total: {len(resultados)} país(es) encontrado(s)")
    print(f"{'='*50}")