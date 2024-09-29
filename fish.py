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

    def update(self, flock_fishes):
        separation_change = self.separation(flock_fishes, tooClose=50, separation_factor=0.5)
        alignment_change = self.alignment(flock_fishes, visible_distance=50, alignment_factor=0.5)
        cohesion_change = self.cohesion(flock_fishes, visible_distance=50, cohesion_factor=0.5)
        self.velocity += separation_change + alignment_change + cohesion_change

        #Begræns hastigheden til et maksimalt niveau
        max_speed = 5
        if self.velocity.__getLength__() > max_speed:
            self.velocity = self.velocity.normalize() * max_speed

        # Opdaterer positionen ved at lægge velocity til
        self.position += self.velocity

        # Tjek om fisken rammer kanten af skærmen og vend om
        if self.position.get_x() <= 0 or self.position.get_x() >= 750:  # Grænse ved skærmbredde (800 minus fisken på 75px)
            self.velocity = Vector(-self.velocity.get_x(), self.velocity.get_y())  # Vend om i x-retning
        if self.position.get_y() <= 0 or self.position.get_y() >= 550:  # Grænse ved skærmhøjde (600 minus fisken på 75px)
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

    def get_distance_to(self, flock_fishes):
        #Calculate distance to other fishes
        return self.position.distance_to(flock_fishes.position)
    
    def separation(self, flock_fishes, tooClose=50, separation_factor=0.5):
        separation_vector = Vector(0, 0)
        for fish in flock_fishes:
            distance_vector = self.position - fish.position
            distance = distance_vector.length()

            if distance < tooClose:
                separation_vector += distance_vector.normalize() / distance
        return (separation_vector * separation_factor)
    
    def alignment(self, flock_fishes, visible_distance, alignment_factor=0.5):
        alignment_vector = Vector(0, 0)
        count = 0
        for fish in flock_fishes:
            if fish != self:
                distance = self.position.distance_to(fish.position)
                if distance < visible_distance:
                    alignment_vector += fish.velocity
                    count += 1
        if count > 0:
            alignment_vector /= count
            alignment_vector = alignment_vector.normalize() * alignment_factor
        return alignment_vector

    def cohesion(self, flock_fishes, visible_distance, cohesion_factor=0.5):
        cohesion_vector = Vector(0, 0)
        count = 0
        for fish in flock_fishes:
            if fish != self:
                distance = self.position.distance_to(fish.position)
                if distance < visible_distance:
                    cohesion_vector += fish.position
                    count += 1
        if count > 0:
            cohesion_vector /= count
            cohesion_vector = cohesion_vector.normalize() * cohesion_factor
        return cohesion_vector
