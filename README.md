# TP-Integrador-Programacion-2026-Acosta_Benjamin-Hernandez_Gabriel
# Gestión de Datos de Países en Python

**Trabajo Práctico Integrador - Programación 1**

**Universidad Tecnológica Nacional (UTN)**  
**Tecnicatura Universitaria en Programación a Distancia**

---

## Integrantes

| Nombre | Apellido |
|--------|----------|
| Benjamín | Acosta |
| Gabriel | Hernández |

---

## Descripción del Programa

Este programa permite gestionar información sobre países mediante un **menú interactivo en consola**. Los datos se almacenan en un archivo **CSV** y el sistema permite realizar operaciones de:

- **Agregar** países nuevos
- **Actualizar** datos de población y superficie
- **Buscar** países por nombre (coincidencia parcial o exacta)
- **Filtrar** países por continente, rango de población o rango de superficie
- **Ordenar** países por nombre, población o superficie (ascendente/descendente)
- **Mostrar estadísticas** globales (mayor/menor población, promedios, países por continente)

El proyecto aplica conceptos de **Programación 1**: listas, diccionarios, funciones, condicionales, bucles, ordenamientos, estadísticas básicas y manejo de archivos CSV.

---

## Estructura del Proyecto
TP-Integrador-Programacion/
├── main.py                           # Programa principal (menú y flujo)
├── validaciones.py                   # Funciones de validación de entradas
├── carga_guardado_csv.py             # Lectura y escritura del archivo CSV
├── agregar_buscar_actualizar_paises.py  # Alta, búsqueda y modificación de países
├── filtrado.py                       # Filtros por continente, población y superficie
├── ordenamiento.py                   # Ordenamientos por nombre, población y superficie
├── estadisticas.py                   # Cálculo y muestra de estadísticas globales
├── menu_presentacion.py              # Menú principal y tabla de países
└── paises.csv                        # Dataset base con 50 países


---

## Requisitos

- **Python 3.x** (cualquier versión 3.6 o superior)
- No requiere librerías externas (solo módulos de la biblioteca estándar)

---

## Instrucciones de Uso

### 1. Clonar o descargar el repositorio

```bash
git clone https://github.com/tu-usuario/TP-Integrador-Programacion.git
cd TP-Integrador-Programacion

2. Ejecutar el programa
python main.py


3. Navegar por el menú
Al iniciar, el programa carga automáticamente los datos desde paises.csv y muestra el menú principal:
==================================================
    G E S T I Ó N   D E   P A Í S E S
==================================================

  [1]  Agregar país
  [2]  Actualizar país
  [3]  Buscar país
  [4]  Filtrar países
  [5]  Ordenar países
  [6]  Mostrar estadísticas
  [7]  Mostrar todos los países
  [0]  Salir y guardar

==================================================

Seleccioná una opción ingresando el número correspondiente y seguí las instrucciones en pantalla.


#Ejemplos de Entrada/Salida
##Ejemplo 1: Agregar un país
Entrada:

Seleccione una opción: 1
Ingrese el nombre del país: Uruguay
Ingrese su población: 3473730
Ingrese su superficie en km cuadrados: 176215
Ingrese el continente en el que se encuentra: América

Salida:

+ + + + + País agregado correctamente. + + + + +


##Ejemplo 2: Buscar país por nombre (coincidencia parcial)

Entrada:

Seleccione una opción: 3
Ingrese el nombre del país a buscar: Arge

Salida:

+ + + + + Se encontraron 1 coincidencias: + + + + +
 - Argentina: Población 45376763, Superficie 2780400 km², Continente América


##Ejemplo 3: Filtrar por continente:

Entrada:

Seleccione una opción: 4
Seleccione una opción: 1
Ingrese el continente a filtrar: Asia

Salida:

==================================================
   PAÍSES ENCONTRADOS EN: ASIA
==================================================

  [1] Japón
       Población:  125,800,000 habitantes
       Superficie: 377,975 km²

  [2] China
       Población:  1,439,323,776 habitantes
       Superficie: 9,596,961 km²

  ... (más países)

==================================================
   Total: 25 país(es) encontrado(s)
==================================================


##Ejemplo 4: Mostrar estadísticas
Entrada:

Seleccione una opción: 6

Salida:

==================================================
         E S T A D Í S T I C A S   G L O B A L E S
==================================================

  País con MAYOR población:
     China (1,439,323,776 habitantes)

  País con MENOR población:
     Maldivas (540,544 habitantes)

  Promedio de población: 187,654,321 habitantes
  Promedio de superficie: 1,234,567 km²

  Cantidad de países por continente:
     • Asia: 25 país(es)
     • América: 3 país(es)
     • Europa: 1 país(es)
     • África: 2 país(es)

==================================================


##Ejemplo 5: Ordenar por población (descendente)
Entrada:

Seleccione una opción: 5
Seleccione una opción: 2
Seleccione una opción: 2

Salida:

==================================================
   PAÍSES ORDENADOS POR POBLACIÓN (MAYOR a MENOR)
==================================================

  [1] China
       Población:  1,439,323,776 habitantes
       Superficie: 9,596,961 km²
       Continente: Asia

  [2] India
       Población:  1,380,004,385 habitantes
       Superficie: 3,287,263 km²
       Continente: Asia

  ... (más países)

==================================================


#Formato del Dataset (CSV)
El archivo paises.csv utiliza el siguiente formato:
csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América

nombre: String (nombre del país)
poblacion: Entero (habitantes)
superficie: Entero (km²)
continente: String (continente)


#Decisiones Técnicas
Modularización: Cada funcionalidad está en un archivo separado para cumplir con el principio de "una función = una responsabilidad".
Estructuras de datos: Se utiliza una lista de diccionarios para representar los países en memoria.
Persistencia: Los datos se guardan en formato CSV para facilitar la lectura y edición manual.
Validaciones: Las entradas del usuario se validan para evitar campos vacíos, letras en campos numéricos y valores negativos.
Ordenamiento: Se combina Bubble Sort (manual, para nombre) con el método .sort() de Python (para campos numéricos).


#Dificultades y Soluciones:
| Dificultad                                   | Solución aplicada                                         |
| -------------------------------------------- | --------------------------------------------------------- |
| Manejo de mayúsculas/minúsculas en búsquedas | Uso de `.lower()` y `.title()` para normalizar textos     |
| Validación de rangos numéricos               | Funciones reutilizables en `validaciones.py`              |
| Ordenamiento de diccionarios                 | Uso de `lambda` en `.sort()` para especificar la clave    |
| Persistencia de datos                        | Lectura/escritura automática del CSV en cada modificación |


#Bibliografía / Webgrafía:
Documentación oficial de Python 3.x: https://docs.python.org/3/
Manejo de archivos CSV en Python: https://docs.python.org/3/library/csv.html
Métodos de ordenamiento en Python: https://docs.python.org/3/howto/sorting.html


#Enlaces del Proyecto
Repositorio GitHub: [text](https://github.com/gabi57hernandez-star/TP-Integrador-Programacion-2026-Acosta_Benjamin-Hernandez_Gabriel)

Video demostrativo: https://youtu.be/FyysPd7vm9M

Documentación-Drive:https://docs.google.com/document/d/1Bxk2nFN8A5A06Zcw0dF0BgP8xHkiNfcpA3b8U_gQapQ/edit?usp=sharing

#Notas de Entrega
Trabajo en equipo: 2 integrantes:
Gabriel Hernández DNI:42.532.318
Benjamin Acosta DNI:42.912.227 


