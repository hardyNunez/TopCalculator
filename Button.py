import pygame

class Button:
    # Constructor
    def __init__(self, pos_x, pos_y, height, width, color, icon, icon_color, icon_size, input):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.color = color
        self.icon = icon
        self.icon_color = icon_color
        self.icon_size = icon_size
        self.input = input
    
    # Draws the button square on the screen with given attributes and calls draw_icon() function
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.pos_x, self.pos_y, self.width, self.height))
        self.draw_icon(screen)

    # Draws the icon as text
    def draw_icon(self, screen):
        font = pygame.font.SysFont('Sans serif', self.icon_size)
        text_surface = font.render(self.icon, True, self.icon_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.pos_x + self.width // 2, self.pos_y + self.height // 2)
        screen.blit(text_surface, text_rect)
    
    # Function for button press event
    def pressed(self):
        global representation 
        representation = str(self.input)
        return representation
            
    # Checks collision based on a collider with the body
    def area(self, body):
        collider = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        return body.colliderect(collider)
