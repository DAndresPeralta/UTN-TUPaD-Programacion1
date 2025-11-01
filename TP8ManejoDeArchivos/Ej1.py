# Crear archivo inicial con productos: Crear un archivo de texto llamado 
# productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad 

products = ["Manzana, 1500, 50", "Pera, 1200, 30", "Limon, 800, 20"]

with open("productos.txt", "w") as archivo:
    for product in products:
        archivo. write(product + "\n")