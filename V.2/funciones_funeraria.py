import os

servicios = [
    [1, "Servicio Básico (Urna de madera y traslado)", 500000],
    [2, "Servicio Premium (Urna tallada, capilla y traslado)", 1200000],
    [3, "Servicio de Cremación (Cremación y ánfora estándar)", 900000]
]

ordenes_generadas = []

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
    while True:
        try:
            id_buscar = int(input("Ingrese el ID del servicio a modificar (1, 2 o 3):\n"))
            bandera = False
            for s in servicios:
                if s[0] == id_buscar:
                    servicio_encontrado = s
                    bandera = True
                    break
            if bandera:
                break
            else:
                print("Error: El ID ingresado no existe. Intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    print(f"\nServicio actual: {servicio_encontrado[1]}")
    print(f"Precio actual: ${servicio_encontrado[2]}")
    print("--------------------------------------------------")

    while True:
        nuevo_detalle = input("Ingrese el nuevo detalle del servicio:\n").strip()
        if nuevo_detalle != "":
            servicio_encontrado[1] = nuevo_detalle
            break
        else:
            print("Error: El detalle no puede quedar vacío.")

    while True:
        try:
            nuevo_precio = int(input("Ingrese el nuevo precio para este servicio:\n"))
            if nuevo_precio > 0:
                servicio_encontrado[2] = nuevo_precio
                print("\n¡Servicio actualizado con éxito!\n")
                break
            else:
                print("Error: El precio debe ser un monto mayor a 0.")
        except ValueError:
            print("Error: Debe ingresar un monto numérico válido.")

def generarOrden():
    print("\n=== GENERAR ÓRDEN DE SERVICIO ===")
    
    numeros_prohibidos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    while True:
        cliente = input("Ingrese el nombre del cliente / contratante:\n").strip()
        if cliente != "":
            tiene_numero = False
            for num in numeros_prohibidos:
                if num in cliente:
                    tiene_numero = True
                    break
            if not tiene_numero:
                break
            else:
                print("Error: El nombre del cliente no debe contener números.")
        else:
            print("Error: El nombre del cliente no puede quedar vacío.")
    
    while True:
        rut_o_id = input("Ingrese el RUT o ID del cliente:\n").strip()
        if rut_o_id != "":
            break
        else:
            print("Error: El RUT/ID no puede quedar vacío.")
    
    while True:
        try:
            id_servicio = int(input("Ingrese el ID del servicio que desea contratar:\n"))
            bandera = False
            for s in servicios:
                if s[0] == id_servicio:
                    servicio_seleccionado = s
                    bandera = True
                    break
            if bandera:
                break
            else:
                print("Error: Ese ID de servicio no existe en el catálogo. Intente de nuevo.")
        except ValueError:
            print("Error: Debe digitar un número entero.")

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