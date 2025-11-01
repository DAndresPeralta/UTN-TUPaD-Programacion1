# Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
# formato: Producto: Lapicera | Precio: $120.5 | Cantidad: 30 

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre.strip()} | Precio: ${precio.strip()} | Cantidad: {cantidad.strip()}")