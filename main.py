import pygame
import random
import math

import sys

class Spaceship:
    def __init__(self, image, width, height, x, y, angle):
        # Initialize the spaceship's attributes
        self.image = image
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 5

    def move_left(self):
        new_x = self.x - self.speed * math.cos(math.radians(self.angle))
        new_y = self.y - self.speed * math.sin(math.radians(self.angle))
        if new_x >= 0 and new_x <= display_width - self.width:
            self.x = new_x
        if new_y >= 0 and new_y <= display_height - self.height:
            self.y = new_y

    def move_right(self):
        new_x = self.x + self.speed * math.cos(math.radians(self.angle))
        new_y = self.y + self.speed * math.sin(math.radians(self.angle))
        if new_x >= 0 and new_x <= display_width - self.width:
            self.x = new_x
        if new_y >= 0 and new_y <= display_height - self.height:
            self.y = new_y

    def move_up(self):
        new_x = self.x + self.speed * math.sin(math.radians(self.angle))
        new_y = self.y - self.speed * math.cos(math.radians(self.angle))
        if new_x >= 0 and new_x <= display_width - self.width:
            self.x = new_x
        if new_y >= 0 and new_y <= display_height - self.height:
            self.y = new_y

    def move_down(self):
        new_x = self.x - self.speed * math.sin(math.radians(self.angle))
        new_y = self.y + self.speed * math.cos(math.radians(self.angle))
        if new_x >= 0 and new_x <= display_width - self.width:
            self.x = new_x
        if new_y >= 0 and new_y <= display_height - self.height:
            self.y = new_y

    def rotation_handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.x > 0:
            self.x -= 0.5
            self.angle -= 5
        if keys[pygame.K_LEFT] and self.x < display_width - self.width:
            self.x += 0.5
            self.angle += 5

    def movement_handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x > 0:
            self.move_left()
        if keys[pygame.K_d] and self.x < display_width - self.width:
            self.move_right()
        if keys[pygame.K_w] and self.y > 0:
            self.move_up()
        if keys[pygame.K_s] and self.y < display_height - self.height:
            self.move_down()

    def draw(self, WIN):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect()
        rotated_rect.center = (self.x + self.width / 2, self.y + self.height / 2)
        WIN.blit(rotated_image, rotated_rect)

# Initialize Pygame
pygame.init()

# Set up the display
display_width = 800
display_height = 600
WIN = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Asteroid Shooter')

# Set up the player's spaceship
spaceship_image = pygame.image.load('imgs/spaceship.png')
spaceship_width = 50
spaceship_height = 50
spaceship_x = display_width / 2
spaceship_y = display_height - spaceship_height
spaceship_angle = 0
spaceship = Spaceship(spaceship_image, spaceship_width, spaceship_height, spaceship_x, spaceship_y, spaceship_angle)

# Set up the asteroids
asteroid_image = pygame.image.load('imgs/asteriod.png')
asteroid_width = 50
asteroid_height = 50
asteroid_x = random.randint(0, display_width - asteroid_width)
asteroid_y = 0
asteroid_speed = 2

# Set up the laser
laser_image = pygame.image.load('imgs/laser.png')
laser_width = 10
laser_height = 30
laser_x = spaceship_x + spaceship_width / 2 - laser_width / 2
laser_y = spaceship_y
laser_speed = 5

background_image = pygame.image.load('imgs/background.jpg')




# Create a list to store all the lasers on the screen
lasers = []

# Set up the asteroids
asteroids = []

def create_asteroid():
    asteroid = {
        'x': random.randint(0, display_width - asteroid_width),
        'y': 0,
    }
    asteroids.append(asteroid)


def draw_game_objects(game_display, spaceship, asteroids, lasers):
    game_display.blit(background_image, (0, 0))
    spaceship.draw(game_display)

    for asteroid in asteroids:
        game_display.blit(asteroid_image, (asteroid['x'], asteroid['y']))
    for laser in lasers:
        game_display.blit(laser_image, (laser['x'], laser['y']))

    pygame.display.update()

# Create some initial asteroids
for i in range(5):
    create_asteroid()

run = True


FPS = 60
clock = pygame.time.Clock()



# Set up the game loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    spaceship.rotation_handle_input()
    spaceship.movement_handle_input()

    # Draw the game objects
    draw_game_objects(WIN, spaceship, asteroids, lasers)

    # Wait for a while
    clock.tick(FPS)

    # Update the position of the asteroids and check for collisions
    for asteroid in asteroids:
        asteroid['y'] += asteroid_speed
        # Check if the asteroid has left the screen
        if asteroid['y'] > display_height:
            # Remove the asteroid from the list
            asteroids.remove(asteroid)
            # Create a new asteroid
            create_asteroid()

            # # Handle keyboard input
            # pygame.key.init()
            # keys = pygame.key.get_pressed()


            # Check if any lasers have hit the asteroid
            for laser in lasers:
                if laser['x'] > asteroid['x'] and laser['x'] < asteroid['x'] + asteroid_width and laser['y'] < asteroid[
                    'y'] + asteroid_height:
                    # The laser has hit the asteroid, so remove the asteroid and the laser
                    asteroids.remove(asteroid)
                    lasers.remove(laser)
                    # Create a new asteroid
                    create_asteroid()
            # Move the lasers
            for laser in lasers:
                laser['y'] -= laser_speed



                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Create a new laser and add it to the list
                        laser = {
                            'x': laser_x,
                            'y': laser_y,
                        }
                        lasers.append(laser)



        # Draw the game objects
        WIN.fill((0, 0, 0))
        WIN.blit(background_image, (0, 0))
        WIN.blit(spaceship_image, (spaceship_x, spaceship_y))
        for asteroid in asteroids:
            WIN.blit(asteroid_image, (asteroid['x'], asteroid['y']))

pygame.quit()