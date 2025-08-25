import math
from decimal import Decimal

# EJERCICIO 1
print('Ejercicio 1:');
saludo = "Hola Mundo!";

print(saludo)

# EJERCICIO 2
print('Ejercicio 2:');
nombre = input("Por favor, ingresa tu nombre: ");
saludo = f'hola {nombre}!';

print(saludo);

# EJERCICIO 3
print('Ejercicio 3:');
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = input('Ingrese su edad: ')
localidad = input('Ingrese su dirección: ')

print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {localidad}.')


# EJERCICIO 4
print('Ejercicio 4:');
radio = float(input('Ingrese el radio del círculo: '));
area = math.pi * (radio ** 2);
perimetro = 2 * math.pi * radio;

print(format(f'El área del círculo es: {area:.2f}'));
print(format(f'El perimetro del círculo es: {perimetro:.2f}'));


# EJERCICIO 5
print('Ejercicio 5:');
segundos = Decimal(input('Ingrese una cantidad determinada de segundos: '));
horas = Decimal(segundos / 3600);

print(format(f'La cantidad de segundos expresadas en horas es: {horas}'));


# EJERCICIO 6
print('Ejercicio 6:');
numero = int(input('Ingrese un número: '))

for i in range(0, numero + 1):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')


# EJERCICIO 7
print('Ejercicio 7:');
num1 = int(input('Ingrese un número entero distinto de 0: '))
num2 = int(input('Ingrese otro número entero distinto de 0: '))

while num1 == 0 or num2 == 0:
    print('Los números deben ser distintos de 0. Intente nuevamente.')
    num1 = int(input('Ingrese un número entero distinto de 0: '))
    num2 = int(input('Ingrese otro número entero distinto de 0: '))
    
suma = num1 + num2;
resta = num1 - num2;
multiplicacion = num1 * num2;
division = num1 / num2;

print(f'La suma de {num1} y {num2} es: {suma}')
print(f'La resta de {num1} y {num2} es: {resta}')
print(f'La multiplicacion entre {num1} y {num2} es: {multiplicacion}')
print(f'La division entre {num1} y {num2} es: {division}')


# EJERCICIO 8
print('Ejercicio 8:');
peso = float(input('Ingrese su peso en kg: '))
altura = float(input('Ingrese su altura en metros: '))

imc = peso / (altura ** 2)

print(f'El índice de masa corporal es: {imc:.2f}')


# EJERCICIO 9
print('Ejercicio 9:');
celcius = float(input('Ingrese la temperatura en grados Celsius: '))
fahrenheit = ((9/5) * celcius) + 32

print(f'La temperatura en grados Fahrenheit es: {fahrenheit:.2f}')


# EJERCICIO 10
print('Ejercicio 10:');
num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))
num3 = float(input('Ingrese el tercer número: '))

promedio = (num1 + num2 + num3) / 3

print(f'El promedio de los números ingresados es: {promedio:.2f}')