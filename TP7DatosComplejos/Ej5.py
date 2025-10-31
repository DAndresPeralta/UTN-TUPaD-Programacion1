# Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra.

cantidad = {}

frase = input('Ingresa una frase: ')

palabras = frase.split()
unicas = set(palabras)

print('Palabras únicas: ', unicas)

for palabra in palabras:
    if palabra in unicas:
        cantidad[palabra] = cantidad.get(palabra, 0) + 1

print('Cantidad de apariciones de cada palabra: ', cantidad)