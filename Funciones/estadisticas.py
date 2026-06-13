# =============================================================================
# FUNCIONES PARA ESTADÍSTICAS
# =============================================================================

def mostrar_estadisticas(lista_paises):
    """
    Muestra estadísticas globales del dataset de países:
    - País con mayor y menor población
    - Promedio de población y superficie
    - Cantidad de países por continente

    Parámetro:
        lista_paises: lista de diccionarios con claves 'nombre', 'poblacion',
                      'superficie', 'continente'
    """

    # -------------------------------------------------------------------------
    # PASO 0: Verificar que haya países para analizar
    # -------------------------------------------------------------------------
    if len(lista_paises) == 0:
        print("\n/ / / / / No hay países cargados para mostrar estadísticas. / / / / /")
        return

    # -------------------------------------------------------------------------
    # PASO 1: Inicializar variables de control
    # -------------------------------------------------------------------------
    max_poblacion = -1
    pais_max = ""

    min_poblacion = 999999999999
    pais_min = ""

    acum_poblacion = 0
    acum_superficie = 0
    cantidad_paises = 0

    continentes = {}

    # -------------------------------------------------------------------------
    # PASO 2: Recorrer la lista UNA SOLA VEZ
    # -------------------------------------------------------------------------
    for pais in lista_paises:

        if pais["poblacion"] > max_poblacion:
            max_poblacion = pais["poblacion"]
            pais_max = pais["nombre"]

        if pais["poblacion"] < min_poblacion:
            min_poblacion = pais["poblacion"]
            pais_min = pais["nombre"]

        acum_poblacion = acum_poblacion + pais["poblacion"]
        acum_superficie = acum_superficie + pais["superficie"]
        cantidad_paises = cantidad_paises + 1

        continente_actual = pais["continente"]

        if continente_actual in continentes:
            continentes[continente_actual] = continentes[continente_actual] + 1
        else:
            continentes[continente_actual] = 1

    # -------------------------------------------------------------------------
    # PASO 3: Calcular promedios
    # -------------------------------------------------------------------------
    promedio_poblacion = acum_poblacion / cantidad_paises
    promedio_superficie = acum_superficie / cantidad_paises

    # -------------------------------------------------------------------------
    # PASO 4: Mostrar resultados formateados
    # -------------------------------------------------------------------------
    print("\n" + "=" * 50)
    print("         E S T A D Í S T I C A S   G L O B A L E S")
    print("=" * 50)

    print(f"\n  País con MAYOR población:")
    print(f"     {pais_max} ({max_poblacion:,} habitantes)")

    print(f"\n  País con MENOR población:")
    print(f"     {pais_min} ({min_poblacion:,} habitantes)")

    print(f"\n  Promedio de población: {promedio_poblacion:,.0f} habitantes")
    print(f"  Promedio de superficie: {promedio_superficie:,.0f} km²")

    print(f"\n  Cantidad de países por continente:")
    for continente, cantidad in continentes.items():
        print(f"     • {continente}: {cantidad} país(es)")

    print("\n" + "=" * 50)
 