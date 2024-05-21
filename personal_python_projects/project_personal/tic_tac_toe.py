# Crear el tablero de juego
tablero = [' ' for _ in range(9)] #  convención para indicar que no nos importa el valor real de la variable en cada iteración

# Definir los símbolos de los jugadores
jugador1 = 'X'
jugador2 = 'O'

# Función para imprimir el tablero
def imprimir_tablero():
    print('-------------')
    print('|', tablero[0], '|', tablero[1], '|', tablero[2], '|')
    print('-------------')
    print('|', tablero[3], '|', tablero[4], '|', tablero[5], '|')
    print('-------------')
    print('|', tablero[6], '|', tablero[7], '|', tablero[8], '|')
    print('-------------')

# Función para realizar un movimiento
def hacer_movimiento(jugador, posicion):
    tablero[posicion] = jugador

# Función para verificar si un jugador ha ganado
def verificar_ganador(jugador):
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]  # Diagonales
    ]
    
    for combinacion in combinaciones_ganadoras:
        if tablero[combinacion[0]] == tablero[combinacion[1]] == tablero[combinacion[2]] == jugador:
            return True
    
    return False

# Función para jugar el juego completo
def jugar_tic_tac_toe():
    jugador_actual = jugador1
    juego_terminado = False
    
    while not juego_terminado:
        imprimir_tablero()
        posicion = int(input("Jugador {}: Ingresa la posición (0-8): ".format(jugador_actual)))
        
        if tablero[posicion] == ' ':
            hacer_movimiento(jugador_actual, posicion)
            
            if verificar_ganador(jugador_actual):
                imprimir_tablero()
                print("¡Jugador {} ha ganado!".format(jugador_actual))
                juego_terminado = True
            elif ' ' not in tablero:
                imprimir_tablero()
                print("¡Empate!")
                juego_terminado = True
            else:
                jugador_actual = jugador2 if jugador_actual == jugador1 else jugador1
        else:
            print("¡Posición ocupada! Inténtalo de nuevo.")
    
    reiniciar = input("¿Quieres jugar de nuevo? (s/n): ")
    if reiniciar.lower() == 's':
        reiniciar_juego()
    else:
        print("Gracias por jugar. ¡Hasta luego!")

# Función para reiniciar el juego
def reiniciar_juego():
    global tablero
    tablero = [' ' for _ in range(9)]
    jugar_tic_tac_toe()

# Iniciar el juego
jugar_tic_tac_toe()
