import pygame
import random
from vector import Vector
from fish import Fish

class Flock:
    def __init__(self, num_fish, screen_size):
        self.fishes = []
        self.screen_size = screen_size
        
        # Create multiple fish with random positions and velocities
        for _ in range(num_fish):
            position = Vector(random.randint(0, screen_size[0]), random.randint(0, screen_size[1]))
            velocity = Vector(random.uniform(-2, 2), random.uniform(-2, 2))
            fish = Fish(position, velocity, "fisk.png") 
            self.fishes.append(fish)

    def update(self):
        for fish in self.fishes:
            fish.update()

    def draw(self, screen):
        for fish in self.fishes:
            fish.draw(screen)

# Initialize Pygame
pygame.init()
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)

# Create the flock of fish
flock = Flock(10, screen_size)  # A flock with 10 fish

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the flock
    flock.update()

    # Draw the flock
    screen.fill((0, 0, 0))  # Clear screen with black background
    flock.draw(screen)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
