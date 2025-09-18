# Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 

num = 1;
suma = 0;

while num != 0:
    num = int(input('Ingrese un número: '));
    suma = suma + num;

print(f"La suma de los números ingresados es {suma}")