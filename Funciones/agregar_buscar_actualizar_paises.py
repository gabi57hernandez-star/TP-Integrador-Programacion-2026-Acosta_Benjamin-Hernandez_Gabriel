# =============================================================================
# FUNCIONES AGREGADO, BUSQUEDA O ACTUALIZACION          
# =============================================================================
from carga_guardado_csv import guardar_paises
from validaciones import validar_texto, validar_numero

#/////////////////////////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def agregar_pais(lista_paises, archivo_csv):
    print("="*20)
    print("AGREGAR PAÍS")
    print("="*20)

#Se ingresan los datos del diccionario validandolos con funciones
    #Se valida si el pais ya existe
    while True:
        nombre=validar_texto("Ingrese el nombre del país: ")
        existe=False

        for pais in lista_paises:
            if pais["nombre"].lower() == nombre.lower():
                print(f"\n/ / / / / Error: {nombre} ya existe. Intente con otro nombre. / / / / /")
                existe=True
                break
            
        if not existe:
            break

    poblacion=validar_numero("Ingrese su población: ")
    superficie=validar_numero("Ingrese su superficie en km cuadrados: ")
    continente=validar_texto("Ingrese el continente en el que se encuentra: ")

#Se crea el nuevo diccionario que se va a agregar
    nuevo_pais ={
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
#Se agrega el nuevo diccionario a la lista
    lista_paises.append(nuevo_pais)

#Se llama a la funcion para guardar la lista a en el archivo
    guardar_paises(lista_paises,archivo_csv)

    print("\n+ + + + + País agregado correctamente. + + + + +")

#/////////////////////////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def actualizar_pais(lista_paises,archivo_csv):

#Se verifica si la lista no esta vacía
    if len(lista_paises) == 0:
        print("\n/ / / / / No hay países cargados en el sistema. / / / / /")
        return

#Ingreso y validación de existencia del pais    
    print("="*15)
    print("ACTUALIZAR PAÍS")
    print("="*15)

    while True:
        nombre=validar_texto("\n Ingrese el pais que desea actualizar")

        encontrado=None
        for pais in lista_paises:
            if pais["nombre"].lower() == nombre.lower():
                encontrado = pais
                break
        if encontrado is not None:
            break
        print(f"/ / / / / Error: El país {nombre}, no existe en el sistema. / / / / /")
        
#Se muestran los datos actuales.
    print(f"\nDatos actuales de {encontrado['nombre']}:")
    print(f"_ Población: {encontrado['poblacion']}")
    print(f"_ Superficie: {encontrado['superficie']} km cuadrados.")

#El usuario ingresa una nueva población y un nuevo número.
    nueva_poblacion = validar_numero("Ingrese la nueva población: ")
    nueva_superficie = validar_numero("Ingrese la nueva superficie en km cuadrados: ")

#Se guardan los nuevos valores en la lista
    encontrado["poblacion"] = nueva_poblacion
    encontrado["superficie"] = nueva_superficie

#Se guarda la lista en el en el csv
    guardar_paises(lista_paises, archivo_csv)

    print(f"\n+ + + + + País '{encontrado['nombre']}' actualizado correctamente. + + + + +")

#/////////////////////////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def buscar_pais(lista_paises):

    print("=" * 15)
    print("BUSCAR PAÍS")
    print("=" * 15)

#Ingreso y validación de texto
    texto_a_buscar = validar_texto("\nIngrese el nombre del país a buscar: ")

#Se buscan coincidencias del valores nombre con el texto ingresado, si las encontramos se guardan en resultados
    resultados = []
    for pais in lista_paises:
        if texto_a_buscar.lower() in pais["nombre"].lower():
            resultados.append(pais)

#Se muestran los resultados,tanto si se encontraron coincidencias o como si no.
    if len(resultados) == 0:
        print(f"\n/ / / / / No se encontraron países que coincidan con '{texto_a_buscar}'. / / / / /")
    else:
        print(f"\n+ + + + + Se encontraron {len(resultados)} coincidencias: + + + + +")
        for pais in resultados:
            print(f" - {pais['nombre']}: Población {pais['poblacion']}, Superficie {pais['superficie']} km², Continente {pais['continente']}")