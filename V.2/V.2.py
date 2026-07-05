import time
import os
import funciones_funeraria

usuarios = [
    {'user': 'jefe', 'clave': '123', 'rol': 'jefe'},
    {'user': 'cliente1', 'clave': '321', 'rol': 'cliente'}
]

while True:
    userBan = False
    acceso = False
    rol_usuario = ""
    
    user = input("Ingrese su nombre de Usuario\n").strip()
    password = input("Ingrese su clave\n").strip()
    
    for x in usuarios:
        if x['user'] == user:
            userBan = True
            if x['clave'] == password:
                acceso = True
                rol_usuario = x['rol']
            break
            
    if acceso:
        print(f"\n¡Acceso concedido! Rol asignado: {rol_usuario.upper()}")
        time.sleep(1.5)
        break
    else:
        print("Usuario y/o Clave incorrecto o inexistente.\n")
        time.sleep(1.5)
        if os.name == 'nt': os.system("cls")
        else: os.system("clear")

if acceso:
    if os.name == 'nt': os.system("cls")
    else: os.system("clear")
    
    print("--- Sistema de Gestión Funeraria v4.0 ---\n")
    
    respuesta = "si"
    
    while respuesta == "si":
        print(f"--- MENÚ PRINCIPAL (Usuario actual: {rol_usuario.upper()}) ---")
        print("Opción 1 >> Ver Servicios y Precios << (Todos)")
        print("Opción 2 >> Editar Detalle y Precio de un Servicio << (Solo Jefe)")
        print("Opción 3 >> Generar Orden de Servicio << (Todos)\n")
        
        while True:
            try:
                opcion = int(input("Ingresar Opción:\n"))
                break
            except ValueError:
                print("Error: Debe ingresar un número entero (1, 2 o 3).\n")
        
        # Para llamar a las funciones del otro archivo usamos el prefijo 'funciones_funeraria.'
        if opcion == 1:
            funciones_funeraria.verServicios()
        elif opcion == 2:
            # Le pasamos el rol por parámetro para que verifique si es jefe
            funciones_funeraria.editarPrecio(rol_usuario)
        elif opcion == 3:
            funciones_funeraria.generarOrden()
        else:
            funciones_funeraria.default()
        
        while True:
            respuesta = input("¿Desea volver al menú principal? (si/no):\n").strip().lower()
            if respuesta == "si" or respuesta == "no":
                break
            else:
                print("Error: Por favor responda estrictamente 'si' o 'no'.")
        
        if os.name == 'nt': os.system("cls")
        else: os.system("clear")
        
    print("Gracias por utilizar el sistema funerario. Cierre de sesión exitoso.")