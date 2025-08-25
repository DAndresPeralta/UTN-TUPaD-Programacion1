# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número. 

numero = int(input('Ingrese un número: '))

for i in range(0, numero + 1):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
