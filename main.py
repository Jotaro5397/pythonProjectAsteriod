import pygame
import random

# Initialize Pygame
pygame.init()

# Window size
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Asteroid Shooter")

# Load the spaceship image
spaceship_image = pygame.image.load("imgs/spaceship.png")

# Load the asteroid image
asteroid_image = pygame.image.load("imgs/asteriod.png")

# Load the laser image
laser_image = pygame.image.load("imgs/laser.png")

# Set the spaceship's starting position
spaceship_x = window_size[0] / 2
spaceship_y = window_size[1] - 50

# Set the spaceship's movement speed
spaceship_speed = 5

# Set the laser's movement speed
laser_speed = 10

# Set the asteroid's movement speed
asteroid_speed = 5

# Set the asteroid's starting position
asteroid_x = random.randint(0, window_size[0])
asteroid_y = -50

# Set the laser's starting position
laser_x = spaceship_x + 20
laser_y = spaceship_y

# Set the game to running
running = True

# Start the game loop
while running:
    # Check for events
    for event in pygame.event.get():
        # Check if the user closed the window
        if event.type == pygame.QUIT:
            running = False

        # Check if the user pressed a key
        if event.type == pygame.KEYDOWN:
            # Check if the user pressed the left arrow key
            if event.key == pygame.K_LEFT:
                # Move the spaceship left
                spaceship_x -= spaceship_speed
            # Check if the user pressed the right arrow key
            elif event.key == pygame.K_RIGHT:
                # Move the spaceship right
                spaceship_x += spaceship_speed
            # Check if the user pressed the space bar
            elif event.key == pygame.K_SPACE:
                # Fire a laser
                laser_x = spaceship_x + 20
                laser_y = spaceship_y

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the spaceship
    screen.blit(spaceship_image, (spaceship_x, spaceship_y))

    # Draw the asteroid
    screen.blit(asteroid_image, (asteroid_x, asteroid_y))

    # Draw the laser
    screen.blit(laser_image, (laser_x, laser_y))

    # Update the laser's position
    laser_y -= laser_speed

    pygame.display.update()

