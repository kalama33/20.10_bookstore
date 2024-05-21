import random

def jugar():
    opciones = ['piedra', 'papel', 'tijera'] # lista de strings
    
    # Elección del jugador
    jugador = input("Elige piedra, papel o tijera: ").lower()
    
    # Elección aleatoria de la computadora
    computadora = random.choice(opciones)
    
    print("Jugador: ", jugador)
    print("Computadora: ", computadora)
    
    # Verificar el resultado del juego
    if jugador == computadora:
        print("Empate")
    elif (jugador == 'piedra' and computadora == 'tijera') or (jugador == 'papel' and computadora == 'piedra') or (jugador == 'tijera' and computadora == 'papel'):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
        
    # Preguntar si desea jugar de nuevo
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    
    if jugar_de_nuevo == 's':
        jugar()

# Iniciar el juego
jugar()