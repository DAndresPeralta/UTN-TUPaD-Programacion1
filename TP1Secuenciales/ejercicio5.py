# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
# cuántas horas equivale. 

from decimal import Decimal

segundos = Decimal(input('Ingrese una cantidad determinada de segundos:'));
horas = Decimal(segundos / 3600);

print(format(f'La cantidad de segundos expresadas en horas es: {horas}'));