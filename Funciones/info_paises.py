"""
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                TRABAJO PRÁCTICO INTEGRADOR|PROGRAMACION|UTN
                                    ACOSTA BENJAMÍN | HERNÁNDEZ GABRIEL
                                        GESTIÓN DE DATASET PAISES
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""
# =============================================================================
# IMPORTS
# =============================================================================
import csv
from validaciones import validar_texto,validar_numero,validar_rango
from carga_guardado_csv import cargar_paises,guardar_paises
from agregar_buscar_pais import agregar_pais,buscar_pais,actualizar_pais
from filtrado import filtrar_por_continente,filtrar_por_poblacion,filtrar_por_superficie
from ordenamiento import ordenar_por_nombre,ordenar_por_poblacion,ordenar_por_superficie
from estadisticas import mostrar_estadisticas
from menu_presentacion import main,mostrar_menu,mostrar_paises
# =============================================================================
# CONSTANTE
# =============================================================================
ARCHIVO_CSV = "paises.csv"

# =============================================================================
# INICIO
# =============================================================================
main()