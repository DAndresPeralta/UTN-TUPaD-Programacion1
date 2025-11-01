# Guardar los productos actualizados: Después de haber leído, buscado o agregado 
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
# productos actualizados desde la lista. 

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

with open("productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")