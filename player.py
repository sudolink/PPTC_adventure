import pygame
import pathlib
from random import randint
import sprites

path_to_walk_gifs_RIGHT = pathlib.Path("./assets/character/walk-frames/RIGHT")
path_to_walk_gifs_LEFT = pathlib.Path("./assets/character/walk-frames/LEFT")
path_to_walk_gifs_UP = pathlib.Path("./assets/character/walk-frames/UP")
path_to_walk_gifs_DOWN = pathlib.Path("./assets/character/walk-frames/DOWN")
path_to_idles = pathlib.Path("./assets/character/idles/")
PLAYER_IDLES = [item.name for item in path_to_idles.glob("**/*") if item.is_file()]

walk_timer = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self,loc,tile_size):
        super().__init__()
        self.tile_size = tile_size
        self.width = self.tile_size ##x
        self.height = self.tile_size*2 ##y
        #PLAYER IMAGES#########################
        self.idles = [pygame.image.load(str(path_to_idles)+"/"+idle) for idle in PLAYER_IDLES]
        self.walking_gifs = {"left":None,"right":None,"up":None,"down":None}
        self.load_walks()
        self.walk_frame = 0
        self.idles = self.resize_self(self.idles)

        self.image =  self.idles[0]
        #######################################
        self.rect = self.image.get_rect()
        self.rect.center = loc
        #######################################

        #ADD to all sprites: own sprite and bottom sprite
        sprites.player_sprite.add(self)

############################## RESIZING LOADED IMAGES
    def resize_self(self,image_list):
        resized = []
        for surface in image_list:
            resized.append(pygame.transform.scale(surface,(self.width,self.height)))
        return resized

############################### LOAD walking_gifs

    def load_walks(self):
        walk_right = []
        for num in range(0,12):
            frame = pygame.image.load(str(path_to_walk_gifs_RIGHT)+"\\{}_frame.png".format(num))
            walk_right.append(frame)

        walk_left = []
        for num in range(0,12):
            frame = pygame.image.load(str(path_to_walk_gifs_LEFT)+"\\{}_frame.png".format(num))
            walk_left.append(frame)

        walk_up = []
        for num in range(0,12):
            frame = pygame.image.load(str(path_to_walk_gifs_UP)+"\\{}_frame.png".format(num))
            walk_up.append(frame)

        walk_down = []
        for num in range(0,12):
            frame = pygame.image.load(str(path_to_walk_gifs_DOWN)+"\\{}_frame.png".format(num))
            walk_down.append(frame)

        self.walking_gifs["left"] = self.resize_self(walk_left)
        self.walking_gifs["right"] = self.resize_self(walk_right)
        self.walking_gifs["up"] = self.resize_self(walk_up)
        self.walking_gifs["down"] = self.resize_self(walk_down)
        del walk_right,walk_left,walk_up,walk_down
###############################
    def animate_walk(self,direction):

        try:
            self.walking_gifs[direction]
        except:
            pass
        else:
            if self.walk_frame == 12:
                self.walk_frame = 0
            self.image = self.walking_gifs[direction][self.walk_frame]
            walk_timer.tick(20)
            self.walk_frame += 1

    def move(self,scroll,direction):
        #self.rect.x += scroll[0]
        #self.rect.y += scroll[1]
        self.animate_walk(direction)
