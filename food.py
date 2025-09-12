import pygame
import random

class Food:
    def __init__(self):
        self.x = random.randint(20,1000)
        self.y = random.randint(20, 600)
        # points its worth
        self.points = random.randint(3,7)
        self.trait = None 
        # selects trait
        self.image = pygame.transform.scale_by(pygame.image.load("food.png"), 0.1 + self.points * 0.01)
        if random.random() < 0.2:
            if random.random() < 0.5:
                self.trait = "Invisibility"
            else:
                self.trait = "Speed"

        self.hitbox = self.image.get_rect()
    

    def update(self, screen):
        self.hitbox.x = self.x
        self.hitbox.y = self.y
        # pygame.draw.rect(screen, "red", self.hitbox)
        screen.blit(self.image, (self.x, self.y))


