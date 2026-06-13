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
