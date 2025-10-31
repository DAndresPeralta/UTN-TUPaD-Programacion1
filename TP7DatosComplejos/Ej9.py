# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
# Ejemplo: Permití consultar qué actividad hay en cierto día y hora.

agenda ={
    ("Lunes", "11:15"): "Reunión con el equipo",
    ("Martes","15:00"): "Cita médico",
    ("Miercoles", "09:00"): "Clase de yoga",
    ("Miercoles", "12:00"): "Reunión semanal",
    ("Jueves", "16:00"): "Entrega proyecto",
}

dia = input('Ingrese el día de la semana para conocer sus actividades agendadas: ')
hora = input('Ingrese la hora: ')

if (dia, hora) in agenda:
    print(f'Actividad agendada para el {dia} a las {hora}: {agenda[(dia, hora)]}')
else:
    print(f'No hay actividades agendadas para el {dia} a las {hora}.')