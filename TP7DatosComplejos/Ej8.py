# Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario: 
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe. 

stock = {
"Notebooks": 25,
"Monitores": 15,
"Teclados": 30,
"Mouse":5
}

print('Menu')
print('1- Consultar stock de un producto')
print('2- Agregar unidades al stock de un producto existente')
print('3- Agregar un nuevo producto')
print('4- Salir')

opcion = int(input('Ingrese una opcion: '))

while opcion <5 or opcion > 0:
    if opcion == 1:
        productoConsulta = input('Ingrese el nombre del producto: ')
        if productoConsulta in stock:
            print(f'El stock de {productoConsulta} es {stock[productoConsulta]} unidades.')
        else:
            print('El producto ingresado no existe en el stock')

    elif opcion == 2:
        productoAgregarUnidades = input('Ingrese el nombre del producto: ')
        if productoAgregarUnidades in stock:
            unidadesAgregar = int(input('Ingrese la cantidad de unidades a agregar: '))
            stock[productoAgregarUnidades] += unidadesAgregar
            print(f'se han agredado {unidadesAgregar} unidades')
            print(f'Nuevo stock: {productoAgregarUnidades} = {stock[productoAgregarUnidades]}')
        else:
            print('El producto ingresado no existe en el stock')

    elif opcion == 3:
        nuevoProducto = input('Ingrese el nombre del nuevo producto: ')
        if nuevoProducto not in stock:
            unidadesNuevoProducto = int(input('Ingrese las unidades a agregar: '))
            stock[nuevoProducto] = unidadesNuevoProducto
            print(f'Se ha agregado el producto {nuevoProducto} con {unidadesNuevoProducto} unidades al stock.')
        else:
            print('El producto ya existe en el stock')

    elif opcion == 4:
            print('Muchas Gracias')
            break