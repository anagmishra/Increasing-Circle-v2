import pygame #A library has a set or collection of functions or properties for you to use it properly

pygame.init() #Helps us to initialize all the modules (functions and properties) from the pygame library that we will use 
screen = pygame.display.set_mode((600,600))
screen.fill((50,205,50))
blue = (0,0,255)
pygame.display.update()

class Circle:
    def __init__(self, clr, pos, radius, width):
        self.circle_colour = clr
        self.circle_radius = radius
        self.circle_pos = pos
        self.circle_width = width
        self.circle_surface = screen
    
    def draw(self):
        self.draw_circle = pygame.draw.circle( #Function for rectangle is pygame.draw.rect
            self.circle_surface,
            self.circle_colour,
            self.circle_pos,
            self.circle_radius,
            self.circle_width,
        )

    def grow(self, r):
        self.circle_radius = self.circle_radius + r
        self.draw_circle = pygame.draw.circle
        (
            self.circle_surface,
            self.circle_colour,
            self.circle_pos,
            self.circle_radius,
            self.circle_width,
        )

circle = Circle(blue, (300, 300), 20, 0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((50, 205, 50))
            circle.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((50, 205, 50))
            circle.grow(1)
            pygame.display.update()