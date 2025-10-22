# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#  una temperatura en grados Celsius y devuelva su equivalente en
#  Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#  resultado usando la función.

celsius = float(input('Ingrese la temperatura en grados Celsius: '))

def celsius_a_fahrenheit(c):
    f = (c * (9/5)) + 32
    return f

print(f'La temperatura expresada en grados Fahrenheit es: {celsius_a_fahrenheit(celsius)}')