# Crear una función llamada operaciones_basicas(a, b) que reciba
#  dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))

def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b)

suma, resta, multiplicacion, division = operaciones_basicas(num1, num2)

print(f'La suma es: {suma}')
print(f'La resta es: {resta}')
print(f'La multiplicacion es: {multiplicacion}')
print(f'La division es: {division}')