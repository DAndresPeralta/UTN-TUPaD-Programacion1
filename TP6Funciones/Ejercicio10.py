# Crear una función llamada calcular_promedio(a, b, c) que reciba
#  tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta
#  función.

a = float(input('Ingrese el primer valor: '))
b = float(input('Ingrese el segundo valor: '))
c = float(input('Ingrese el tercer valor: '))

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

print(f'El promedio de los tres números es: {calcular_promedio(a, b, c)}')