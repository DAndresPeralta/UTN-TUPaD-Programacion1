# Crear una matriz con las notas de 5 estudiantes en 3 materias. 
# • Mostrar el promedio de cada estudiante. 
# • Mostrar el promedio de cada materia. 

notas = [
    [80,65,90],
    [75,80,55],
    [70,91,75],
    [92,52,75],
    [84,45,70]
]

promedioAlumno = [sum(fila)/len(fila) for fila in notas];

for i in range(len(promedioAlumno)):
    print(f"Estudiante {i+1} → promedio: {promedioAlumno[i]}")

promedioMateria = [sum(col)/len(col) for col in zip(*notas)]

print(f"Promedio por materias: {promedioMateria}")