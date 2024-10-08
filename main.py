import pygame
from pygame.locals import *
from vector import *
from fish import Fish
from flock import Flock

# pygame setup
#initialiserer alle de nødvendige moduler, der kræves for at bruge Pygame. Pygame består af flere moduler, hver med sit eget formål, såsom grafik, lyd, inputhåndtering osv.
#pygame.init() returnerer funktionen to værdier: en tæller af hvor mange moduler, der blev initialiseret korrekt, og en tæller af hvor mange moduler, der mislykkedes i at initialisere.
pygame.init()
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)


#opretter et objekt af typen Clock`-objekt, til at styre hvor lang tid der går mellem hver iteration i lykken.
clock = pygame.time.Clock()
running = True

fish = Fish(Vector(400, 300), Vector(1, 1), 'Fisk.png', vision_range=1)
flock = Flock(15, screen_size)

while running:
    
    #Denne linje henter en liste over alle hændelser (events), som er sket siden sidste gang, løkken kørte. 
    for event in pygame.event.get():

        #Denne event sker typisk når vinduet lukkes
        if event.type == pygame.QUIT:
            running = False

    #Lav en baggrundsfarve
    screen.fill((0, 128, 255))
    
    #Tegn fisken
    flock.draw(screen)

    # opdatere fisken
    flock.update()

    #Flip, så vores tegning kommer på skærmen.
    pygame.display.flip()

    #60 frames pr sekund. Dvs løkken skal gentages 60 gange i sekundet.
    clock.tick(60)  

pygame.quit()