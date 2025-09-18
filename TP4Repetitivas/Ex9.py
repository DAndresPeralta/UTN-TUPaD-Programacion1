#  Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).

num = 0;
suma = 0;
media = 0;
rango = 10

print(f"Ingrese 100 números")

for i in range(rango):
   num = int(input())
   suma = suma + num;

media = suma / rango;

print(f"La media es {media}")