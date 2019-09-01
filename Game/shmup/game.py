import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

# Colors

WHITE = (255, 255, 255)
BLACK = (0, 0 ,0)
GREEN = (0, 255, 0)

# initialize pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spacez')
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speed = 8

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

all_sprite = pygame.sprite.Group()
player = Player()
all_sprite.add(player)
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
    all_sprite.update()
    # Render
    screen.fill(BLACK)
    all_sprite.draw(screen)
    # after drawing on screen
    pygame.display.flip()

pygame.quit()
