import pygame
import random

def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img,size)


class Movement:
    def __init__(self):
        # Set the movement speed
        self.speed = 5

    def move_left(self, object_x):
        # Move the object left
        object_x -= self.speed
        return object_x

    def move_right(self, object_x):
        # Move the object right
        object_x += self.speed
        return object_x

    def move_up(self, object_y):
        # Move the object up
        object_y -= self.speed
        return object_y

    def move_down(self, object_y):
        # Move the object down
        object_y += self.speed
        return object_y

# Initialize Pygame
pygame.init()


# Load the background image
Background = scale_image(pygame.image.load("imgs/background.jpg"),0.5 )

# Load the spaceship image
spaceship_image = pygame.image.load("imgs/spaceship.png")

# Load the asteroid image
asteroid_image = pygame.image.load("imgs/asteriod.png")

# Load the laser image
laser_image = pygame.image.load("imgs/laser.png")


window_size = (800, 600)

screen = pygame.display.set_mode(window_size)


spaceship_movement = Movement()

# Set the spaceship's starting position
spaceship_x = window_size[0] / 2
spaceship_y = window_size[1] - 50

# Set the spaceship's movement speed
spaceship_speed = 5

# Set the laser's movement speed
laser_speed = 10

# Set the asteroid's movement speed
asteroid_speed = 5

# Create a Movement object for the asteroids
asteroid_movement = Movement()

# Set the asteroid's starting position
asteroid_x = random.randint(0, window_size[0])
asteroid_y = -50

# Set the laser's starting position
laser_x = spaceship_x + 20
laser_y = spaceship_y




# Set the game to running
running = True

# Set the starting time
start_time = pygame.time.get_ticks()

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Set the desired frame rate
frame_rate = 60

# Set the asteroid's movement direction
# 0 = left, 1 = right, 2 = up, 3 = down
asteroid_direction = random.randint(0, 3)

# Set the asteroid's movement speed
asteroid_speed = random.randint(1, 5)

# Start the game loop
while running:
    # Check for events
    for event in pygame.event.get():
        # Check if the user closed the window
        if event.type == pygame.QUIT:
            running = False

        # Check if the user pressed a key
        if event.type == pygame.KEYUP:
            # Check if the user pressed the left arrow key
            if event.key == pygame.K_LEFT:
                # Move the spaceship left
                spaceship_x = spaceship_movement.move_left(spaceship_x)
            # Check if the user pressed the right arrow key
            elif event.key == pygame.K_RIGHT:
                # Move the spaceship right
                spaceship_x = spaceship_movement.move_right(spaceship_x)
            # Check if the user pressed the up arrow key
            elif event.key == pygame.K_UP:
                # Move the spaceship up
                spaceship_y = spaceship_movement.move_up(spaceship_y)
            # Check if the user pressed the down arrow key
            elif event.key == pygame.K_DOWN:
                # Move the spaceship down
                spaceship_y = spaceship_movement.move_down(spaceship_y)
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

