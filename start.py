import pygame
import pathlib
import player
from game_controls import *
from random import randint
import time
import sprites
import rooms
import camera

#initialize pygame
pygame.init()

#CONSTANTS
WHITE = (255,255,255)
BLACK = (0,0,0)
#print(str(path_to_walk_gifs))
clock = pygame.time.Clock()
#the screen
swidth = 1024
sheight = 786
screen_size = (swidth,sheight)
screen_center = (swidth/2,sheight/2)
player_start_pos = (screen_center[0],screen_center[1]+rooms.tile_size)
screen = pygame.display.set_mode((swidth,sheight)) #,pygame.FULLSCREEN,16
pygame.init()

########## init objects

room_0 = rooms.Room("./assets/rooms/room_0/room_0.txt",screen_size)
viewport = camera.Viewport(screen_size)
player_0 = player.Player(player_start_pos,rooms.tile_size)
######### DRAWING FUNCTIONs

def draw_things(what_surface,what_img,x_y_location):
    if type(what_img) == list:
        for image in what_img:
            what_surface.blit(image.image,image.rect.center)
    else:
        what_surface.blit(what_img,x_y_location)

def draw_screen():
    room_0.tiles.update()
    room_0.invisiwalls.update()
    sprites.all_sprites.update()
    sprites.player_sprite.update()
    sprites.inner_view_sprite.update()
    screen.fill(BLACK)
    room_0.tiles.draw(screen)
    sprites.all_sprites.draw(screen)
    sprites.inner_view_sprite.draw(screen)
    room_0.invisiwalls.draw(screen)

    player_0.shadow.cast_shadow()
    screen.blit(player_0.shadow.image,player_0.shadow.rect.center)

    sprites.player_sprite.draw(screen)
    sprites.inner_view_sprite.draw(screen)
    pygame.display.flip()

########## game LOOP #########
running = True

while running:
    clock.tick(60)
    pygame.event.pump()#UPDATE EVENT STATES BEFORE CHECKING THEM
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    handle_input(room_0,player_0,viewport)

    ### temporary - for testing collisions
    mouse_pressed = pygame.mouse.get_pressed() #(left,middle,right)
    if mouse_pressed[0]:
        mouse_pos = pygame.mouse.get_pos()

    draw_screen()


quit()
