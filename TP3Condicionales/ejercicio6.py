# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
# mediana es mayor que la moda. 
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
# la mediana es menor que la moda. 
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.

import random 
from statistics import mode, median, mean

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