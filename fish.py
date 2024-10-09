import pygame
from vector import Vector

class Fish:
    def __init__(self, position, velocity, image_file, vision_range):
        self.position = position  
        self.velocity = velocity  
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.vision_range = vision_range
        self.screen = (800, 600)

    def update(self):
        #separation_change = self.separation(flock_fishes, tooClose=50, separation_factor=0.5)
        #alignment_change = self.alignment(flock_fishes, visible_distance=50, alignment_factor=0.5)
        # cohesion_change = self.cohesion(flock_fishes, visible_distance=50, cohesion_factor=0.5)
        # self.velocity += separation_change + alignment_change + cohesion_change

        #Opdatere hastigheden
        self.velocity = self.screenConfinementBounce()

        # Opdaterer positionen ved at lægge velocity til
        self.position = self.position + self.velocity

        # Tjek om fisken rammer kanten af skærmen og vend om
        if self.position.x <= 0 or self.position.x >= 750:  # Grænse ved skærmbredde (800 minus fisken på 75px)
            self.velocity *= -1  # Vend om i x-retning
        if self.position.y <= 0 or self.position.y >= 550:  # Grænse ved skærmhøjde (600 minus fisken på 75px)
            self.velocity *= -1  # Vend om i y-retning

    def draw(self, screen):
        screen.blit(self.image, (self.position.x, self.position.y))

    def screenConfinementBounce(self):
        velocity = self.velocity
        return self.velocity
    
    def screenConfinementIt(self, d=50):
        if self.position.x < d:
            self.velocity = Vector(self.velocity.x + ((1 - self.position.x/d)**2), self.velocity.y)
            self.velocity = Vector(self.velocity.x + ((1 - (self.position.x - self.screen[0]/d))**2), self.velocity.y)
        if self.position.y < d:
            self.velocity = Vector(self.velocity.x, self.velocity.y + ((1 - self.position.y/d)**2))
            self.velocity = Vector(self.velocity.x, self.velocity.y + ((1 - (self.position.y - self.screen[0]/d))**2))

    def get_distance_to(self, flock_fishes):
        return self.position.distance(flock_fishes.position)
    
    def separation(self, flock_fishes, tooClose=50, separation_factor=0.5):
        pass
    
    def alignment(self, flock_fishes, visible_distance, alignment_factor=0.5):
       pass

    def cohesion(self, flock_fishes, visible_distance, cohesion_factor=0.5):
        pass