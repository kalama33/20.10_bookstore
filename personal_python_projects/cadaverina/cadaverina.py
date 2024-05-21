import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana del juego
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Unicornio en Berlín")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Cargar imágenes
unicorn_image = pygame.image.load("unicorn.png")
death_image = pygame.image.load("death.png")
background_image = pygame.image.load("berlin.jpg")
obstacle_image = pygame.image.load("obstacle.png")

# Obtener tamaños y posiciones iniciales
unicorn_rect = unicorn_image.get_rect()
death_rect = death_image.get_rect()
obstacle_rect = obstacle_image.get_rect()
unicorn_rect.center = (100, height - 50)
death_rect.center = (width - 100, height - 50)
obstacle_rect.center = (width, height - 50)

# Velocidad de movimiento
unicorn_speed = 5
obstacle_speed = 10
gravity = 1
jump_strength = 15
jumping = False

# Obstáculos
obstacles = [obstacle_rect]

# Puntuación
score = 0
font = pygame.font.Font(None, 36)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del unicornio
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        unicorn_rect.x -= unicorn_speed
    if keys[pygame.K_RIGHT]:
        unicorn_rect.x += unicorn_speed

    # Saltar
    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
            jump_count = jump_strength
    else:
        if jump_count >= -jump_strength:
            neg = 1
            if jump_count < 0:
                neg = -1
            unicorn_rect.y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False

    # Gravedad
    if unicorn_rect.y < height - 50:
        unicorn_rect.y += gravity
    else:
        unicorn_rect.y = height - 50

    # Mover obstáculos
    for obstacle in obstacles:
        obstacle.x -= obstacle_speed
        if obstacle.right < 0:
            obstacles.remove(obstacle)

    # Crear nuevos obstáculos
    if random.randint(0, 100) < 10:
        new_obstacle = obstacle_image.get_rect()
        new_obstacle.center = (width, height - 50)
        obstacles.append(new_obstacle)

    # Colisiones con obstáculos
    for obstacle in obstacles:
        if unicorn_rect.colliderect(obstacle):
            running = False

    # Dibujar el fondo
    screen.blit(background_image, (0, 0))

    # Dibujar el unicornio y la Muerte
    screen.blit(unicorn_image, unicorn_rect)
    screen.blit(death_image, death_rect)

    # Dibujar obstáculos
    for obstacle in obstacles:
        screen.blit(obstacle_image, obstacle)

    # Puntuación
    score += 1
    text = font.render(f"Puntuación: {score}", True, black)
    screen.blit(text, (10, 10))

    # Actualizar la pantalla
    pygame.display.update()

# Terminar Pygame
pygame.quit()
