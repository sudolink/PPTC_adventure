import pygame
import pathlib
from player import *
from game_controls import *
from random import randint
import rooms
import time
import sprites
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
screen_center = (swidth/2,sheight/2)
screen = pygame.display.set_mode((swidth,sheight)) #,pygame.FULLSCREEN,16
scroll = [0,0] #x,y
pygame.init()

########## init objects

map_0_blueprint = "./assets/rooms/room_0/room_0.txt"
room_0 = rooms.room(map_0_blueprint)
viewport = camera.Camera()
print(viewport.player)
######### DRAWING FUNCTIONs

def draw_things(what_surface,what_img,x_y_location):
    if type(what_img) == list:
        for image in what_img:
            what_surface.blit(image.image,image.rect.center)
    else:
        what_surface.blit(what_img,x_y_location)

def adjust_sprites_for_scroll(sprite_list,scroll):
    for sprite in sprite_list:
        sprite.rect.center[0] = sum([sprite.rect.center[0],scroll[0]])
        sprite.rect.center[1] = sum([sprite.rect.center[1],scroll[1]])


def draw_screen():
    sprites.find_visible_sprites(viewport.colliding_sprites())
    sprites.visible_sprites.update()
    screen.fill(BLACK)
    sprites.visible_sprites.draw(screen)
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

    handle_input(viewport.player)

    ### temporary - for testing collisions
    mouse_pressed = pygame.mouse.get_pressed() #(left,middle,right)
    if mouse_pressed[0]:
        mouse_pos = pygame.mouse.get_pos()
        rooms.create_invisiblock(mouse_pos[0],mouse_pos[1])


    draw_screen()


quit()
