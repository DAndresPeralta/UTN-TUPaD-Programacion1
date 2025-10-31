# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno. 

alumnos = {}
i = 0
j = 0

for i in range(3):
    nombre = input('Ingrese el nombre del alumno: ')
    notas = []
    for j in range(3):
        nota = float(input(f'Ingrese la {j + 1}° nota de {nombre}: '))
        notas.append(nota);
        j += 1
    alumnos[nombre] = tuple(notas)
    i += 1

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f'El promedio del alumno {alumno} es: {promedio}')