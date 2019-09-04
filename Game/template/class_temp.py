import pygame
import random

# settings
WHITE = (255, 255, 255)
BLACK = (0, 0 ,0)

class Game:
    def __init__(self, w, h, fps=30):
        pygame.init()
        pygame.mixer.init()
        self.WIDTH = w
        self.HEIGHT = h
        self.FPS = fps
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('My Game')
        self.clock = pygame.time.Clock()
        self.running = True
        if self.running == False:
            pygame.quit()

    def set_fps(self, newfps):
        self.FPS = newfps

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def start_game(self):
        while self.running:
            self.clock.tick(self.FPS)
            # Update
            self.update()
            # Render
            self.screen.fill(BLACK)
            # after drawing on screen
            pygame.display.flip()

Game(500, 500, 60).start_game()
