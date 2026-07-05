# ==============================================================================
# IMPORTACIÓN DE LIBRERÍAS
# ==============================================================================
import time  # Para pausar la pantalla unos segundos cuando hay errores de login
import os    # Para limpiar la consola según el sistema operativo (Windows/Mac/Linux)

# ==============================================================================
# CONTROL DE ACCESO (LOGEO)
# ==============================================================================
# Lista con credenciales válidas en formato de diccionarios {usuario: clave}
usuarios = [
    {'root': '123'}, 
    {'admin': 'funeraria2026'}
]

# Bucle infinito para el login. No dejará pasar al menú hasta que el acceso sea válido.
while True:
    userBan = False  # Indica si el usuario existe en los registros
    acceso = False   # Indica si la contraseña coincide con el usuario
    
    # .strip() elimina espacios vacíos accidentales al inicio o al final del texto
    user = input("Ingrese su nombre de Usuario\n").strip()
    password = input("Ingrese su clave\n").strip()
    
    # Buscamos si el usuario ingresado existe en la base de datos
    for x in usuarios:
        userBan = user in x  # True si encuentra la clave dentro del diccionario actual
        if userBan:
            break  # Rompe el ciclo for si encuentra el usuario
            
    # Si el usuario existe, validamos su contraseña correspondiente
    if userBan:
        clave = x[user]  # Extrae la contraseña real del diccionario
        if clave == password:
            acceso = True  # Otorga el acceso
            break          # Rompe el bucle while del login
        else:
            print("Usuario y/o Clave incorrecto\n")
    else:
        print("Usuario y/o Clave incorrecto\n")
        time.sleep(1)
        # Limpieza de pantalla dinámica según el sistema operativo
        if os.name == 'nt': os.system("cls")
        else: os.system("clear")

