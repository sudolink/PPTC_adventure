import pygame
import pathlib
from player import *
from game_controls import *
from random import randint
import rooms
import time
import sprites

#initialize pygame
pygame.init()

#CONSTANTS
WHITE = (255,255,255)
BLACK = (0,0,0)
#print(str(path_to_walk_gifs))
clock = pygame.time.Clock()
#the screen
swidth = 1024
sheight = 896
screen = pygame.display.set_mode((swidth,sheight))

pygame.init()

########## init objects
room_0 = rooms.room((swidth,sheight))
player_one = create_player()

######### DRAWING FUNCTIONs

def draw_things(what_surface,what_img,x_y_location):
    if type(what_img) == list:
        for image in what_img:
            what_surface.blit(image.image,image.rect.center)
    else:
        what_surface.blit(what_img,x_y_location)

def draw_screen():
    sprites.all_sprites.update()
    screen.fill(BLACK)
    draw_things(screen,room_0.room_tiles,None)
    sprites.all_sprites.draw(screen)
    pygame.display.flip()

########## game LOOP
running = True
while running:
    clock.tick(12)
    pygame.event.pump()#UPDATE EVENT STATES BEFORE CHECKING THEM
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()

    handle_input(player_one)

    ### temporary - for testing collisions
    mouse_pressed = pygame.mouse.get_pressed() #(left,middle,right)
    if mouse_pressed[0]:
        invisiblocks = rooms.create_invisiblock()
        for invisiblock in invisiblocks:
            sprites.all_sprites.add(invisiblock)
            sprites.block_sprites.add(invisiblock)

    draw_screen()


quit()
