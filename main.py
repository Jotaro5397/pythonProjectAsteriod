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
    spaceship.x = spaceship_x
    spaceship.y = spaceship_y
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

    clock.tick(FPS)
    draw_game_objects(WIN, spaceship, asteroids, lasers)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
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
                    spaceship_x -= 0.5
                    spaceship_angle -= 5
                if keys[pygame.K_RIGHT] and spaceship_x < display_width - spaceship_width:
                    spaceship_x += 0.5
                    spaceship_angle += 5
                if keys[pygame.K_UP] and spaceship_y > 0:
                    spaceship_y -= 0.5
                if keys[pygame.K_DOWN] and spaceship_y < display_height - spaceship_height:
                    spaceship_y += 0.5

        # Move the asteroids
        for asteroid in asteroids:
            asteroid['y'] += asteroid_speed
            # Check if the asteroid has left the screen
            if asteroid['y'] > display_height:
                # Remove the asteroid from the list
                asteroids.remove(asteroid)
                # Create a new asteroid
                create_asteroid()
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
        # Draw the game objects
        WIN.fill((0, 0, 0))
        WIN.blit(background_image, (0, 0))
        WIN.blit(spaceship_image, (spaceship_x, spaceship_y))
        for asteroid in asteroids:
            WIN.blit(asteroid_image, (asteroid['x'], asteroid['y']))

pygame.quit()