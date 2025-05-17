import sys, pygame
from pygame.locals import *
pygame.init()

# Font to display text
font = pygame.sysfont.SysFont('Arial', 20)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Set up the display
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')
# Lock the frame rate
clock = pygame.time.Clock()
FPS = 30

# Quit the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(BLACK)  # Fill the screen with black
    pygame.display.flip()  # Update the display
    clock.tick(FPS)  # Control the frame rate
# Quit pygame
pygame.quit()