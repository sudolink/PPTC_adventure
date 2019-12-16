import pygame
import pathlib
from testing_classes import *
from player import *

#initialize pygame
pygame.init()

#CONSTANTS
WHITE = (255,255 ,255)
#print(str(path_to_walk_gifs))
clock = pygame.time.Clock()
#the screen
swidth = 800
sheight = 600
screen = pygame.display.set_mode((swidth,sheight))

pygame.init()


player_one = player()

def draw_screen():
    screen.fill(WHITE)
    player_one.drawSelf(screen)
    pygame.display.flip()
    pygame.display.update()

#game LOOP
running = True
while running:
    clock.tick(12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]:
        if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
            player_one.move_it("sleft")
        else:
            player_one.move_it("left")
    elif pressed[pygame.K_d]:
        if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
            player_one.move_it("sright")
        else:
            player_one.move_it("right")
    elif pressed[pygame.K_w]:
        player_one.move_it("up")
    elif pressed[pygame.K_s]:
        player_one.move_it("down")
    elif not any(pressed):
        player_one.move_it("idle")



    draw_screen()


quit()