# ==============================================================================
# SISTEMA PRINCIPAL DE LA FUNERARIA (Solo se ejecuta si acceso es True)
# ==============================================================================
if acceso:
    if os.name == 'nt': os.system("cls")
    else: os.system("clear")
    
    print("--- Sistema de Gestión Funeraria v2.2 ---\n")
    
    # MATRIZ BASE: Almacena los datos de los servicios [ID, Nombre/Detalle, Precio]
    servicios = [
        [1, "Servicio Básico (Urna de madera y traslado)", 500000],
        [2, "Servicio Premium (Urna tallada, capilla y traslado)", 1200000],
        [3, "Servicio de Cremación (Cremación y ánfora estándar)", 900000]
    ]
    
    # Lista global para guardar de manera histórica las órdenes que se emitan
    ordenes_generadas = []

    # --------------------------------------------------------------------------
    # FUNCIÓN 1: MOSTRAR CATÁLOGO DE SERVICIOS
    # --------------------------------------------------------------------------
    def verServicios():
        print("\n=== LISTA DE SERVICIOS DISPONIBLES ===")
        print("--------------------------------------------------")
        # Recorremos cada fila de la matriz servicios
        for s in servicios:
            print(f"ID: {s[0]} | Detalle: {s[1]}")
            print(f"Precio: ${s[2]}")
            print("--------------------------------------------------")

    # --------------------------------------------------------------------------
    # FUNCIÓN 2: EDITAR TANTO EL DETALLE/TEXTO COMO EL PRECIO (TOTALMENTE VALIDADA)
    # --------------------------------------------------------------------------
    def editarPrecio():
        print("\n=== EDITAR SERVICIO (DETALLE Y PRECIO) ===")
        
        # Bucle 1: Validar la búsqueda del ID del servicio
        while True:
            try:
                id_buscar = int(input("Ingrese el ID del servicio a modificar (1, 2 o 3):\n"))
                bandera = False
                
                # Buscamos el ID dentro de la matriz
                for s in servicios:
                    if s[0] == id_buscar:
                        servicio_encontrado = s  # Guardamos la referencia de la lista interna encontrada
                        bandera = True
                        break
                
                if bandera:
                    break  # Si el ID existe, salimos de este bucle de validación
                else:
                    print("Error: El ID ingresado no existe. Intente nuevamente.")
            except ValueError:
                # Captura el error si el usuario escribe letras en lugar de números
                print("Error: Debe ingresar un número entero válido.")

        # Mostramos los datos actuales antes de modificarlos
        print(f"\nServicio actual: {servicio_encontrado[1]}")
        print(f"Precio actual: ${servicio_encontrado[2]}")
        print("--------------------------------------------------")

        # Bucle 2: Validar el ingreso del nuevo nombre/detalle
        while True:
            nuevo_detalle = input("Ingrese el nuevo detalle del servicio (ej: 'Servicio Básico (Solo Urna)'):\n").strip()
            if nuevo_detalle != "":  # Valida que no sea una cadena vacía
                servicio_encontrado[1] = nuevo_detalle  # Sobrescribe el texto en la matriz original
                break
            else:
                print("Error: El detalle no puede quedar vacío.")

        # Bucle 3: Validar el ingreso del nuevo precio numérico
        while True:
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio para este servicio:\n"))
                if nuevo_precio > 50000:  # Valida que el monto sea un número lógico real
                    servicio_encontrado[2] = nuevo_precio  # Sobrescribe el precio en la matriz original
                    
                    # Confirmación visual de los cambios guardados con éxito
                    print("\n¡Servicio actualizado con éxito!")
                    print(f"Nuevo Detalle: {servicio_encontrado[1]}")
                    print(f"Nuevo Precio: ${servicio_encontrado[2]}\n")
                    break  # Rompe el bucle de validación de precio
                else:
                    print("Error: El precio debe ser un monto mayor a $50.000.")
            except ValueError:
                print("Error: Debe ingresar un monto numérico válido.")

    # --------------------------------------------------------------------------
    # FUNCIÓN 3: CREAR ÓRDENES DE SERVICIO PARA CLIENTES (TOTALMENTE VALIDADA)
    # --------------------------------------------------------------------------
    def generarOrden():
        print("\n=== GENERAR ÓRDEN DE SERVICIO ===")
        
        # LISTA SUGERIDA POR TU PROFESOR: Contiene los números como texto para poder comparar
        numeros_prohibidos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        # Bucle 1: Validar nombre del comprador (No debe incluir números ni estar vacío)
        while True:
            cliente = input("Ingrese el nombre del cliente / contratante:\n").strip()
            
            if cliente != "":
                tiene_numero = False  # Bandera para rastrear si encontramos un número malo
                
                # Recorremos la lista de números prohibidos propuesta por tu profesor
                for num in numeros_prohibidos:
                    if num in cliente:  # Si el número actual está dentro del texto del cliente
                        tiene_numero = True  # Activamos la bandera de error
                        break                # Dejamos de revisar los demás números para ahorrar tiempo
                
                # Si revisamos todo y NO tiene ningún número, el nombre es aceptado
                if not tiene_numero:
                    break  # Salimos exitosamente del bucle 'while'
                else:
                    print("Error: El nombre del cliente no debe contener números.")
            else:
                print("Error: El nombre del cliente no puede quedar vacío.")
        
        # Bucle 2: Validar identificación
        while True:
            rut_o_id = input("Ingrese el RUT o ID del cliente:\n").strip()
            if rut_o_id != "":
                break
            else:
                print("Error: El RUT/ID no puede quedar vacío.")
        
        # Bucle 3: Validar que el servicio solicitado realmente exista
        while True:
            try:
                id_servicio = int(input("Ingrese el ID del servicio que desea contratar:\n"))
                bandera = False
                for s in servicios:
                    if s[0] == id_servicio:
                        servicio_seleccionado = s  # Almacena el servicio elegido
                        bandera = True
                        break
                if bandera:
                    break  # ID correcto encontrado, salimos del bucle
                else:
                    print("Error: Ese ID de servicio no existe en el catálogo. Intente de nuevo.")
            except ValueError:
                print("Error: Debe digitar un número entero.")

        # Proceso de almacenamiento histórico usando una lista auxiliar temporal
        aux_orden = []
        aux_orden.append(cliente)
        aux_orden.append(rut_o_id)
        aux_orden.append(servicio_seleccionado[1])  # Guarda el texto del servicio vigente
        aux_orden.append(servicio_seleccionado[2])  # Guarda el precio cobrado vigente
        ordenes_generadas.append(aux_orden)          # Se inyecta la lista temporal a la lista global
        
        # Estructura e impresión en pantalla del comprobante de la orden de servicio
        print("\n==========================================")
        print("          ORDEN DE SERVICIO EMITIDA       ")
        print("==========================================")
        print(f"Cliente:     {cliente}")
        print(f"RUT/ID:      {rut_o_id}")
        print(f"Contrata:    {servicio_seleccionado[1]}")
        print(f"Total pagar: ${servicio_seleccionado[2]}")
        print("==========================================\n")

    # Función por defecto vinculada al menú
    def default():
        print("Error: Selecciona una opción válida (1, 2 o 3).\n")

    # ==============================================================================
    # MENÚ PRINCIPAL E INTERACTIVO (SIMULACIÓN SWITCH CASE)
    # ==============================================================================
    respuesta = "si"  # Variable centinela para mantener el programa corriendo
    
    # Diccionario 'switch' que asocia números enteros directamente con las funciones anteriores
    switch = {1: verServicios, 2: editarPrecio, 3: generarOrden}
    
    while respuesta == "si":
        print("--- MENÚ PRINCIPAL ---")
        print("Opción 1 >> Ver Servicios y Precios <<")
        print("Opción 2 >> Editar Detalle y Precio de un Servicio <<")
        print("Opción 3 >> Generar Orden de Servicio <<\n")
        
        # Bucle interno: Valida que la opción del menú principal sea estrictamente un entero numérico
        while True:
            try:
                opcion = int(input("Ingresar Opción:\n"))
                break  # Sale del bucle de captura si es un número válido
            except ValueError:
                print("Error: Debe ingresar un número entero (1, 2 o 3).\n")
        
        # Llama a la función del diccionario pasándole la opción elegida. 
        # Si no la encuentra, ejecuta la función 'default'
        switch.get(opcion, default)()
        
        # Bucle interno: Obliga al usuario a responder estrictamente con "si" o "no"
        while True:
            respuesta = input("¿Desea volver al menú principal? (si/no):\n").strip().lower()
            if respuesta == "si" or respuesta == "no":
                break  # Sale de la validación de la respuesta
            else:
                print("Error: Por favor responda estrictamente 'si' o 'no'.")
        
        # Limpieza de pantalla tras salir o repetir el ciclo
        if os.name == 'nt': os.system("cls")
        else: os.system("clear")
        
    print("Gracias por utilizar el sistema funerario. Cierre de sesión exitoso.")