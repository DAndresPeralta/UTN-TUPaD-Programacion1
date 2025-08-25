# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 

celcius = float(input('Ingrese la temperatura en grados Celsius: '))
fahrenheit = ((9/5) * celcius) + 32

print(f'La temperatura en grados Fahrenheit es: {fahrenheit:.2f}')