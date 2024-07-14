import pygame
from Button import Button

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

# Buttons
square_color = yellow
icon_color = black
icon_size = 35

'''
Button logic is as follows:
Button_x = Button(Position_X, Position_Y, height, width, square_color, Icon, icon_color, icon_size, input)
'''

Bo_1 = Button(200, 300, 32, 32, square_color, '1', icon_color, icon_size, 1)
Bo_2 = Button(266, 300, 32, 32, square_color, '2', icon_color, icon_size, 2)
Bo_3 = Button(332, 300, 32, 32, square_color, '3', icon_color, icon_size, 3)

Bo_4 = Button(200, 364, 32, 32, square_color, '4', icon_color, icon_size, 4)
Bo_5 = Button(266, 364, 32, 32, square_color, '5', icon_color, icon_size, 5)
Bo_6 = Button(332, 364, 32, 32, square_color, '6', icon_color, icon_size, 6)

Bo_7 = Button(200, 428, 32, 32, square_color, '7', icon_color, icon_size, 7)
Bo_8 = Button(266, 428, 32, 32, square_color, '8', icon_color, icon_size, 8)
Bo_9 = Button(332, 428, 32, 32, square_color, '9', icon_color, icon_size, 9)

Bo_0 = Button(266, 492, 32, 32, square_color, '0', icon_color, icon_size, 0)

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

            # Key to press buttons (Enter)
            if event.key == pygame.K_RETURN:
                
                # If we are on top of a button, it will send the signal to execute the pressed function
                
                if Bo_1.area(p_rect):
                    Bo_1.pressed()
                
                if Bo_2.area(p_rect):
                    Bo_2.pressed()
                
                if Bo_3.area(p_rect):
                    Bo_3.pressed()    

                if Bo_4.area(p_rect):
                    Bo_4.pressed()
                
                if Bo_5.area(p_rect):
                    Bo_5.pressed()
                
                if Bo_6.area(p_rect):
                    Bo_6.pressed()    
                
                if Bo_7.area(p_rect):
                    Bo_7.pressed()
                
                if Bo_8.area(p_rect):
                    Bo_8.pressed()
                
                if Bo_9.area(p_rect):
                    Bo_9.pressed()
                
                if Bo_0.area(p_rect):
                    Bo_0.pressed()
                
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
    
    # Drawing the buttons
    Bo_1.draw(screen)
    Bo_2.draw(screen)
    Bo_3.draw(screen)

    Bo_4.draw(screen)
    Bo_5.draw(screen)
    Bo_6.draw(screen)
    
    Bo_7.draw(screen)
    Bo_8.draw(screen)
    Bo_9.draw(screen)
    
    Bo_0.draw(screen)
    
    # Updating the screen
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
