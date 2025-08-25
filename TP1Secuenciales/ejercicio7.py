# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

num1 = int(input('Ingrese un número entero distinto de 0:'))
num2 = int(input('Ingrese otro número entero distinto de 0:'))

while num1 == 0 or num2 == 0:
    print('Los números deben ser distintos de 0. Intente nuevamente.')
    num1 = int(input('Ingrese un número entero distinto de 0:'))
    num2 = int(input('Ingrese otro número entero distinto de 0:'))
    
suma = num1 + num2;
resta = num1 - num2;
multiplicacion = num1 * num2;
division = num1 / num2;

print(f'La suma de {num1} y {num2} es: {suma}')
print(f'La resta de {num1} y {num2} es: {resta}')
print(f'La multiplicacion entre {num1} y {num2} es: {multiplicacion}')
print(f'La division entre {num1} y {num2} es: {division}')
