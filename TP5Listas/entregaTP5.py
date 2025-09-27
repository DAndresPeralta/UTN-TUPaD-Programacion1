# Crear una lista con las notas de 10 estudiantes. 
# • Mostrar la lista completa. 
# • Calcular y mostrar el promedio. 
# • Indicar la nota más alta y la más baja. 

import random

notas = [85,77,55,69,71,91,100,83,77,34]
print("Lista completa de notas: ", notas)

promedio = sum(notas)/len(notas)
print("El promedio de notas de el curso es: ", promedio)

notaMayor = max(notas)
print("La nota mas alta del curso es: ", notaMayor)

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


    # Generar una lista con 15 números enteros al azar entre 1 y 100. 
# • Crear una lista con los pares y otra con los impares. 
# • Mostrar cuántos números tiene cada lista.

numeros = []
cantidad = 15
pares = []
impares = []

for i in range(cantidad):
    numero = random.randint(1, 100)
    numeros.append(numero)

print(f"Lista de numeros: {numeros}")

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    elif numero % 2 != 0:
        impares.append(numero)

print(f"Lista de numeros pares: {pares}")
print(f"Lista de numeros impares: {impares}")

# Crear una nueva lista sin elementos repetidos. 
# • Mostrar el resultado. 

datos = [1,3,5,3,7,1,9,5,3]
nuevaLista = set(datos)
print("Lista sin elementos repetidos: ", list(nuevaLista))

# Crear una lista con los nombres de 8 estudiantes presentes en clase. 
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
# • Mostrar la lista final actualizada. 

alumnos = ['Ana', 'Luis', 'Carla', 'Jorge', 'Marta', 'Diego', 'Sofia', 'Pedro']

opcion = input('Desea agregar un nuevo estudiante (A) o eliminar uno existente (E)?')

if opcion.upper() == 'A':
    nuevoAlumno = input('Ingrese el nombre: ')
    alumnos.append(nuevoAlumno)

    print(f"La nueva lista de estudiantes es: {alumnos}")
elif opcion.upper() == 'E':
    alumnoEliminar = input('Ingrese el nombre del estudiante que desea eliminar: ')
    if alumnoEliminar in alumnos:
        alumnos.remove(alumnoEliminar)
        print(f"La nueva lista de estudiantes es: {alumnos}")
    else:
        print("El estudiante no se encuentra en la lista.")
else:
    print("Opción inválida.")
    print(f"La lista de estudiantes es: {alumnos}")

# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
# último pasa a ser el primero).

numeros = [1, 2, 3, 4, 5, 6, 7]

ultimo = numeros.pop()    
numeros.insert(0, ultimo)   

print(numeros)

# Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
# semana. 
# • Calcular el promedio de las mínimas y el de las máximas. 
# • Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [
    [13,22],
    [14,24],
    [7,19],
    [12,18],
    [20,24],
    [11,27],
    [10,25],
]

minimas = [temp[0] for temp in temperaturas]
maximas = [temp[1] for temp in temperaturas]

promMinimas = sum(minimas)/len(minimas)
promMaximas = sum(maximas)/len(maximas)

print(f"Promedio de temperaturas mínimas: {promMinimas:.2f}")
print(f"Promedio de temperaturas máximas: {promMaximas:.2f}")

amplitudes = [maximas[i] - minimas[i] for i in range(len(temperaturas))]

diaMayorAmplitud = amplitudes.index(max(amplitudes)) + 1

print(f"El día con mayor amplitud térmica es {diaMayorAmplitud}")


# Crear una matriz con las notas de 5 estudiantes en 3 materias. 
# • Mostrar el promedio de cada estudiante. 
# • Mostrar el promedio de cada materia. 

notas = [
    [80,65,90],
    [75,80,55],
    [70,91,75],
    [92,52,75],
    [84,45,70]
]

promedioAlumno = [sum(fila)/len(fila) for fila in notas];

for i in range(len(promedioAlumno)):
    print(f"Estudiante {i+1} → promedio: {promedioAlumno[i]}")

promedioMateria = [sum(col)/len(col) for col in zip(*notas)]

print(f"Promedio por materias: {promedioMateria}")

# Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
# • Inicializarlo con guiones "-" representando casillas vacías. 
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
# • Mostrar el tablero después de cada jugada. 

tablero = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

jugador1 = 'X'
jugador2 = 'O'

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

mostrar_tablero(tablero)

for turno in range(9):
    if turno % 2 == 0:
        jugador = jugador1
    else:
        jugador = jugador2

    fila = int(input(f"Turno del jugador {jugador}, ingrese la fila (0-2): "))
    columna = int(input(f"Turno del jugador {jugador}, ingrese la columna (0-2): "))

    if tablero[fila][columna] == '-':
        tablero[fila][columna] = jugador
    else:
        print("Casilla ya ocupada, intente de nuevo.")

    mostrar_tablero(tablero)

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

