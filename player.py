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
        self.direction = "up"
        self.opposite_direction = {"up":"down","left":"right","up_left":"down_right","up_right":"down_left",
                                "down":"up","right":"left","down_right":"up_left","down_left":"up_right"}
        self.image =  self.idles[0]
        #######################################
        self.rect = self.image.get_rect()
        self.rect.center = loc
        #######################################
        #ADD to all sprites: own sprite and bottom sprite
        self.collision_rect = Player_collision_block(self,self.width)
        self.shadow = Player_shadow(self,tile_size)
        sprites.player_sprite.add(self,self.collision_rect)

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
        self.resize_collision_block()
        self.animate_walk(direction)
        self.direction = direction

    def be_idle(self):
        self.image = self.idles[0]

    def resize_collision_block(self):
        udi_width = self.width /2
        strafe_width = self.width
        lr_width = self.width
        if self.direction in ["up","down","idle"]:
            sprites.player_sprite.remove(self.collision_rect)
            self.collision_rect = Player_collision_block(self,udi_width)
            sprites.player_sprite.add(self.collision_rect)
        elif self.direction in ["left","right"]:
            sprites.player_sprite.remove(self.collision_rect)
            self.collision_rect = Player_collision_block(self,lr_width)
            sprites.player_sprite.add(self.collision_rect)
        else:
            sprites.player_sprite.remove(self.collision_rect)
            self.collision_rect = Player_collision_block(self,strafe_width)
            sprites.player_sprite.add(self.collision_rect)



###############################
class Player_collision_block(pygame.sprite.Sprite):
    def __init__(self,other,width):
        super().__init__()
        self.width = width
        self.height = other.height/8
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill((0,100,255))
        self.image.set_alpha(77)
        self.rect = self.image.get_rect()
        self.rect.center = other.rect.center
        self.rect.y += other.height/2 - self.height/2

    def check_collision(self,colliding_sprite_list):
        return pygame.sprite.spritecollide(self,colliding_sprite_list,False)


class Player_shadow():
    def __init__(self,other,tile_size):
        self.width = tile_size
        self.height = tile_size/2
        self.image = pygame.Surface((self.width,self.height),pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = other.rect.center
        self.rect.y = other.rect.y + other.rect.height - self.height * 1.3
        self.rect.x = other.rect.x - self.width / 2


    def cast_shadow(self):
        pygame.draw.ellipse(self.image,(0,0,0,60),self.image.get_rect())
        #pygame.draw.rect(self.image,(0,0,255,150),self.image.get_rect(),10)
