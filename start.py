import pygame
import pathlib
from player import *
from game_controls import *
from random import randint
import rooms

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

room_0 = rooms.room((swidth,sheight))

all_sprites = pygame.sprite.Group()
block_sprites = pygame.sprite.Group()
player_one = create_player()

all_sprites.add(player_one)
##make invisiblocks
def create_invisiblock():
    mouse_pos = pygame.mouse.get_pos()
    invisiblock = rooms.invisi_block(mouse_pos[0],mouse_pos[1])
    all_sprites.add(invisiblock)
    block_sprites.add(invisiblock)

player_one.get_collidables(block_sprites)

######### DRAWING FUNCTIONs
def draw_thing(what_surface,what_img,x_y_location):
    what_surface.blit(what_img,x_y_location)

def draw_screen():
    all_sprites.update()
    screen.fill(WHITE)
    draw_thing(screen,room_0.bg,(0,0))
    all_sprites.draw(screen)
    pygame.display.flip()

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
    mouse_pressed = pygame.mouse.get_pressed() #(left,middle,right)
    if mouse_pressed[0]:
        create_invisiblock()
    handle_input(player_one)

    draw_screen()


quit()
