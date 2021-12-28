import pygame
import random
from pygame.locals import (
K_ESCAPE,
KEYDOWN
)
import sys
import os.path

from Enemy_NewGame import Enemy

pygame.init()
screen = pygame.display.set_mode((1000,700))


all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

enemy = Enemy(speed=random.randint(1,10), size=random.randint(1,10)) # change parameters for size as it depends on image.
#print(enemy)

all_sprites.add(enemy)
enemies.add(enemy)

bg_colour = (40, 200, 143)


running = True

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

print("Hello")
while running:
   
    for entity in enemies:
        entity.update()

    screen.fill(bg_colour)

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

