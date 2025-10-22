# Crear una función llamada segundos_a_horas(segundos) que reciba
#  una cantidad de segundos como parámetro y devuelva la cantidad
#  de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.

segundos = int(input('Ingrese la cantidad de segundos: '))

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

print(f'La cantidad de horas es: {segundos_a_horas(segundos)}')