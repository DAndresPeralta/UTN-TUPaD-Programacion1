# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

num1 = 0;
num2 = int(input("Ingrese un número positivo: "));
suma = 0;

num2 = abs(num2);

for i in range(num2):
    suma = suma + i;

print(f"La suma de los números comprendidos entre {num1} y {num2} es: {suma}")