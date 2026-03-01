import pygame
import numpy as np

from config import *

class dislocation:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.color = RED

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)