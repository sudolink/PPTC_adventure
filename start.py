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
room_tiles = []
all_sprites.add(player_one)
##make invisiblocks

player_one.get_collidables(block_sprites)

######### DRAWING FUNCTIONs
def create_invisiblock():
    mouse_pos = pygame.mouse.get_pos()
    invisiblock = rooms.invisi_block(mouse_pos[0],mouse_pos[1])
    all_sprites.add(invisiblock)
    block_sprites.add(invisiblock)

def generate_room_blocks():
    rows = room_0.rows
    collumns = room_0.collumns
    print(rows,collumns)
    x = 64
    y = 64
    for row in range(rows-2):
        for collumn in range(collumns-2):
            new_tile = rooms.room_tile(x,y)
            room_tiles.append(new_tile)
            x+=new_tile.rect.w
        x = 64
        y += new_tile.rect.h

def draw_things(what_surface,what_img,x_y_location):
    if type(what_img) == list:
        for image in what_img:
            what_surface.blit(image.image,image.rect.center)
    else:
        what_surface.blit(what_img,x_y_location)

def draw_screen():
    all_sprites.update()
    screen.fill(WHITE)
    draw_things(screen,room_0.image,(0,0))
    draw_things(screen,room_tiles,None)
    all_sprites.draw(screen)
    pygame.display.flip()

generate_room_blocks()
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
        create_invisiblock()

    draw_screen()


quit()
