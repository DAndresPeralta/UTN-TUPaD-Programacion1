# Crear una función llamada tabla_multiplicar(numero) que reciba un
#  número como parámetro y imprima la tabla de multiplicar de ese
#  número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción.

num = int(input('Ingrese un número para ver su tabla de multiplicar: '))

def tabla_multiplicar(numero):
    for i in range (1,11):
        resultado = numero * i
        print(f'{numero} X {i} = {resultado}')

tabla_multiplicar(num)        