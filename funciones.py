def mostrar_menu():
    print("\n--- Yoda's Snack ---")
    print("1. Agregar producto al inventario")
    print("2. Realizar una venta")
    print("3. Mostrar productos disponibles")
    print("4. Salir del sistema")
    
    #2. Agregar producto al inventario:
#Permitir al usuario agregar productos al inventario. Cada producto debe tener 
#un nombre, una cantidad disponible y un precio unitario.
#Los productos deben almacenarse en una lista.
#Ver la estructura del inventario al final de la consigna.
def agregar_producto(inventario):
        nombre = input("Ingrese el nombre del producto : ")
        cantidad =  int(input("Ingrese la cantidad disponible : "))
        precio = int(input("Ingrese el precio del producto por unidad : "))
        inventario.append([nombre, cantidad, precio])       
        return inventario

#3 Realizar una venta:
# Mostrar una lista de productos disponibles (nombre, precio y cantidad).
# El usuario podrá seleccionar un producto y la cantidad que desea comprar.
# Verificar que haya suficiente stock del producto seleccionado.
# Restar la cantidad comprada del inventario.
# Mostrar el total a pagar al cliente por la venta.
# Si no hay suficiente stock, mostrar un mensaje que indique que no se puede 
# realizar la venta
def mostrar_productos(inventario):
    print ("\---Productos Disponibles---")
    print (inventario)

def verificar_stock(stock, cantidad):
    if cantidad > stock :  
        venta_posible = False
    else:
        venta_posible = True            
    return venta_posible

def calcular_precio(cantidad, precio):
    precio_final = precio * cantidad
    return precio_final

def restar_stock(stock, cantidad):
    nuevo_stock = stock - cantidad
    return nuevo_stock

def realizar_venta(cantidad, inventario):
    mostrar_productos(inventario)
    producto = input("Ingrese el nombre del producto que desea comprar : ").lower()
    for i in inventario:
        for j in inventario[i]:
            if inventario[i][0] == producto:
                stock_producto = inventario[i][1]
                break
    cantidad = int(input("Ingrese la cantidad deseada : "))
    venta_posible = verificar_stock(stock_producto, cantidad)
    while venta_posible == False:
        cantidad = int(input("Cantidad mayor al stock, ingrese una menor cantidad : "))
        venta_posible = verificar_stock(stock_producto, cantidad)
