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
sheight = 896
screen = pygame.display.set_mode((swidth,sheight))

pygame.init()


room_0_bg = pygame.transform.scale(pygame.image.load("./assets/rooms/room_0/room_0.png"),(swidth,sheight))
room_0_rect = room_0_bg.get_rect()
room_0_rect.center = (swidth/2,sheight/2)

player_one = create_player()



######### DRAWING FUNCTIONs
def draw_thing(what_surface,what_img,x_y_location):
    what_surface.blit(what_img,x_y_location)

def draw_screen():
    draw_thing(screen,room_0_bg,room_0_rect)
    draw_thing(screen,player_one.img,(player_one.x,player_one.y))
    pygame.display.flip()
    pygame.display.update()

########## game LOOP
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
