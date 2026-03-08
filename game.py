import pygame
import numpy as np

from config import *

from player import Player
from defects import Dislocation, Twin

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.dislocations = [Dislocation(100, 100), Dislocation(200, 200), Dislocation(300, 300)]
        self.twins = [Twin(400, 400), Twin(500, 500), Twin(600, 600)]

    def run(self) -> None:
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
            for t in self.twins:
                t.draw(self.screen)

            pygame.display.flip()
            self.dt = self.clock.tick(FPS) / 1000

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()