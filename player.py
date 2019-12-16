import pygame
import pathlib
from random import randint

path_to_walk_gifs = pathlib.Path("./assets/character/walk-frames/")
path_to_idles = pathlib.Path("./assets/character/idles/")
PLAYER_WALK_GIF_locations = [item.name for item in path_to_walk_gifs.glob("**/*") if item.is_file()]
PLAYER_IDLES = [item.name for item in path_to_idles.glob("**/*") if item.is_file()]

class create_player():
    def __init__(self):
        self.x = 200
        self.y = 400
        self.width = 64 ##x
        self.height = 128 ##y
        self.speed = 8
        self.walk_count = 0
        #PLAYER IMAGES#########################
        self.idles = [pygame.image.load(str(path_to_idles)+"/"+idle) for idle in PLAYER_IDLES]
        self.walk_right = [pygame.image.load(str(path_to_walk_gifs)+"/left_right/"+frame) for frame in PLAYER_WALK_GIF_locations] #Grab all the walk frames in put them here
        self.walk_right = self.resize_self(self.walk_right)
        self.idles = self.resize_self(self.idles)
        self.walk_left = [pygame.transform.flip(frame,True,False) for frame in self.walk_right] #mirror flip all images in walk_right to make the left walk loop
        self.img =  self.idles[0]
        #######################################
        self.walking_direction = {"down":False,"down_right":False,"right":False,"up_right":False,"up":False,"up_left":False,"left":False,"down-left":False}
        self.first_move = True
        self.is_idle = True
        self.moves = {"down":self.move_down,
                    "right":self.move_right,
                    "up":self.move_up,
                    "left":self.move_left,
                    "down_left":self.move_down_left,
                    "up_left":self.move_up_left,
                    "down_right":self.move_down_right,
                    "up_right":self.move_up_right}

    def resize_self(self,image_list):
        resized = []
        for surface in image_list:
            resized.append(pygame.transform.scale(surface,(self.width,self.height)))
        return resized

    def location(self):
        return (self.x,self.y)

    def size(self):
        return (self.width,self.height)

######### DRAWING FUNCTION
    def drawSelf(self,where):
        where.blit(self.img,(self.x,self.y))



##*#*#*#*#*#*##*#*#*#*#*#*#*#/  MOVEMENT /#*#*#*#*#*#*##*#*#*#*#*#*#*##

    def be_idle(self):
        if not self.is_idle:
            self.img = self.idles[randint(0,len(self.idles)-1)] #set a random still for now
            self.is_idle = True

############## SET WALK GIF
    def right_facing_walk(self):
        self.img = self.walk_right[self.walk_count]
        self.is_idle = False

    def left_facing_walk(self):
        self.img = self.walk_left[self.walk_count]
        self.is_idle = False

############## MOVING
    def move_down(self):
        self.y += self.speed
        self.right_facing_walk()

    def move_right(self):
        self.x += self.speed
        self.right_facing_walk()

    def move_up(self):
        self.y -= self.speed
        self.left_facing_walk()

    def move_left(self):
        self.x -= self.speed
        self.left_facing_walk()

###### DIAGONALS

    def move_down_left(self):
        self.x -= self.speed
        self.y += self.speed
        self.left_facing_walk()

    def move_up_left(self):
        self.x -= self.speed
        self.y -= self.speed
        self.left_facing_walk()

    def move_down_right(self):
        self.x += self.speed
        self.y += self.speed
        self.right_facing_walk()

    def move_up_right(self):
        self.x += self.speed
        self.y -= self.speed
        self.right_facing_walk()

########## MOVE FUNCTION
    def move_it(self,direction):
        #check if walk count is greater than the number of frames
        #if yes, reset back to starting walk frame
        self.walk_count += 1
        if self.walk_count >= len(self.walk_right):
            self.walk_count = 0
        self.moves[direction]()
