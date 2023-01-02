import pygame
import random
import sys

class Spaceship:
    def __init__(self, image, width, height, x, y, angle):
        self.image = image
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.angle = angle

    def draw(self, game_display):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect()
        rotated_rect.center = (self.x + self.width / 2, self.y + self.height / 2)
        game_display.blit(rotated_image, rotated_rect)

# Initialize Pygame
pygame.init()

# Set up the display
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
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

# Add some asteroids to the list
asteroid_1 = {
    'x': 50,
    'y': 50,
}
asteroid_2 = {
    'x': 100,
    'y': 100,
}
asteroids.append(asteroid_1)
asteroids.append(asteroid_2)


def draw_game_objects(game_display, spaceship, asteroids, lasers):
    game_display.blit(background_image, (0, 0))
    spaceship.draw(game_display)
    for asteroid in asteroids:
        game_display.blit(asteroid_image, (asteroid['x'], asteroid['y']))
    for laser in lasers:
        game_display.blit(laser_image, (laser['x'], laser['y']))

    pygame.display.update()


run = True

draw_game_objects(game_display, spaceship, asteroids, lasers)


# Set up the game loop
while run:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Create a new laser and add it to the list
                laser = {
                    'x': laser_x,
                    'y': laser_y,
                }
                lasers.append(laser)
    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship_x > 0:
        spaceship_x -= 0.2
    if keys[pygame.K_RIGHT] and spaceship_x < display_width - spaceship_width:
        spaceship_x += 0.2
    if keys[pygame.K_UP] and spaceship_y > 0:
        spaceship_y -= 0.2
    if keys[pygame.K_DOWN] and spaceship_y < display_height - spaceship_height:
        spaceship_y += 0.2

    # Move the asteroids
    asteroid_y += asteroid_speed
    # Check if any lasers have hit the asteroid
    for laser in lasers:
        if laser['x'] > asteroid_x and laser['x'] < asteroid_x + asteroid_width and laser[
            'y'] < asteroid_y + asteroid_height:
            # The laser has hit the asteroid, so remove the asteroid and the laser
            lasers.remove(laser)
            asteroid_x = random.randint(0, display_width - asteroid_width)
            asteroid_y = 0
    # Move the lasers
    for laser in lasers:
        laser['y'] -= laser_speed
    # Draw the game objects
    game_display.blit(background_image, (0, 0))
    rotated_spaceship = pygame.transform.rotate(spaceship_image, spaceship_angle)
    rotated_rect = rotated_spaceship.get_rect()
    rotated_rect.center = (spaceship_x + spaceship_width / 2, spaceship_y + spaceship_height / 2)
    game_display.blit(rotated_spaceship, rotated_rect)
    for asteroid in asteroids:
        game_display.blit(asteroid_image, (asteroid['x'], asteroid['y']))

pygame.quit()