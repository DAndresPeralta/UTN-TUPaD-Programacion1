# Crear una lista con los nombres de 8 estudiantes presentes en clase. 
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
# • Mostrar la lista final actualizada. 

alumnos = ['Ana', 'Luis', 'Carla', 'Jorge', 'Marta', 'Diego', 'Sofia', 'Pedro']

opcion = input('Desea agregar un nuevo estudiante (A) o eliminar uno existente (E)?')

if opcion.upper() == 'A':
    nuevoAlumno = input('Ingrese el nombre: ')
    alumnos.append(nuevoAlumno)

    print(f"La nueva lista de estudiantes es: {alumnos}")
elif opcion.upper() == 'E':
    alumnoEliminar = input('Ingrese el nombre del estudiante que desea eliminar: ')
    if alumnoEliminar in alumnos:
        alumnos.remove(alumnoEliminar)
        print(f"La nueva lista de estudiantes es: {alumnos}")
    else:
        print("El estudiante no se encuentra en la lista.")
else:
    print("Opción inválida.")
    print(f"La lista de estudiantes es: {alumnos}")