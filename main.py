import pygame
import random
import math

import sys


# Initialize health bar attributes
health = 100
health_bar_color = (255, 0, 0)
health_bar_width = 150
health_bar_height = 20
health_bar_x = 20
health_bar_y = 20

def draw_health_bar(WIN):
    # Draw the health bar
    pygame.draw.rect(WIN, health_bar_color, (health_bar_x, health_bar_y, health_bar_width, health_bar_height))

    # Calculate the width of the part of the health bar that represents the current health
    current_health_width = health / 100 * health_bar_width

    # Draw the part of the health bar that represents the current health
    pygame.draw.rect(WIN, (0, 255, 0), (health_bar_x, health_bar_y, current_health_width, health_bar_height))


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

    def shoot(self):
        laser = {
            'x': self.x,
            'y': self.y,
        }
        lasers.append(laser)

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, image, width, height, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(1, 5)
        self.speed = random.randint(3, 10)  # Generate a random speed for each asteroid

    def update(self):
        self.rect.y += self.speed


class Laser:
    def __init__(self, x, y, angle):
        self.image = pygame.image.load("laser.png")
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 10

    def update(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))

    def draw(self, WIN):
        WIN.blit(self.image, (self.x, self.y))



def main():
    # Initialize Pygame
    pygame.init()

# Set up the display
pygame.display.set_caption("Health Bar Example")

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
asteroid_image = pygame.image.load('imgs/asteroid.png')
asteroid_width = 1
asteroid_height = 1

# Set up the number of asteroids that will appear at the begining
num_of_asteroids = 5

# Set up the asteroids
asteroids = []

for i in range(5):
    asteroid_x = random.randint(0, display_width - asteroid_width)
    asteroid_y = random.randint(-display_height, -asteroid_height)
    asteroid = Asteroid(asteroid_image, asteroid_width, asteroid_height, asteroid_x, asteroid_y)
    asteroids.append(asteroid)

all_asteroids = pygame.sprite.Group()
asteroid = Asteroid(asteroid_image, 50, 50, 0, -50)
all_asteroids.add(asteroid)


def spawn_asteroids():
    x_pos = random.randint(0, display_width - 50)
    y_pos = -50
    asteroid = Asteroid(asteroid_image, 50, 50, x_pos, y_pos)
    asteroids.append(asteroid)

def update_asteroids():
    for asteroid in asteroids:
        asteroid['y'] += asteroid['speed']
        if asteroid['y'] > display_height:
            asteroids.remove(asteroid)

def draw_game_objects(WIN, spaceship, asteroids, lasers):
    WIN.blit(spaceship.image, (spaceship.x, spaceship.y))
    for asteroid in asteroids:
        WIN.blit(asteroid.image, (asteroid.x, asteroid.y))
    for laser in lasers:
        WIN.blit(laser.image, (laser.x, laser.y))


class HealthBar:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 0, 0)
        self.current_health = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.current_health, self.height))


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

def draw_game_objects(game_display, spaceship, asteroids, lasers):
    game_display.blit(background_image, (0, 0))
    spaceship.draw(game_display)

    for asteroid in asteroids:
        game_display.blit(asteroid.image, asteroid.rect)
    for laser in lasers:
        game_display.blit(laser_image, (laser['x'], laser['y']))


keys = pygame.key.get_pressed()
if keys[pygame.K_SPACE]:
    # Create a new laser and add it to the list
    laser = {
        'x': spaceship.x,
        'y': spaceship.y,
    }
    lasers.append(laser)

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


    # Wait for a while
    clock.tick(FPS)

    all_asteroids.update()
    all_asteroids.draw(WIN)

    # Update the position of the asteroids and check for collisions
    for asteroid in asteroids:
        asteroid.rect.y += 2  # adjust the speed here

        # Check if the asteroid has left the screen
        if asteroid.rect.y >= display_height:
            asteroids.remove(asteroid)
            # Create a new asteroid
            spawn_asteroids()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            spaceship.shoot()

    if keys[pygame.K_SPACE]:
        laser = Laser(spaceship.x, spaceship.y, spaceship.angle)
        lasers.append(laser)
    for laser in lasers:
        laser.update()
        laser.draw(WIN)


    # Check if any lasers have hit the asteroid
    for laser in lasers:
        if laser['x'] > asteroid.rect.x and laser['x'] < asteroid.rect.x + asteroid_width and laser['y'] < asteroid.rect.y \
                + asteroid_height:
            # The laser has hit the asteroid, so remove the asteroid and the laser
            asteroids.remove(asteroid)
            lasers.remove(laser)
            # Create a new asteroid
            spawn_asteroids()
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

    # Draw the background image
    WIN.blit(background_image, (0, 0))



    # Draw the game objects
    draw_game_objects(WIN, spaceship, asteroids, lasers,)
    # Draw the health bar
    draw_health_bar(WIN)


    # Update the display
    pygame.display.update()

pygame.quit()

if __name__ == "__main__":
    main()