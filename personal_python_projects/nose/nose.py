import pygame
from pygame.locals import * 
import random

pygame.init()

# conf screen
width, height = 1200, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Nose")

# colors
white =()
black =()

# images

nose = pygame.image.load("")
kovalev = pygame.image.load("")
background_image =  pygame.image.load("")
obstacle_image = pygame.image.load("")

#size and positions

nose_rect = nose_image.get_rect()
nose_rect.center = (100, height - 50)

kovalev_rect = kovalev_image.get_rect()
kovalev_rect.center = (width - 100, height - 50)

obstacle_rect = obstacle_image.get_rect()
obstacle_rect.center = (width, height - 50)

# speed

nose_speed = 5
obstacle_speed = 10
gravity = 1
jump_strength = 15
jumping = False

# obstacle

obstacles = [obstacle_rect]

#punct

score = 0
font = pygame.font.Font(None, 36)

# main loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # nose's move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        nose_rect.x -= nose_speed
    if keys[pygame.K_RIGHT]:
        nose_rect.x += nose_speed
    
    # nose's jump    
    else:
        if jump_count >= -jump_strength:
            neg = 1
            if jump_count < 0:
                neg = -1
            nose_rect.y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            
    # gravity
    if nose_rect.y < height - 50:
        nose_rect.y += gravity
    else:
        nose_rect.y = height - 50
        
    # new obstacles
    
    if random.randit(0,100) < 10:
        new_obstacle = obstacle_image.get_rect()
        new_obstacle.center = (width, height - 50)
        obstacles.append(new_obstacle)
        
    # collision 
    
    for obstacle in obstacles:
        if unicorn_rect.colliderect(obstacle):
            running = False
            
    # backgroung drawing
    screen.blit(background_image, (0, 0))
    
    # nose, kovalev drawing
    screen.blit(nose_image, nose_rect)
    screen.blit(kovalev_rect_image, kovalev_rect)
    
    # obstacles
    for obstacle in obstacles:
        screen.blit(obstacle_image, obstacle)

    # puncts.
    score += 1
    text = font.render(f"Points: {score}", True, black)
    screen.blit(text, (10, 10))

    # update screen
    pygame.display.update()

# end pygame
pygame.quit()