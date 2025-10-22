# Crear una función llamada calcular_imc(peso, altura) que reciba el
#  peso en kilogramos y la altura en metros, y devuelva el índice de
#  masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.

peso = float(input('Ingrese su peso: '))
altura = float(input('Ingrese su altura en mts: '))

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

imc = calcular_imc(peso, altura)

print(f'Su indice de masa corporal (IMC) es: {imc}')
