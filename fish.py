import pygame
from vector import Vector

class Fish:
    def __init__(self, position, velocity, image_file):
        self.position = position  
        self.velocity = velocity  
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (50, 50))

    def update(self):
        # Opdaterer positionen ved at lægge velocity til
        self.position = self.position + self.velocity

        # Tjek om fisken rammer kanten af skærmen og vend om
        if self.position.get_x() <= 0 or self.position.get_x() >= 750:  # Grænse ved skærmbredde (800 minus fisken på 50px)
            self.velocity = Vector(-self.velocity.get_x(), self.velocity.get_y())  # Vend om i x-retning
        if self.position.get_y() <= 0 or self.position.get_y() >= 550:  # Grænse ved skærmhøjde (600 minus fisken på 50px)
            self.velocity = Vector(self.velocity.get_x(), -self.velocity.get_y())  # Vend om i y-retning

    def draw(self, screen):
        # Tegner fisken på skærmen på dens aktuelle position
        screen.blit(self.image, (self.position.get_x(), self.position.get_y()))
