#  Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe. 

contactos = {}
i = 0

for i in range(5):
    nombre = input('Ingrese el nombre del contacto: ')
    telefono = input('Ingrese el número de teléfono: ')
    contactos[nombre] = telefono
    i += 1

print(contactos)    

buscar = input('Ingrese el nombre del contacto que desea buscar: ')

if buscar in contactos:
    print(f'El número de {buscar} es {contactos[buscar]}')