def mostrarProductos(file):
    with open(file, "r") as archivo:
     for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre.strip()} | Precio: ${precio.strip()} | Cantidad: {cantidad.strip()}")

# Crear archivo inicial con productos: Crear un archivo de texto llamado 
# productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad 
print("Ejercicio 1")

products = ["Manzana, 1500, 50", "Pera, 1200, 30", "Limon, 800, 20"]

with open("productos.txt", "w") as archivo:
    for product in products:
        archivo. write(product + "\n")


print("\n")

# Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
# formato: Producto: Lapicera | Precio: $120.5 | Cantidad: 30 
print("Ejercicio 2")
print("\n")

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre.strip()} | Precio: ${precio.strip()} | Cantidad: {cantidad.strip()}")

print("\n")

# Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
# cantidad) y lo agregue al archivo sin borrar el contenido existente. 
print("Ejercicio 3")
print("\n")

mostrarProductos("productos.txt")

producto = input("Ingrese el nombre del producto: ")
precio = input("Ingrese el precio del producto: ")
cantidad = input("Ingrese la cantidad del producto: ")

with open("productos.txt", "a") as archivo:
    archivo.write(f"{producto}, {precio}, {cantidad}\n")

mostrarProductos("productos.txt")

print("\n")


# Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
# una lista llamada productos, donde cada elemento sea un diccionario con claves: 
# nombre, precio, cantidad. 
print("Ejercicio 4")
print("\n")

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

print("\n")


# Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
# no existe, mostrar un mensaje de error.
print("Ejercicio 5")
print("\n")

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

print("\n")


# Guardar los productos actualizados: Después de haber leído, buscado o agregado 
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
# productos actualizados desde la lista. 
print("Ejercicio 6")
print("\n")

with open("productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")

mostrarProductos("productos.txt")