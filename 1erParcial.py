titulos = []

cantidades = []
opcion = 0

print(f"Bienvenido al sistema de gestión de librerias UTN")
print()

while opcion != 8:

    print("================================")
    print(f'MENU PRINCIPAL')
    print()

    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")
    print()
    print("================================")

    opcion = int(input("Selecciona una opción (1-8): "))

    if opcion < 1 or opcion > 8:
        print('Opción inváliada. Ingrese una opción del 1 al 8.')

    match opcion:
        case 1:

            nuevoTitulo = ""
            cantidad = 0
            exist = False

            while nuevoTitulo == "" or cantidad < 0:

                print("Ingresar títulos")
                print()
                nuevoTitulo = input('Ingrese el título del libro: ')

                if nuevoTitulo == "":
                    print('El título no puede estar vacío. Intente nuevamente.')
                    continue

                cantidad = int(input('Ingrese la cantidad inicial de ejemplares: '))

                if cantidad < 0:
                    print('La cantidad no puede ser inferior a 0. Intente nuevamente.')
                    continue
            
                print()

                for i in range(len(titulos)):
                    if titulos[i].lower() == nuevoTitulo.lower():
                            print('El título ya existe e el catálogo. Intente nuevamente.')
                            exist = True
                            break
                    
                if exist:
                    continue

                titulos.append(nuevoTitulo)
                cantidades.append(cantidad)
                print(f'Se ha agregado el título "{nuevoTitulo}" con {cantidad} ejemplares.')

        case 2: 

            tituloABuscar = ""
            cantidadAgregar = 0

            while tituloABuscar == "" or cantidadAgregar < 0:

                print(titulos)
                print("Ingresar ejemplares")
                print()

                tituloABuscar = input('Ingrese el título del libro al que desea agregar ejemplares: ')
                if tituloABuscar == "":
                    print('El título no puede estar vacío. Intente nuevamente.')
                    continue
                print()

                for i in range(len(titulos)):
                    if titulos[i].lower() == tituloABuscar.lower():
                        cantidadAgregar = int(input('Ingrese la cantidad de ejemplares a agregar: '))

                        if cantidadAgregar < 0:
                            print('La cantidad no puede ser inferior a 0. Intente nuevamente.')
                            continue

                        cantidades[i] = cantidades[i] + cantidadAgregar
                        print(f'Se agregaron los ejemplares con éxito')
                        break
                else:
                    print('El título no se encuentra en el catálogo.')             

        case 3:
            print("Mostrar catálogo")
            print()
                
            print(titulos)
            print(cantidades)

        case 4:

            tituloABuscar = ""

            while tituloABuscar == "":

                print('Consultar disponibilidad')
                print()
                tituloABuscar = input('Ingrese el título del libro que desea consultar: ')

                if tituloABuscar == "":
                    print('El título no puede estar vacío. Intente nuevamente.')
                    continue
                
                print()

                for i in range(len(titulos)):
                    if titulos[i].lower() == tituloABuscar.lower():
                        index = i
                        cantidad = cantidades[index]
                        print(f'El título "{titulos[index]}" tiene {cantidad} ejemplares disponibles.')
                        break
                else:
                    print('El título no se encuentra en el catálogo.')

        case 5:
            agotados = []

            print('Listar agotados')
            print()

            for i in range(len(cantidades)):
                if cantidades[i] == 0:
                    agotados = titulos[i]
            
            print('los títulos agotados son: ')
            print(agotados)

        case 6: 
            print('Agregar título')
            nuevoTitulo = ""
            cantidad = 0

            while nuevoTitulo == "" or cantidad < 0:

                print("Ingresar títulos")
                print()
                nuevoTitulo = input('Ingrese el título del libro: ')

                if nuevoTitulo == "":
                    print('El título no puede estar vacío. Intente nuevamente.')
                    continue

                cantidad = int(input('Ingrese la cantidad inicial de ejemplares: '))

                if cantidad < 0:
                    print('El título no puede estar vacío. Intente nuevamente.')
                    continue
            
                print()

                titulos.append(nuevoTitulo)
                cantidades.append(cantidad)
                print(f'Se ha agregado el título "{nuevoTitulo}" con {cantidad} ejemplares.')

        case 7:
            opcionActualizar = 0
            tituloABuscar = ""

            print("================================")
            print()
            print(f'ACTUALIZACION DE EJEMPLARES')
            print("1. Préstamo")
            print("2. Devolución")
            print("3. Salir")

            while opcionActualizar < 1 or opcionActualizar > 3:

                opcionActualizar = int(input('Ingrese la opción deseada (1-3): '))

                if opcionActualizar == 1:
                    print('Prestamo de ejemplares')

                    while tituloABuscar == "":

                        tituloABuscar = input('Ingrese el título a dar en préstamo: ')

                        if tituloABuscar == "":
                            print('El título no puede estar vacío. Intente nuevamente.')
                            continue

                        for i in range(len(titulos)):
                            if titulos[i].lower() == tituloABuscar.lower():
                                if cantidades[i] > 0:
                                    cantidades[i] = cantidades[i] - 1
                                    print(f'Se ha realizado el préstamo del título exitosamente')
                                else:
                                    print('No hay ejemplares disponibles')

                elif opcionActualizar == 2:
                    print('Devolución de ejemplares')

                    while tituloABuscar == "":

                        tituloABuscar = input('Ingrese el título a devolver: ')

                        if tituloABuscar == "":
                            print('El título no puede estar vacío. Intente nuevamente.')
                            continue

                        for i in range(len(titulos)):
                            if titulos[i].lower() == tituloABuscar.lower():
                                cantidades[i] = cantidades[i] + 1
                                print(f'Se ha realizado la devolución del título exitosamente')  

                elif opcionActualizar == 3:
                    print('Salir')
                    break                 

        case 8:
            print('Salir')
            print()
            print('Gracias por usar el sistema de gestión de librerías UTN. ¡Hasta luego!')
            break
