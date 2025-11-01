# Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
# una lista llamada productos, donde cada elemento sea un diccionario con claves: 
# nombre, precio, cantidad. 

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
