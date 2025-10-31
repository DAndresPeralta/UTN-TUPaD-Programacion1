# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores. 

capitales = {}

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción",
    "Perú": "Lima",
    "Bolivia": "La Paz",
    "Colombia": "Bogotá",
    "Ecuador": "Quito",
    "Venezuela": "Caracas",
    "México": "Ciudad de México",
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma",
    "Alemania": "Berlín",
    "Reino Unido": "Londres",
    "Estados Unidos": "Washington D.C.",
    "Canadá": "Ottawa",
    "Japón": "Tokio",
    "China": "Pekín"
}

capitales = {capital: pais for pais, capital in paises.items()}
print('Diccionario invertido')
print(capitales)