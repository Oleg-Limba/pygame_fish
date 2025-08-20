import random
import pygame

class Shark:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.image = (pygame.image.load("shark.png"))
    self.size = random.randint(1, 3)
    if self.size == 1:
      self.speed = 8
    elif self.size == 2:
      self.speed = 6.5
    else:
      self.speed = 5

    
  
  def update(self, p_hitbox, screen):
  # if the fish is going up down right etc then make the picture of the shark point that way
    if self.x > p_hitbox.x:
      self.x -= self.speed
    else:
      self.x += self.speed
    if self.y > p_hitbox.y:
      self.y -= self.speed
    else:
        self.y += self.speed
    screen.blit(self.image, (self.x, self.y))