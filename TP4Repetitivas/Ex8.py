#  Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

num = 0;
pares = 0;
impares = 0;
positivos = 0;
negativos = 0;

print(f"Ingrese 100 números")

for i in range(100):
    num = int(input())

    if (num % 2 == 0 and num > 0):
        pares = pares + 1;
        positivos = positivos + 1;
    elif (num % 2 != 0 and num > 0):
        impares = impares + 1;
        positivos = positivos + 1;
    elif (num % 2 == 0 and num < 0):
        pares = pares + 1;
        negativos = negativos + 1;
    elif (num % 2 != 0 and num < 0):
        impares = impares + 1;
        negativos = negativos + 1;
    else:
        pares = pares + 1;

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

