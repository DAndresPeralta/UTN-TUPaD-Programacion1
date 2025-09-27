# Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
# • Mostrar el total vendido por cada producto. 
# • Mostrar el día con mayores ventas totales. 
# • Indicar cuál fue el producto más vendido en la semana. 

ventas = [
    [150,200,250,300,350,400,450],
    [100,150,200,250,300,350,400],
    [200,250,300,350,400,450,500],
    [50,100,150,200,250,300,350]
]

totalProducto = [sum(columna) for columna in zip(*ventas)]

print (f'Total vendido por producto: {totalProducto}')

diaMayorVenta = totalProducto.index(max(totalProducto))

print (f'El dia que más se vendio fue: {diaMayorVenta + 1}')

