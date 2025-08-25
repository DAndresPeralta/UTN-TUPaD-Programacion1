# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
# modo: 

peso = float(input('Ingrese su peso en kg: '))
altura = float(input('Ingrese su altura en metros: '))

imc = peso / (altura ** 2)

print(f'El índice de masa corporal es: {imc:.2f}')