# Import the pygame module
import pygame
import random
import sys
import os.path


# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards

# https://pygame.readthedocs.io/en/latest/1_intro/intro.html#import-pygame-locals

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


# get the folder qwhich contains this file
folder = os.path.abspath(os.path.dirname(__file__))

PLAYER = os.path.join(folder, "man.png")
FLYER = os.path.join(folder, "star.png")
ENEMY = os.path.join(folder, "alien.png")

bg_color = (0, 247, 255)

SONG = os.path.join(folder, "song.mp3")  # mp3 file
SOUND = None

# Define constants for the screen width and height
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600


def play_sound(sound_file):
    
    #play sound once
    if sound_file is not None:
        soundObj = pygame.mixer.Sound(sound_file)
        soundObj.play(1)


class Song:

    def __init__(self, mute=False):

        self.mute = mute

        # load song file
        self.song = pygame.mixer.Sound(SONG)

    def play(self):
        if not self.mute:
            self.song.play(-1)

    def stop(self):
        if not self.mute:
            self.song.stop()


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load(PLAYER).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -7.5)

        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 7.5)


        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-7.5, 0)


        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(7.5, 0)


        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load(ENEMY).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Define the flyer object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Flyer(pygame.sprite.Sprite):
    def __init__(self):
        super(Flyer, self).__init__()
        self.surf = pygame.image.load(FLYER).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites, cloud sprites, and all sprites
# - enemies is used for collision detection and position updates
# - clouds is used for position updates
# - all_sprites is used for rendering

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Update the display
pygame.display.flip()

#start in game song, pass mute=True if you want to surpress song
song = Song()

# Variable to keep the main loop running
running = True
song.play()


# Main loop
while running:

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Add a new cloud?
        elif event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Flyer()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
            
    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        
        # If so, then remove the player and stop the loop
        player.kill()
        
        print("Game Over")
        
        song.stop()
        play_sound("lose.mp3")

        pygame.time.wait(5000)

        running = False

    # Update enemy position
    enemies.update()
    clouds.update()

    # Fill the screen with sky blue
    screen.fill(bg_color)

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
 
    # Flip screen
    pygame.display.flip()
 
    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

