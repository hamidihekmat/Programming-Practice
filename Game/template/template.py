import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# Colors

WHITE = (255, 255, 255)
BLACK = (0, 0 ,0)

# initialize pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

# Game Loop
running = True
while running:
    # keep game running at FPS
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # closing window
        if event.type == pygame.QUIT:
            running = False
    # Update
    # Render
    screen.fill(BLACK)
    # after drawing on screen
    pygame.display.flip()

pygame.quit()
