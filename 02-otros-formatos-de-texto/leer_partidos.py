import json

# Leer el fichero JSON
with open('partidos.json', 'r') as file:
    partidos = json.load(file)

# Mostrar los resultados por pantalla
for partido in partidos:
    print(f"Nombre del Partido: {partido['Nombre del Partido']}")
    print(f"Equipo Local: {partido['Equipo Local']}")
    print(f"Equipo Visitante: {partido['Equipo Visitante']}")
    print(f"Fecha: {partido['Fecha']}")
    print(f"Resultado: {partido['Resultado']}")
    print('-------------------------')