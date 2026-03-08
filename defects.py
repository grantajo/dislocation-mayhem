import pygame
import numpy as np

from config import *

class Dislocation:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.radius = 10
        self.color = RED

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class Twin:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.length = 20
        self.color = DARK_RED

    def draw(self, screen) -> None:
        pygame.draw.line(screen, self.color, (self.x - self.length // 2, self.y), (self.x + self.length // 2, self.y), width=3)