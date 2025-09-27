# Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
# • Inicializarlo con guiones "-" representando casillas vacías. 
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
# • Mostrar el tablero después de cada jugada. 

tablero = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

jugador1 = 'X'
jugador2 = 'O'

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

mostrar_tablero(tablero)

for turno in range(9):
    if turno % 2 == 0:
        jugador = jugador1
    else:
        jugador = jugador2

    fila = int(input(f"Turno del jugador {jugador}, ingrese la fila (0-2): "))
    columna = int(input(f"Turno del jugador {jugador}, ingrese la columna (0-2): "))

    if tablero[fila][columna] == '-':
        tablero[fila][columna] = jugador
    else:
        print("Casilla ya ocupada, intente de nuevo.")

    mostrar_tablero(tablero)
