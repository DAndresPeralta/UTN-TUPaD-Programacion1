# Generar una lista con 15 números enteros al azar entre 1 y 100. 
# • Crear una lista con los pares y otra con los impares. 
# • Mostrar cuántos números tiene cada lista.

import random

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