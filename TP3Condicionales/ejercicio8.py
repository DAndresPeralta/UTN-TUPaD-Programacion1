# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Por favor, ingresa tu nombre: ");
opcion = int(input("Ingrese una opción para convertir su nombre a: 1 para mayusculas, 2 para minusculas, 3 para primera letra mayuscula: "));

if opcion == 1:
    print(nombre.upper());
elif opcion == 2:
    print(nombre.lower());
elif opcion == 3:
    print(nombre.title());
else:
    while opcion < 1 or opcion > 3:
        print("Opción inválida. Por favor, ingrese 1, 2 o 3.");
        opcion = int(input("Ingrese una opción para convertir su nombre a: 1 para mayusculas, 2 para minusculas, 3 para primera letra mayuscula: "));
        if opcion == 1:
            print(nombre.upper());
        elif opcion == 2:
            print(nombre.lower());
        elif opcion == 3:
            print(nombre.title());