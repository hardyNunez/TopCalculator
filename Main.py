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

# Inner Square (s1) and Outer Square (s2)
s1_color = white
s1_x = 100
s1_y = screen_size[1] / 9
s1_height = 600
s1_width = 128

s2_color = yellow
s2_x = 100 + 64
s2_y = screen_size[1] / 9 + 32
s2_height = 460
s2_width = 64

'''
Button logic:
Button_x = Button(Position_X, Position_Y, height, width, square_color, Icon, icon_color, icon_size, input)
'''

Bo_1 = Button(200, 300, 32, 32, square_color, '1', icon_color, icon_size, '1')
Bo_2 = Button(266, 300, 32, 32, square_color, '2', icon_color, icon_size, '2')
Bo_3 = Button(332, 300, 32, 32, square_color, '3', icon_color, icon_size, '3')

Bo_4 = Button(200, 364, 32, 32, square_color, '4', icon_color, icon_size, '4')
Bo_5 = Button(266, 364, 32, 32, square_color, '5', icon_color, icon_size, '5')
Bo_6 = Button(332, 364, 32, 32, square_color, '6', icon_color, icon_size, '6')

Bo_7 = Button(200, 428, 32, 32, square_color, '7', icon_color, icon_size, '7')
Bo_8 = Button(266, 428, 32, 32, square_color, '8', icon_color, icon_size, '8')
Bo_9 = Button(332, 428, 32, 32, square_color, '9', icon_color, icon_size, '9')

Bo_0 = Button(266, 492, 32, 32, square_color, '0', icon_color, icon_size, '0')

# Extra text variables
text = ""
t_x, t_y = 200, screen_size[1] / 9 + 45
t_screen = text

# Function to draw text on the screen
def draw_text(surface, text, size, color, x, y):
    font = pygame.font.SysFont('Arial', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

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
                
                # If we are over a button, it will send the signal for the pressed function to execute
                
                if Bo_1.area(p_rect):
                    text += Bo_1.pressed()
                    
                if Bo_2.area(p_rect):
                    text += Bo_2.pressed()
                
                if Bo_3.area(p_rect):
                    text += Bo_3.pressed()

                if Bo_4.area(p_rect):
                    text += Bo_4.pressed()
                
                if Bo_5.area(p_rect):
                    text += Bo_5.pressed()
                
                if Bo_6.area(p_rect):
                    text += Bo_6.pressed()
                
                if Bo_7.area(p_rect):
                    text += Bo_7.pressed()
                
                if Bo_8.area(p_rect):
                    text += Bo_8.pressed()
                
                if Bo_9.area(p_rect):
                    text += Bo_9.pressed()
                
                if Bo_0.area(p_rect):
                    text += Bo_0.pressed()
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                p_y_speed = 0
            if event.key == pygame.K_s:
                p_y_speed = 0
            if event.key == pygame.K_a:
                p_x_speed = 0
            if event.key == pygame.K_d:
                p_x_speed = 0
    
    # Adding the speeds to the positions
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
    
    # Drawing the screen
    s1 = pygame.draw.rect(screen, s1_color, (s1_x, s1_y, s1_height, s1_width))
    s2 = pygame.draw.rect(screen, s2_color, (s2_x, s2_y, s2_height, s2_width))
    
    # Drawing text
    draw_text(screen, t_screen,  30, black, t_x, t_y)
    
    # If the text length is not greater than 32
    if not len(text) < 32:
        if t_x == 270:
            t_x += 15
    else:
        t_screen = text
        t_x = 390
    
    # Updating the window
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
