# Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
# cantidad) y lo agregue al archivo sin borrar el contenido existente. 

def mostrarProductos(file):
    with open(file, "r") as archivo:
     for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre.strip()} | Precio: ${precio.strip()} | Cantidad: {cantidad.strip()}")

mostrarProductos("productos.txt")

producto = input("Ingrese el nombre del producto: ")
precio = input("Ingrese el precio del producto: ")
cantidad = input("Ingrese la cantidad del producto: ")

with open("productos.txt", "a") as archivo:
    archivo.write(f"{producto}, {precio}, {cantidad}\n")

mostrarProductos("productos.txt")