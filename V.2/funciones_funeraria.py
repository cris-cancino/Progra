import os

servicios = [
    [1, "Servicio Básico (Urna de madera y traslado)", 500000],
    [2, "Servicio Premium (Urna tallada, capilla y traslado)", 1200000],
    [3, "Servicio de Cremación (Cremación y ánfora estándar)", 900000]
]

ordenes_generadas = []

# ==============================================================================
# FUNCIONES DE VALIDACIÓN DE SEGURIDAD (Puntos 3, 5 y 6)
# ==============================================================================

def solicitar_texto_seguro(mensaje_input, permitir_numeros=False, largo_maximo=40):
    """
    Filtra la entrada del usuario impidiendo textos vacíos, excesivamente largos,
    con caracteres especiales o con números (si no están permitidos).
    """
    # Lista de caracteres especiales prohibidos en los inputs de texto
    caracteres_prohibidos = [
        "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", 
        "{", "}", "[", "]", ";", ":", "'", '"', "<", ">", "?", "/", "\\", "|", "`", "~"
    ]
    
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    while True:
        entrada = input(mensaje_input).strip()
        
        # Validación: No permitir vacío
        if entrada == "":
            print("Error: El campo no puede quedar vacío.")
            continue
            
        # Validación: Control de longitud máxima (Punto 5)
        if len(entrada) > largo_maximo:
            print(f"Error: El texto es demasiado largo (Máximo {largo_maximo} caracteres).")
            continue
            
        # Validación: Bloqueo de caracteres especiales (Punto 6)
        tiene_caracter_especial = False
        for caracter in caracteres_prohibidos:
            if caracter in entrada:
                tiene_caracter_especial = True
                break
        if tiene_caracter_especial:
            print("Error: No se permiten caracteres especiales (!, @, #, $, etc.).")
            continue

        # Validación: Verificar si tiene números cuando no corresponden
        if not permitir_numeros:
            tiene_numero = False
            for num in numeros:
                if num in entrada:
                    tiene_numero = True
                    break
            if tiene_numero:
                print("Error: Este campo no debe contener números.")
                continue

        return entrada


def solicitar_numero_seguro(mensaje_input, valor_minimo=1, valor_maximo=None):
    """
    Captura excepciones de conversión numérica impidiendo el ingreso de letras
    o valores fuera de los rangos establecidos.
    """
    while True:
        try:
            valor = int(input(mensaje_input))
            
            if valor < valor_minimo:
                print(f"Error: El valor debe ser igual o mayor a {valor_minimo}.")
                continue
                
            if valor_maximo is not None and valor > valor_maximo:
                print(f"Error: El valor no puede ser mayor a {valor_maximo}.")
                continue
                
            return valor
        except ValueError:
            print("Error: Debe ingresar un número entero válido (no se permiten letras ni espacios).")


# ==============================================================================
# FUNCIONES DEL SISTEMA PRINCIPAL (Optimizadas con validaciones)
# ==============================================================================

def verServicios():
    print("\n=== LISTA DE SERVICIOS DISPONIBLES ===")
    print("--------------------------------------------------")
    for s in servicios:
        print(f"ID: {s[0]} | Detalle: {s[1]}")
        print(f"Precio: ${s[2]}")
        print("--------------------------------------------------")


def editarPrecio(rol_usuario):
    if rol_usuario != 'jefe':
        print("\n[ACCESO DENEGADO]: Esta operación solo puede ser realizada por el Jefe.\n")
        return

    print("\n=== EDITAR SERVICIO (DETALLE Y PRECIO) ===")
    
    # Validamos el ID de manera segura impidiendo caídas por letras
    id_buscar = solicitar_numero_seguro("Ingrese el ID del servicio a modificar (1, 2 o 3):\n", 1, 3)
    
    for s in servicios:
        if s[0] == id_buscar:
            servicio_encontrado = s
            break

    print(f"\nServicio actual: {servicio_encontrado[1]}")
    print(f"Precio actual: ${servicio_encontrado[2]}")
    print("--------------------------------------------------")

    # Modificación del detalle usando el filtro de texto seguro (Permite números por si el servicio los lleva)
    nuevo_detalle = solicitar_texto_seguro("Ingrese el nuevo detalle del servicio:\n", permitir_numeros=True, largo_maximo=80)
    servicio_encontrado[1] = nuevo_detalle

    # Modificación del precio usando el filtro numérico seguro
    nuevo_precio = solicitar_numero_seguro("Ingrese el nuevo precio para este servicio:\n", valor_minimo=1)
    servicio_encontrado[2] = nuevo_precio
    
    print("\n¡Servicio actualizado con éxito!\n")


def generarOrden():
    print("\n=== GENERAR ÓRDEN DE SERVICIO ===")
    
    # El nombre del cliente no acepta números y tiene un largo lógico máximo de 35 caracteres
    cliente = solicitar_texto_seguro("Ingrese el nombre del cliente / contratante:\n", permitir_numeros=False, largo_maximo=35)
    
    # El RUT/ID puede llevar letras y números, pero no caracteres especiales
    rut_o_id = solicitar_texto_seguro("Ingrese el RUT o ID del cliente (Sin puntos ni guión):\n", permitir_numeros=True, largo_maximo=12)
    
    # ID de servicio numérico controlado entre 1 y 3
    id_servicio = solicitar_numero_seguro("Ingrese el ID del servicio que desea contratar (1, 2 o 3):\n", 1, 3)
    
    for s in servicios:
        if s[0] == id_servicio:
            servicio_seleccionado = s
            break

    aux_orden = []
    aux_orden.append(cliente)
    aux_orden.append(rut_o_id)
    aux_orden.append(servicio_seleccionado[1])
    aux_orden.append(servicio_seleccionado[2])
    ordenes_generadas.append(aux_orden)
    
    print("\n==========================================")
    print("          ORDEN DE SERVICIO EMITIDA       ")
    print("==========================================")
    print(f"Cliente:     {cliente}")
    print(f"RUT/ID:      {rut_o_id}")
    print(f"Contrata:    {servicio_seleccionado[1]}")
    print(f"Total pagar: ${servicio_seleccionado[2]}")
    print("==========================================\n")


def default():
    print("Error: Selecciona una opción válida (1, 2 o 3).\n")
