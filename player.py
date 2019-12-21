import pygame
import pathlib
from random import randint
import sprites

path_to_walk_gifs = pathlib.Path("./assets/character/walk-frames/")
path_to_idles = pathlib.Path("./assets/character/idles/")
PLAYER_WALK_GIF_locations = [item.name for item in path_to_walk_gifs.glob("**/*") if item.is_file()]
PLAYER_IDLES = [item.name for item in path_to_idles.glob("**/*") if item.is_file()]

class bottom_half(pygame.sprite.Sprite):
    def __init__(self,parent):
        super().__init__()
        self.dimensions = (parent.width,parent.height / 4)
        self.image = pygame.Surface(self.dimensions)
        self.image.fill((200,20,200))
        self.image.set_alpha(120)
        self.rect = self.image.get_rect()
        self.radius = int(self.dimensions[0] / 5)
        pygame.draw.circle(self.image,(255,255,255),self.rect.center,self.radius) #circle(surface, color, center, radius) -> Rect
        self.update_position(parent.rect.x,parent.rect.y)
        self.get_collidables(sprites.block_sprites)

    def update_position(self,parent_x,parent_y):
        self.rect.x = parent_x
        self.rect.y = parent_y + self.dimensions[1] * 3

    def circled_collision(self, colliders):
        circled_collisions = []
        for collision in colliders:
                if pygame.sprite.collide_circle(self,collision):
                    circled_collisions.append(collision)
        return circled_collisions

    def check_collision(self):
        block_hit_list = pygame.sprite.spritecollide(self, self.collidables, False)
        return block_hit_list

    def get_collidables(self,collidable_list):
        self.collidables = collidable_list



class create_player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
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
        self.image =  self.idles[0]
        #######################################
        self.rect = self.image.get_rect()
        self.rect.center = (1024/2,786/2) # (x,y)
        self.bottom = bottom_half(self)
        #######################################
        self.walking_direction = {"down":False,"down_right":False,"right":False,"up_right":False,"up":False,"up_left":False,"left":False,"down-left":False}
        self.moving = False
        self.direction = None
        self.moves = {"down":self.move_down,
                    "right":self.move_right,
                    "up":self.move_up,
                    "left":self.move_left,
                    "down_left":self.move_down_left,
                    "up_left":self.move_up_left,
                    "down_right":self.move_down_right,
                    "up_right":self.move_up_right}
        self.moves_opposites = [["down","up"],
                                ["left","right"],
                                ["up_left","down_right"],
                                ["down_left","up_right"]]
        #ADD to all sprites: own sprite and bottom sprite
        sprites.all_sprites.add(self.bottom,self)

#*#*#*#*#*#*##*#*#*#*#*#*##**#*#/  COLLISION  /*#*#*#*#*#*#*#*##*#*#*#*#*#*##*
    def prevent_movement_into_colliding_object(self):
        collisions = self.bottom.check_collision()
        circled_collisions = self.bottom.circled_collision(collisions)
        if len(collisions) > 0:
            for obj in collisions:
                if self.direction != "idle":
                    opposite = self.get_opposite_move(self.direction)
                    self.moves[opposite]()
                    return [a for a in self.moves_opposites if a != opposite][0]

############################## RESIZING LOADED IMAGES
    def resize_self(self,image_list):
        resized = []
        for surface in image_list:
            resized.append(pygame.transform.scale(surface,(self.width,self.height)))
        return resized


##*#*#*#*#*#*##*#*#*#*#*#*#*#/  MOVEMENT /#*#*#*#*#*#*##*#*#*#*#*#*#*##

    #return the opposite of the current direction
    def get_opposite_move(self,move):
        for move_pair in self.moves_opposites:
            if move in move_pair:
                return [a for a in move_pair if a != move][0]

    #set idle - will handle idle animations in future
    def be_idle(self):
        if self.moving:
            self.image = self.idles[randint(0,len(self.idles)-1)] #set a random still for now
            self.moving = False

############## SET WALK GIF
    def right_facing_walk(self):
        self.image = self.walk_right[self.walk_count]
        self.moving = True

    def left_facing_walk(self):
        self.image = self.walk_left[self.walk_count]
        self.moving = True

############## MOVING
    def move_it(self,direction):
        #check if walk count is greater than the number of frames
        #if yes, reset back to starting walk frame
        self.walk_count += 1
        if self.walk_count >= len(self.walk_right):
            self.walk_count = 0
        self.moves[direction]()
        self.bottom.update_position(self.rect.x,self.rect.y)
############## DIRECTION FUNCTIONS
    def move_down(self):
        self.rect.y += self.speed
        self.right_facing_walk()
        self.direction = "down"

    def move_right(self):
        self.rect.x += self.speed
        self.right_facing_walk()
        self.direction = "right"

    def move_up(self):
        self.rect.y -= self.speed
        self.left_facing_walk()
        self.direction = "up"

    def move_left(self):
        self.rect.x -= self.speed
        self.left_facing_walk()
        self.direction = "left"

###### DIAGONAL WALKS

    def move_down_left(self):
        self.rect.x -= self.speed
        self.rect.y += self.speed
        self.left_facing_walk()
        self.direction = "down_left"

    def move_up_left(self):
        self.rect.x -= self.speed
        self.rect.y -= self.speed
        self.left_facing_walk()
        self.direction = "up_left"

    def move_down_right(self):
        self.rect.x += self.speed
        self.rect.y += self.speed
        self.right_facing_walk()
        self.direction = "down_right"

    def move_up_right(self):
        self.rect.x += self.speed
        self.rect.y -= self.speed
        self.right_facing_walk()
        self.direction = "up_right"
