#  Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 
import random;

for i in range(0,101,2):
    print(i)

# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 

num2 = int(input('Ingrese un número '));
contador2 = 0;

while num2 > 0:
    num2 = num2 // 10;
    contador2 = contador2 + 1;

print(f"El número ingreso tiene {contador2} dígitos.")

#  Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 

num13 = int(input('Ingrese el primer número: '));
num23 = int(input('Ingrese el segundo número: '));
suma3 = 0;

for i in range (num13 + 1, num23):
    suma3 = suma3 + i;

print(f"La suma de los números comprendidos entre {num13} y {num23} es: {suma3}")

# Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 

num4 = 1;
suma4 = 0;

while num4 != 0:
    num4 = int(input('Ingrese un número: '));
    suma4 = suma4 + num4;

print(f"La suma de los números ingresados es {suma4}")

# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

randomNum5 = random.randint(0, 9);
intentos5 = 0;
num5 = -1;

while randomNum5 != num5:
    num5 = int(input('Cual es el número secreto: '));
    if (num5 < 0 or num5 > 9):
        print(f"Ingrese un número comprendido entre 0 y 9");
        continue;
    intentos5 = intentos5 + 1

print(f"Acertaste!!!")
print(f"El número secreto es {randomNum5}, usted intento {intentos5} veces")


# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.

for i in range(98 ,0 , -2):
    print(i)

# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

num17 = 0;
num27 = int(input("Ingrese un número positivo: "));
suma7 = 0;

num27 = abs(num27);

for i in range(num27):
    suma7 = suma7 + i;

print(f"La suma de los números comprendidos entre {num17} y {num27} es: {suma7}")

#  Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

num8 = 0;
pares8 = 0;
impares8 = 0;
positivos8 = 0;
negativos8 = 0;

print(f"Ingrese 100 números")

for i in range(100):
    num8 = int(input())

    if (num8 % 2 == 0 and num8 > 0):
        pares8 = pares8 + 1;
        positivos8 = positivos8 + 1;
    elif (num8 % 2 != 0 and num8 > 0):
        impares8 = impares8 + 1;
        positivos8 = positivos8 + 1;
    elif (num8 % 2 == 0 and num8 < 0):
        pares8 = pares8 + 1;
        negativos8 = negativos8 + 1;
    elif (num8 % 2 != 0 and num8 < 0):
        impares8 = impares8 + 1;
        negativos8 = negativos8 + 1;
    else:
        pares8 = pares8 + 1;

print(f"Números pares: {pares8}")
print(f"Números impares: {impares8}")
print(f"Números positivos: {positivos8}")
print(f"Números negativos: {negativos8}")

#  Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).

num9 = 0;
suma9 = 0;
media9 = 0;
rango9 = 10

print(f"Ingrese 100 números")

for i in range(rango9):
   num9 = int(input())
   suma9 = suma9 + num9;

media9 = suma9 / rango9;

print(f"La media es {media9}")

# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

numx = int(input("Ingrese un número entero: "))
invertidox = 0
numx = abs(numx) 

while numx > 0:
    digitox = numx % 10              
    invertidox = invertidox * 10 + digitox 
    numx = numx // 10                     

print(f"Número invertido: {invertidox}")
