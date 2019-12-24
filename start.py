import pygame
import pathlib
from player import *
from game_controls import *
from random import randint
import time
import sprites
import camera
import rooms

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
pygame.init()

########## init objects

room_0 = rooms.Room("./assets/rooms/room_0/room_0.txt")
viewport = camera.Camera(room_0.entry_point)
######### DRAWING FUNCTIONs

def draw_things(what_surface,what_img,x_y_location):
    if type(what_img) == list:
        for image in what_img:
            what_surface.blit(image.image,image.rect.center)
    else:
        what_surface.blit(what_img,x_y_location)

def draw_screen():
    sprites.all_sprites.update()
    room_0.tiles.update()
    screen.fill(BLACK)
    room_0.tiles.draw(screen)
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

    handle_input(room_0)

    ### temporary - for testing collisions
    mouse_pressed = pygame.mouse.get_pressed() #(left,middle,right)
    if mouse_pressed[0]:
        mouse_pos = pygame.mouse.get_pos()

    draw_screen()


quit()
