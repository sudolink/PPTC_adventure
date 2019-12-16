import pygame
import pathlib
from player import *
from game_controls import *
from random import randint

#initialize pygame
pygame.init()

#CONSTANTS
WHITE = (255,255,255)
#print(str(path_to_walk_gifs))
clock = pygame.time.Clock()
#the screen
swidth = 1024
sheight = 786
screen = pygame.display.set_mode((swidth,sheight))

pygame.init()

room =
player_one = create_player()

def draw_screen():
    screen.fill(WHITE)
    player_one.drawSelf(screen)
    pygame.display.flip()
    pygame.display.update()

#game LOOP
running = True
while running:
    clock.tick(12)
    pygame.event.pump()#UPDATE EVENT STATES BEFORE CHECKING THEM
    events = pygame.event.get()
    #imported from game_controls
    for event in events:
        if event.type == pygame.QUIT:
            quit()
    handle_input(player_one)

    draw_screen()


quit()
