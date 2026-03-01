import pygame
import numpy as np

from config import *

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.color = DARK_GRAY
        self.width = 2

    def move(self, keys):
        if keys[pygame.K_a]:
            self.x -= PLAYER_SPEED
        if keys[pygame.K_d]:
            self.x += PLAYER_SPEED
        if keys[pygame.K_w]:
            self.y -= PLAYER_SPEED
        if keys[pygame.K_s]:
            self.y += PLAYER_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.width)

