import pygame
import pathlib
from random import randint

path_to_walk_gifs = pathlib.Path("./assets/character/walk-frames/")
path_to_idles = pathlib.Path("./assets/character/idles/")
PLAYER_WALK_GIF_locations = [item.name for item in path_to_walk_gifs.glob("**/*") if item.is_file()]
PLAYER_IDLES = [item.name for item in path_to_idles.glob("**/*") if item.is_file()]

class player():
    def __init__(self):
        self.x = 200
        self.y = 400
        self.width = 64 ##x
        self.height = 128 ##y
        self.speed = 11
        self.walk_count = 0
        #PLAYER IMAGES#########################
        self.idles = [pygame.image.load(str(path_to_idles)+"/"+idle) for idle in PLAYER_IDLES]
        self.walk_right = [pygame.image.load(str(path_to_walk_gifs)+"/left_right/"+frame) for frame in PLAYER_WALK_GIF_locations] #Grab all the walk frames in put them here
        self.walk_right = self.resize_self(self.walk_right)
        self.idles = self.resize_self(self.idles)
        self.walk_left = [pygame.transform.flip(frame,True,False) for frame in self.walk_right] #mirror flip all images in walk_right to make the left walk loop
        self.img =  self.idles[0]
        #######################################
        self.usable_keys = [pygame.K_a,pygame.K_d]
        self.walking_right = True
        self.first_move = True
        self.idle = True

    def resize_self(self,image_list):
        resized = []
        for surface in image_list:
            resized.append(pygame.transform.scale(surface,(self.width,self.height)))
        return resized

    def location(self):
        return (self.x,self.y)

    def size(self):
        return (self.width,self.height)

    def move_it(self,key):

        #check if walk count is greater than the number of frames
        #if yes, reset back to starting walk frame
        if self.walk_count >= len(self.walk_right):
            self.walk_count = 0

        #left and right, up and down, and idle
        if (key == "left" or key == "sleft"):
            self.walking_right = False
            self.idle = False

            if key == "left":
                self.img = self.walk_left[self.walk_count]
            elif key == "sleft":
                self.img = self.walk_right[self.walk_count]

            self.walk_count += 1
            self.x -= self.speed

        elif (key == "right" or key == "sright"):
            self.walking_right = True
            self.idle = False

            if key == "right":
                self.img = self.walk_right[self.walk_count]
            elif key == "sright":
                self.img = self.walk_left[self.walk_count]

            self.walk_count += 1
            self.x += self.speed

        elif key == "up":
            self.walking_right=True
            self.idle = False

            self.img=self.walk_right[self.walk_count]
            self.walk_count += 1
            self.y -= self.speed

        elif key == "down":
            self.walking_right=False
            self.idle = False

            self.img=self.walk_left[self.walk_count]
            self.walk_count += 1
            self.y += self.speed

        elif key == "idle":
            #pick a random idle
            if not self.idle:
                random_idle_index = randint(0,len(self.idles)-1)
                self.img = self.idles[random_idle_index]
                self.idle = True


    def drawSelf(self,where):
        where.blit(self.img,(self.x,self.y))
