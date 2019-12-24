import pygame
import pathlib
from random import randint
import sprites

path_to_walk_gifs = pathlib.Path("./assets/character/walk-frames/")
path_to_idles = pathlib.Path("./assets/character/idles/")
PLAYER_WALK_GIF_locations = [item.name for item in path_to_walk_gifs.glob("**/*") if item.is_file()]
PLAYER_IDLES = [item.name for item in path_to_idles.glob("**/*") if item.is_file()]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tile_size = 32
        self.width = self.tile_size ##x
        self.height = self.tile_size*2 ##y
        self.speed = 10
        #PLAYER IMAGES#########################
        self.idles = [pygame.image.load(str(path_to_idles)+"/"+idle) for idle in PLAYER_IDLES]
        self.idles = self.resize_self(self.idles)
        self.image =  self.idles[0]
        #######################################
        self.rect = self.image.get_rect()
        self.rect.center = (1024/2,786/2) # (x,y)
        #######################################

        #ADD to all sprites: own sprite and bottom sprite
        sprites.all_sprites.add(self)
        sprites.visible_sprites.add(self)

############################## RESIZING LOADED IMAGES
    def resize_self(self,image_list):
        resized = []
        for surface in image_list:
            resized.append(pygame.transform.scale(surface,(self.width,self.height)))
        return resized
