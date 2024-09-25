import pygame
from vector import Vector

class Fish:
    def __init__(self, position, velocity, image_file, vision_range):
        self.position = position  
        self.velocity = velocity  
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.vision_range = vision_range
        self.screen = (800, 600)

    def update(self, other_fish):
        seperation_change = self.separation(True)
        alignment_change = self.alignment()
        cohesion_change = self.cohesion()

        self.velocity += seperation_change + alignment_change + cohesion_change
        # Opdaterer positionen ved at lægge velocity til
        self.position = self.position + self.velocity
        self.position += self.velocity

        # Tjek om fisken rammer kanten af skærmen og vend om
        if self.position.get_x() <= 0 or self.position.get_x() >= 750:  # Grænse ved skærmbredde (800 minus fisken på 50px)
            self.velocity = Vector(-self.velocity.get_x(), self.velocity.get_y())  # Vend om i x-retning
        if self.position.get_y() <= 0 or self.position.get_y() >= 550:  # Grænse ved skærmhøjde (600 minus fisken på 50px)
            self.velocity = Vector(self.velocity.get_x(), -self.velocity.get_y())  # Vend om i y-retning

    def draw(self, screen):
        screen.blit(self.image, (self.position.get_x(), self.position.get_y()))

    def screenContainment(self):
        if self.__position.x < 2 or self.__position.x > self.screen.get_width()-self.fish_img.get_width() - 2:
            self.velocity.x *= -1
        if self.__position.y < 2 or self.__position.y > self.screen.get_height()-self.fish_img.get_height() - 2:
            self.velocity.x *= -1
        return self.velocity
    
    def screenConfinementIt(self, d=50):
        if self.position.get_x() < d:
            self.velocity = Vector(self.velocity.get_x() + ((1 - self.position.get_x()/d)**2), self.velocity.get_y())
            self.velocity = Vector(self.velocity.get_x() + ((1 - (self.position.get_x() - self.screen[0]/d))**2), self.velocity.get_y())
        if self.position.get_y() < d:
            self.velocity = Vector(self.velocity.get_x(), self.velocity.get_y() + ((1 - self.position.get_y()/d)**2))
            self.velocity = Vector(self.velocity.get_x(), self.velocity.get_y() + ((1 - (self.position.get_y() - self.screen[0]/d))**2))

    def get_distance_to(self, other_fish):
        #Calculate distance to other fishes
        return self.position.distance_to(other_fish.position)
    
    def separation(self, other_fish, tooClose=50, separation_factor=0.5):
        separation_vector = Vector(0, 0)
        for fish in range(other_fish):
            if fish != self:
                distance = self.position.distance_to(self.position)
                if distance < tooClose:
                    seperation_vector += (self.position - fish.position).normalize() / distance
        return (separation_vector * separation_factor)
    
    def alignment(self, other_fish, visible_distance, alignment_factor):
        pass

    def cohesion(self, other_fish, visible_distance, cohesion_factor):
        pass


