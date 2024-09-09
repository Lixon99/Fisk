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

    def screenContainment(self):
        if self.__position.x < 2 or self.__position.x > self.screen.get_width()-self.fish_img.get_width() - 2:
            self.velocity.x *= -1
        if self.__position.y < 2 or self.__position.y > self.screen.get_height()-self.fish_img.get_height() - 2:
            self.velocity.x *= -1
        return self.velocity
    
    def screenConfinementIt(self, d, velocity, position):
        self.d = 50
        velocity.x = -1
        position = 50
        if self.position.x < d:
            velocity.x = velocity.x + (1 - position.x/d)
        if position.x < d:
            velocity.x = velocity.x + (1 - 50/50)
        if position.x < d:
            velocity.x = velocity.x + (1 - 40/50)
        if position.x < d:
            velocity.x = velocity.x + (1 - 25/50)
        if position.x < d:
            velocity.x = velocity.x + (1 - 10/50)

        velocity.y = velocity.x + (1 - 10/50)
        return velocity.x, velocity.y

