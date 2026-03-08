from config import PLAYER_SPEED
import pygame
import numpy as np

from config import *

class Player:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.radius = 20
        self.color = DARK_GRAY
        self.width = 2

    def move(self, keys) -> None:
        direction = pygame.math.Vector2(
            keys[pygame.K_d] - keys[pygame.K_a],
            keys[pygame.K_s] - keys[pygame.K_w]
        )
        
        if direction.length_squared() > 0:
            direction: Vector2 = direction.normalize() * PLAYER_SPEED

        self.x += direction.x
        self.y += direction.y

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.width)

