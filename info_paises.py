"""
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                TRABAJO PRÁCTICO INTEGRADOR|PROGRAMACION|UTN
                                    ACOSTA BENJAMÍN | HERNÁNDEZ GABRIEL
                                        GESTIÓN DE DATASET PAISES
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""

import csv

# =============================================================================
# CONSTANTE
# =============================================================================
ARCHIVO_CSV = "paises.csv"


# =============================================================================
# FUNCIONES DE VALIDACIÓN
# =============================================================================

def validar_texto(mensaje):
    while True:
        texto=input(mensaje).strip().title()
        if texto == "":
            print("/ / / / / Error: No puedes ingresar espacios vacios.Intente de nuevamente / / / / /")
        else:
            return texto


def validar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
        except ValueError:
            print("/ / / / / Error: Solo números enteros.No se permiten ingresar letras, espacios vacíos o decimales.Intente de nuevamente. / / / / /")
            continue  # vuelve al while
        
        if numero <= 0:
            print("/ / / / / Error: Debe ser mayor a cero. / / / / /")
        else:
            return numero


def validar_rango(mensaje, minimo, maximo):
    while True:
        try:
            numero=int(input(mensaje))
            
            if numero < minimo or numero > maximo:
                raise ValueError(f"El valor tiene que estar entre {minimo} y {maximo}. Intente nuevamente.")

        except ValueError as e:
            if "Intente nuevamente" in str(e):
                print(f"/ / / / / Error: {e} / / / / /")
            else:
                print("/ / / / / Error: No se permiten ingresar letras, espacios vacíos o decimales.Intente de nuevamente. / / / / /")
        else:
            return numero

# ============================================================================
# FUNCIONES CARGA Y GUARDADO DE CSV
# =============================================================================

def cargar_paises():
    pass


def guardar_paises(lista_paises):
    pass


# =============================================================================
# FUNCIONES GREGADO O BUSQUEDA
# =============================================================================

def agregar_pais(lista_paises):
    pass


def actualizar_pais(lista_paises):

    pass


def buscar_pais(lista_paises):
    pass


# =============================================================================
# FUNCIONES PARA FILTRAR
# =============================================================================

def filtrar_por_continente(lista_paises):
    """
    Pide un continente y muestra todos los países que pertenezcan a él.
    """
    pass


def filtrar_por_poblacion(lista_paises):
    """
    Pide un rango mínimo y máximo de población y muestra los países
    que estén dentro de ese rango.
    """
    pass


def filtrar_por_superficie(lista_paises):
    """
    Pide un rango mínimo y máximo de superficie y muestra los países
    que estén dentro de ese rango.
    """
    pass


# =============================================================================
# FUNCIONES PARA ORDENAMIENTO
# =============================================================================

def ordenar_por_nombre_manual(lista_paises, ascendente):
    """
    Ordena la lista de países por nombre usando bubble sort u otro
    """
    pass


def ordenar_por_poblacion(lista_paises, ascendente):
    """
    Ordena la lista por población usando  .sort()
    """
    pass


def ordenar_por_superficie(lista_paises, ascendente):
    """
    Ordena la lista por superficie usando .sort() 
    """
    pass


# =============================================================================
# FUNCIONES PARA ESTADÍSTICAS
# =============================================================================

def mostrar_estadisticas(lista_paises):

    pass


# =============================================================================
# FUNCIONES DE MENÚ Y PRESENTACIÓN
# =============================================================================

def mostrar_menu():
    """
    Muestra las opciones 
    """
    pass


def mostrar_paises(lista_paises):
    """
    Muestra tabla.
    Si lista está vacía, muestra mensaje
    """
    pass


def main():
    pass


# =============================================================================
# INICIO
# =============================================================================
    main()