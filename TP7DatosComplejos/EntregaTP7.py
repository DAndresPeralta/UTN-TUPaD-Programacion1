# 1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
# 1450} 
# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# ) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800 


precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#  Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# # precios.

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

frutas = list(precios_frutas.keys())

print(frutas)

#  Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe. 

contactos = {}
i = 0

for i in range(5):
    nombre = input('Ingrese el nombre del contacto: ')
    telefono = input('Ingrese el número de teléfono: ')
    contactos[nombre] = telefono
    i += 1

print(contactos)    

buscar = input('Ingrese el nombre del contacto que desea buscar: ')

if buscar in contactos:
    print(f'El número de {buscar} es {contactos[buscar]}')

# Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra.

cantidad = {}

frase = input('Ingresa una frase: ')

palabras = frase.split()
unicas = set(palabras)

print('Palabras únicas: ', unicas)

for palabra in palabras:
    if palabra in unicas:
        cantidad[palabra] = cantidad.get(palabra, 0) + 1

print('Cantidad de apariciones de cada palabra: ', cantidad)

# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno. 

alumnos = {}
i = 0
j = 0

for i in range(3):
    nombre = input('Ingrese el nombre del alumno: ')
    notas = []
    for j in range(3):
        nota = float(input(f'Ingrese la {j + 1}° nota de {nombre}: '))
        notas.append(nota);
        j += 1
    alumnos[nombre] = tuple(notas)
    i += 1

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f'El promedio del alumno {alumno} es: {promedio}')

#  Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

parcial1 = {60 , 72, 55, 85, 15, 63, 25}
parcial2 = {12, 55, 63, 85, 33, 25, 90}

aprobados1 = {nota for nota in parcial1 if nota >= 60}
aprobados2 = {nota for nota in parcial2 if nota >= 60}

ambos = aprobados1 & aprobados2
print("Aprobaron ambos parciales:", ambos)

soloUno = aprobados1 ^ aprobados2
print("Aprobaron solo uno de los dos:", soloUno)

alMenosUno = aprobados1 | aprobados2
print("Aprobaron al menos un parcial:", alMenosUno)


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


# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
# Ejemplo: Permití consultar qué actividad hay en cierto día y hora.

agenda ={
    ("Lunes", "11:15"): "Reunión con el equipo",
    ("Martes","15:00"): "Cita médico",
    ("Miercoles", "09:00"): "Clase de yoga",
    ("Miercoles", "12:00"): "Reunión semanal",
    ("Jueves", "16:00"): "Entrega proyecto",
}

dia = input('Ingrese el día de la semana para conocer sus actividades agendadas: ')
hora = input('Ingrese la hora: ')

if (dia, hora) in agenda:
    print(f'Actividad agendada para el {dia} a las {hora}: {agenda[(dia, hora)]}')
else:
    print(f'No hay actividades agendadas para el {dia} a las {hora}.')


# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores. 

capitales = {}

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción",
    "Perú": "Lima",
    "Bolivia": "La Paz",
    "Colombia": "Bogotá",
    "Ecuador": "Quito",
    "Venezuela": "Caracas",
    "México": "Ciudad de México",
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma",
    "Alemania": "Berlín",
    "Reino Unido": "Londres",
    "Estados Unidos": "Washington D.C.",
    "Canadá": "Ottawa",
    "Japón": "Tokio",
    "China": "Pekín"
}

capitales = {capital: pais for pais, capital in paises.items()}
print('Diccionario invertido')
print(capitales)