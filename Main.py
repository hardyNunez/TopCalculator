import pygame

pygame.init()

# Colors
black = '#222323'
yellow = '#ffcc33'
white = '#f0f6f0'

# Window
screen_size = (800, 600)
background = black
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
title = pygame.display.set_caption('TopCalculator')

# Player
p_color = yellow
p_x = 400
p_y = 300
p_x_speed = 0
p_y_speed = 0
p_width = 32
p_height = 32

# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        # Controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p_y_speed = -5
            if event.key == pygame.K_s:
                p_y_speed = 5
            if event.key == pygame.K_a:
                p_x_speed = -5
            if event.key == pygame.K_d:
                p_x_speed = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                p_y_speed = 0
            if event.key == pygame.K_s:
                p_y_speed = 0
            if event.key == pygame.K_a:
                p_x_speed = 0
            if event.key == pygame.K_d:
                p_x_speed = 0
    
    # Adding speeds to positions             
    p_y += p_y_speed
    p_x += p_x_speed
    
    # Setting the game background
    screen.fill(background)
    
    # Drawing the player
    p_rect = pygame.draw.rect(screen, p_color, (p_x, p_y, p_height, p_width))
    
    # Updating the screen
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
