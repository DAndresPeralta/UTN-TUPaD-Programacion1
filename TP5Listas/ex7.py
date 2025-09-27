# Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
# semana. 
# • Calcular el promedio de las mínimas y el de las máximas. 
# • Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [
    [13,22],
    [14,24],
    [7,19],
    [12,18],
    [20,24],
    [11,27],
    [10,25],
]

minimas = [temp[0] for temp in temperaturas]
maximas = [temp[1] for temp in temperaturas]

promMinimas = sum(minimas)/len(minimas)
promMaximas = sum(maximas)/len(maximas)

print(f"Promedio de temperaturas mínimas: {promMinimas:.2f}")
print(f"Promedio de temperaturas máximas: {promMaximas:.2f}")

amplitudes = [maximas[i] - minimas[i] for i in range(len(temperaturas))]

diaMayorAmplitud = amplitudes.index(max(amplitudes)) + 1

print(f"El día con mayor amplitud térmica es {diaMayorAmplitud}")