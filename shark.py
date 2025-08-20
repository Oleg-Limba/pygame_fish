import random
import pygame

class Shark:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.image = (pygame.image.load("shark.png"))
    self.size = random.randint(1, 3)
    if self.size == 1:
      self.speed = 4
    elif self.size == 2:
      self.speed = 3.5
    else:
      self.speed = 2
    self.facing_left = True
    

    
  
  def update(self, p_hitbox, screen):
  # if the fish is going up down right etc then make the picture of the shark point that way
    if self.x + 100 > p_hitbox.x:
      self.x -= min(self.speed, abs(self.x + 100 - p_hitbox.x))
      self.facing_left = True
    else:
      self.x += min(self.speed, abs(self.x + 100 - p_hitbox.x))
      self.facing_left = False
    if self.y + 75 > p_hitbox.y:
      self.y -= min(self.speed, abs(self.y + 75 - p_hitbox.y))
    else:
        self.y += min(self.speed, abs(self.y + 75 - p_hitbox.y))

    screen.blit(pygame.transform.flip(self.image, not self.facing_left, False), (self.x, self.y))