hemisferio = input('En que hemisferio se encuentra: ').lower()
mes = input('Ingrese el mes: ').lower()
dia = int(input('Ingrese el día: '))

if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):
    if hemisferio == 'norte':
        print('Verano')
    elif hemisferio == 'sur':
        print('Invierno')

elif (mes == "marzo" and dia >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20):
    if hemisferio == 'norte':
        print('Verano')
    elif hemisferio == 'sur':
        print('Invierno')

elif (mes == "junio" and dia >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20):
    if hemisferio == 'norte':
        print('Verano')
    elif hemisferio == 'sur':
        print('Invierno')

elif (mes == "septiembre" and dia >= 21) or mes == "octubre" or mes == "noviembre" or (mes == "diciembre" and dia <= 20):
    if hemisferio == 'norte':
        print('Verano')
    elif hemisferio == 'sur':
        print('Invierno')
else:
    print("Ingrese valores válidos")