#  Pedir al usuario que cargue 5 productos en una lista. 
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []
cantidad = 5

for i in range(cantidad):
    producto = input('Ingrese el nombre del producto: ')
    productos.append(producto)

print(f"Lista de productos ordenada: {sorted(productos)}")

productoEliminar = input('Ingrese el nombre del producto que desea eliminar: ')

if productoEliminar in productos:
    productos.remove(productoEliminar)
    print("Producto eliminado. Lista actualizada: ", productos)
else:
    print("El producto no se encuentra en la lista.")
