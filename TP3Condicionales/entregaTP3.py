import random 
from statistics import mode, median, mean

#1
edad = input(int('Ingrese su edad'))

if edad >= 18:
    print('Eres mayor de edad')

#2
nota = input(int('Ingrese su nota'));

if nota >= 6:
    print('Aprobado');
else:
    print('Desaprobado');

#3
numero = int(input('Ingrese un numero: '));

if (numero % 2) == 0:
    print("Ha ingresado un número par")
else:
    while (numero % 2) != 0:
        print("Por favor, ingrese un número par")
        numero = int(input('Ingrese un numero: '))
    
#4
edad = int(input('Ingrese su edad: '));

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#5
password = input('Ingrese su contraseña: ');

if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")

#7
frase = input('Ingrese una frase o palabra: ');

if frase[-1].lower() in 'aeiou':
    frase += "!"
    print(frase)
else:
    print(frase)

#8
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

#9
magnitud = int(input('Ingresa la magnitud del terremoto: '));

if magnitud < 3:
    print('"Muy leve" (imperceptible)')
elif magnitud >= 3 and magnitud < 4:
    print('"Leve" (ligeramente perceptible)')
elif magnitud >= 4 and magnitud < 5:
    print('"Moderado" (sentido por personas, pero generalmente no causa daños)')
elif magnitud >= 5 and magnitud < 6:
    print('"Fuerte" (puede causar daños en estructuras débiles)')
elif magnitud >= 6 and magnitud < 7:
     print('"Muy Fuerte" (puede causar daños significativos)')
elif magnitud >= 7:
    print('"Extremo" (puede causar graves daños a gran escala)')

#10
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