# a game where a fish has to eat as much as he can while escaping something
import pygame
import random 
import time
from food import Food
from shark import Shark
from threading import Timer

pygame.init()
screen = pygame.display.set_mode((1200, 900))
clock = pygame.time.Clock()
running = True

bg = pygame.image.load("Earl Wang.jpg")
bg = pygame.transform.scale(bg, (1200,900))

player_img = pygame.image.load("fish.png")

food_img = pygame.transform.scale_by(pygame.image.load("food.png"), 0.1)

shark_img = pygame.image.load("shark.png")

p_x = 0
p_y = 0
# player stats
p_speed = 9

p_hitbox = pygame.Rect(0, 0, 50, 25)

f_x = random.randint(0,1000)
f_y = random.randint(0, 800)
# food stuff
all_food = [Food(), Food(), Food()]

shark = Shark(900, 100)

font = pygame.font.SysFont("timesnewroman", 22)

score = 0
# makes game not crash and clock tick
while running:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False 
    keys_pressed = pygame.key.get_pressed()
# player controls
    if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
        p_y -= p_speed

    if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
        p_y += p_speed

    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
        p_x -= p_speed

    if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
        p_x += p_speed
# player boundaries
    if p_x < 0:
        p_x = 0

    if p_x > 1136:
        p_x = 1136

    if p_y < 0:
        p_y = 0

    if p_y > 868:
        p_y = 868
    # player htiboc
    p_hitbox.x = p_x + 10
    p_hitbox.y = p_y + 5
    screen.blit(bg, (0,0))
    # pygame.draw.rect(screen, "red", p_hitbox)
    screen.blit(player_img, (p_x,p_y))
    # food update
    for food in all_food:
        food.update(screen)
        if p_hitbox.colliderect(food.hitbox):
            score += food.points
            if food.trait == "Speed":
                p_speed = 10
            else
                p_invisiblity = 10
            all_food.remove(food)
            all_food.append(Food())
# shark update
    shark.update(p_hitbox, screen)
    # while True:
    #     shark.update(p_hitbox, screen)
    #     time.sleep(1)
    # score baord
    scoreTxt = font.render("Score: " + str(score), True, "white")
    screen.blit(scoreTxt, (20, 850))

    pygame.display.update()

