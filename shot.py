import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
            
    #in main, maak een nieuwe groep met alle SHOT objects.
    #in player, maak een shoot methode.
        #deze maakt een nieuwe shot aan op de positie van de player