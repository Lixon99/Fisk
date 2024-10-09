import pygame
import random
from vector import Vector
from fish import Fish  

class Flock:
    def __init__(self, num_fish, screen_size):
        self.fishes = []
        self.screen_size = screen_size
        
        for _ in range(num_fish):
            position = Vector(random.randint(0, 750), random.randint(0, 550))
            velocity = Vector(random.uniform(-3, 3), random.uniform(-3, 3))
            vision_range = random.uniform(50, 150)
            fish = Fish(position, velocity, "fisk.png", vision_range)
            self.fishes.append(fish)

    def update(self):
        for fish in self.fishes:
            neighbors = self.get_neighbors(fish)
            fish.update()

            # Limit vision range to avoid extreme values
            if len(neighbors) < 3:
                fish.vision_range *= 1.2
            else:
                fish.vision_range *= 0.9

    def draw(self, screen):
        for fish in self.fishes:
            fish.draw(screen)

    def get_neighbors(self, fish):
        neighbors = []
        for other in self.fishes:
            if other != fish:
                distance = fish.get_distance_to(other)
                if distance < fish.vision_range:
                    neighbors.append(other)
        return neighbors