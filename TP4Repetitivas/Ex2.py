# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 

num = int(input('Ingrese un número '));
contador = 0;

while num > 0:
    num = num // 10;
    contador = contador + 1;

print(f"El número ingreso tiene {contador} dígitos.")

