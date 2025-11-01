# Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
# no existe, mostrar un mensaje de error.

productos = []

with open("productos.txt", "r") as archivo:
    
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")

        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }

        productos.append(producto)

for producto in productos:
    print(producto)


productoBuscado = input("Ingrese el nombre del producto a buscar: ")
encontrado = None

for producto in productos:
    if producto['nombre'].strip().lower() == productoBuscado.strip().lower():
        encontrado = producto
        break

if encontrado:
    print("Producto encontrado:", encontrado)
else:
    print("No se encontró el producto")