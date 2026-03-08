# dislocation-mayhem/test.py

"""
This is a test see what I can do with the dislocation-mayhem package. 

I just want to test out some basic game dev stuff.
"""

import sys

import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    # fill the screen with a color to wipe away anything from the last frame
    grayscale=(140, 140, 140)
    screen.fill(color=grayscale)
    pygame.draw.circle(screen, "blue", player_pos, radius=15, width=2)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
