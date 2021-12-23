import pygame
import random
import sys
import os.path

pygame.init()



from Enemy_NewGame import Enemy

enemy = Enemy(speed=random.randint(1,10), size=random.randint(1,10)) # change parameters for size as it depends on image.
#print(enemy)

SCREEN_HEIGHT = 200
SCREEN_WIDTH = 200

bg_colour = (40, 200, 143)

while True:
    pygame.display.set_mode()
    screen = pygame.display.set_mode((200,200))
    
    screen.fill(bg_colour)
    pygame.display.flip()

