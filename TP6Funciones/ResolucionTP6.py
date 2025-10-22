# Crear una función llamada imprimir_hola_mundo que imprima por
#  pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#  programa principal.

print('EJERCICIO 1')

import math

def imprimir_hola_mundo():
    print('Hola Mundo!')

imprimir_hola_mundo();

print('---------------')

# Crear una función llamada saludar_usuario(nombre) que reciba
#  como parámetro un nombre y devuelva un saludo personalizado.
#  Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
#  principal solicitando el nombre al usuario.

print('EJERCICIO 2')

alumno = 'Andrés'

def saludar_usuario(nombre):
    return (f'Bienvenido a la UTN {nombre}!')

print(saludar_usuario(alumno))

print('---------------')

# Crear una función llamada informacion_personal(nombre, apellido,
#  edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#  [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
# dir los datos al usuario y llamar a esta función con los valores in
# gresados.

print('EJERCICIO 3')

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = input('Ingrese su edad: ')
residencia = input('Ingrese su residencia: ')

def informacion_personal(nombre, apellido, edad, residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')


informacion_personal(nombre, apellido, edad, residencia)

print('---------------')

# Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.

print('EJERCICIO 4')

radio = float(input('Ingrese el radio del círculo: '))

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f'El area del círculo es: {area}')
print(f'El perimetro del círculo es: {perimetro}')

print('---------------')

# Crear una función llamada segundos_a_horas(segundos) que reciba
#  una cantidad de segundos como parámetro y devuelva la cantidad
#  de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.

print('EJERCICIO 5')

segundos = int(input('Ingrese la cantidad de segundos: '))

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

print(f'La cantidad de horas es: {segundos_a_horas(segundos)}')

print('---------------')

# Crear una función llamada tabla_multiplicar(numero) que reciba un
#  número como parámetro y imprima la tabla de multiplicar de ese
#  número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción.

print('EJERCICIO 6')

num = int(input('Ingrese un número para ver su tabla de multiplicar: '))

def tabla_multiplicar(numero):
    for i in range (1,11):
        resultado = numero * i
        print(f'{numero} X {i} = {resultado}')

tabla_multiplicar(num)        

print('---------------')

# Crear una función llamada operaciones_basicas(a, b) que reciba
#  dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

print('EJERCICIO 7')

num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))

def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b)

suma, resta, multiplicacion, division = operaciones_basicas(num1, num2)

print(f'La suma es: {suma}')
print(f'La resta es: {resta}')
print(f'La multiplicacion es: {multiplicacion}')
print(f'La division es: {division}')

print('---------------')

# Crear una función llamada calcular_imc(peso, altura) que reciba el
#  peso en kilogramos y la altura en metros, y devuelva el índice de
#  masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.

print('EJERCICIO 8')

peso = float(input('Ingrese su peso: '))
altura = float(input('Ingrese su altura en mts: '))

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

imc = calcular_imc(peso, altura)

print(f'Su indice de masa corporal (IMC) es: {imc}')

print('---------------')

# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#  una temperatura en grados Celsius y devuelva su equivalente en
#  Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#  resultado usando la función.

print('EJERCICIO 9')

celsius = float(input('Ingrese la temperatura en grados Celsius: '))

def celsius_a_fahrenheit(c):
    f = (c * (9/5)) + 32
    return f

print(f'La temperatura expresada en grados Fahrenheit es: {celsius_a_fahrenheit(celsius)}')

print('---------------')

# Crear una función llamada calcular_promedio(a, b, c) que reciba
#  tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta
#  función.

print('EJERCICIO 10')

a = float(input('Ingrese el primer valor: '))
b = float(input('Ingrese el segundo valor: '))
c = float(input('Ingrese el tercer valor: '))

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

print(f'El promedio de los tres números es: {calcular_promedio(a, b, c)}')

print('---------------')