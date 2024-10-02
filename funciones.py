def validar_opcion(opcion: str) -> bool:
    if (opcion != "1") and (opcion != "2") and (opcion != "3") and (opcion != "4"):
        opcion_valida = False
    else:
        opcion_valida = True
    return opcion_valida

def validar_producto(inventario: list[list], nombre: str) -> bool:
    elemento_encontrado = False
    for i in range(len(inventario)):
        for j in range(len(inventario[i])):
            if (inventario[i][0] == nombre):
                elemento_encontrado = True
                break
    return elemento_encontrado

def validar_cantidad(cantidad: int) -> bool:
    if (cantidad < 1):
        cantidad_valida = False
    else:
        cantidad_valida = True
    return cantidad_valida

def agregar_producto(inventario: list[list]) -> list[list]:
        nombre = input("Ingrese el nombre del producto : ").lower()
        elemento_encontrado = validar_producto(inventario, nombre)

        while (elemento_encontrado == True):
            nombre = input("El elemento ingresado ya se encuentra en el inventario. Ingrese algo diferente: ").lower()
            elemento_encontrado = validar_producto(inventario, nombre)

        cantidad =  int(input("Ingrese la cantidad disponible: "))
        cantidad_valida = validar_cantidad(cantidad)

        while (cantidad_valida == False):
            cantidad =  int(input("Cantidad Inválida. Ingrese un valor mayor a 0: "))
            cantidad_valida = validar_cantidad(cantidad)
        
        precio = int(input("Ingrese el precio del producto por unidad: "))
        inventario.append([nombre, cantidad, precio])       
        return inventario

def mostrar_productos(inventario: list[list]):
    print ("\n---Productos Disponibles---")
    for i in range(len(inventario)):
        print(inventario[i])

def verificar_stock(stock: int, cantidad: int) -> bool:
    if cantidad > stock :  
        venta_posible = False
    else:
        venta_posible = True            
    return venta_posible

def calcular_precio(cantidad: int, precio: int) -> int:
    precio_final = precio * cantidad
    return precio_final

def restar_stock(stock: int, cantidad: int) -> int:
    nuevo_stock = stock - cantidad
    return nuevo_stock

def realizar_venta(inventario: list[list]) -> list[list]:
    mostrar_productos(inventario)
    producto = input("Ingrese el nombre del producto que desea comprar: ").lower()
    producto_encontrado = validar_producto(inventario, producto)

    while (producto_encontrado == False):
        producto = input("Producto No Encontrado. Asegúrese de seleccionar un producto del inventario: ").lower()
        producto_encontrado = validar_producto(inventario, producto)

    for i in range(len(inventario)):
        for j in range(len(inventario[i])):
            if inventario[i][0] == producto:
                stock_producto = inventario[i][1]
                precio_unidad = inventario[i][2]
                posicion = i
                break
            break
    cantidad = int(input("Ingrese la cantidad deseada: "))
    venta_posible = verificar_stock(stock_producto, cantidad)
    while (venta_posible == False):
        cantidad = int(input("Cantidad mayor al stock, ingrese una menor cantidad: "))
        venta_posible = verificar_stock(stock_producto, cantidad)   

    precio_final = calcular_precio(cantidad, precio_unidad)
    print(f"Total a Pagar: ${precio_final}.")

    nuevo_stock = restar_stock(stock_producto, cantidad)
    inventario[posicion][1] = nuevo_stock
    return inventario