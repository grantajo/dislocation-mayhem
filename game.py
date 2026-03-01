import pygame
import numpy as np

from config import *

from player import Player
from defects import dislocation

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.dislocations = [dislocation(100, 100), dislocation(200, 200), dislocation(300, 300)]

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            keys = pygame.key.get_pressed()
            self.player.move(keys)

            self.screen.fill(LIGHT_GRAY)
            self.player.draw(self.screen)
            for d in self.dislocations:
                d.draw(self.screen)

            pygame.display.flip()
            self.dt = self.clock.tick(FPS) / 1000

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()