# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random;

randomNum = random.randint(0, 9);
intentos = 0;
num = -1;

while randomNum != num:
    num = int(input('Cual es el número secreto: '));
    if (num < 0 or num > 9):
        print(f"Ingrese un número comprendido entre 0 y 9");
        continue;
    intentos = intentos + 1

print(f"Acertaste!!!")
print(f"El número secreto es {randomNum}, usted intento {intentos} veces")
