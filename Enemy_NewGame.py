import random
import pygame
import os.path
from pygame.locals import (
    RLEACCEL)

folder = os.path.abspath(os.path.dirname(__file__))

ENEMY_IMAGE_PATH = os.path.join(folder, "alien.png")

class Enemy(pygame.sprite.Sprite):

    def __init__(self, speed, size): 
        pygame.sprite.Sprite.__init__(self)
        print("New enemy created")

        self.surf = pygame.image.load(ENEMY_IMAGE_PATH).convert()
        transparent_color = self.surf.get_at((0,0))
        self.surf.set_colorkey(transparent_color, RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(100,100))
            

        self.speed = speed
        self.size = size

    def update(self):
        #print("Hello")
        self.rect.move_ip(self.speed, 0)
        if self.rect.right < 0:
            self.kill()

    def __str__(self):
        text = ""
        text += "Enemy information:\n"
        text += f"- speed: {self.speed}\n"
        text += f"- size: {self.size}\n"
        return text
    


if __name__ == "__main__":
    enemy = Enemy(speed=4, size=3)
    print(enemy)

    