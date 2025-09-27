# Crear una lista con las notas de 10 estudiantes. 
# • Mostrar la lista completa. 
# • Calcular y mostrar el promedio. 
# • Indicar la nota más alta y la más baja. 

notas = [85,77,55,69,71,91,100,83,77,34]
print("Lista completa de notas: ", notas)

promedio = sum(notas)/len(notas)
print("El promedio de notas de el curso es: ", promedio)

notaMayor = max(notas)
print("La nota mas alta del curso es: ", notaMayor)