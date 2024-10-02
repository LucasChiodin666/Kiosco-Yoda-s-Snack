##Equipo número 21. Integrantes: Sterba Valentin y Chiodin Lucas Ezequiel
from funciones import *

inventario = [
    ["chupetin sable de luz", 50, 200],
    ["agua la fuerza", 35, 3200],
    ["gomitas holocubo", 25, 990],
    ["barrita de cereal wookiee", 48, 2500],
    ["galletitas r2d2", 20, 15800],
]

seguir = True

while (seguir == True):
    print("\n--- Yoda's Snack ---")
    print("1. Agregar producto al inventario")
    print("2. Realizar una venta")
    print("3. Mostrar productos disponibles")
    print("4. Salir del sistema")

    opcion = input("Ingrese una de las opciones: ")
    opcion_valida = validar_opcion(opcion)

    while (opcion_valida == False):
        opcion = input("Opción Iválida. Ingrésela nuevamente: ")
        opcion_valida = validar_opcion(opcion)
    
    match opcion:
        case "1":
            mostrar_productos(inventario)
            agregar_producto(inventario)
            mostrar_productos(inventario)
        case "2":
            realizar_venta(inventario)
        case "3":
            mostrar_productos(inventario)
        case "4":
            print("¡Gracias por su compra!")
            seguir = False