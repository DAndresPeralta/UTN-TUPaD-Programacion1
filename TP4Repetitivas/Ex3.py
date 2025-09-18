#  Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 

num1 = int(input('Ingrese el primer número: '));
num2 = int(input('Ingrese el segundo número: '));
suma = 0;

for i in range (num1 + 1, num2):
    suma = suma + i;

print(f"La suma de los números comprendidos entre {num1} y {num2} es: {suma}")