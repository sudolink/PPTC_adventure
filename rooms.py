import pathlib
import pygame

path_to_rooms = pathlib.Path("./assets/rooms/")
path_to_room_blocks = pathlib.Path("./assets/rooms/room_0")

class room():
    def __init__(self,screen_size):
        self.rect = pygame.Rect(0,0,screen_size[0],screen_size[1])
        self.image = pygame.Surface((self.rect.w,self.rect.h))
        #self.image.fill((255,255,99))
        self.rows =  screen_size[1]//64#force an int result with division
        self.collumns = screen_size[0]//64
        #self.generate_room_blocks()

    def single_png_room(self):
        self.bg = pygame.transform.scale(pygame.image.load("./assets/rooms/room_0/room_0.png"),screen_size)
        self.rect = self.bg.get_rect()
        self.rect.center = (screen_size[0]/2,screen_size[1]/2)


class room_tile():
    def __init__(self,x,y):
        self.image = pygame.image.load("./assets/rooms/room_0/floor.png")
        self.image = pygame.transform.scale(self.image,(64,64))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.return_self()

    def return_self(self):
        return self

class invisi_block(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface([40,40])
        self.image.set_alpha(120)
        self.image.fill((255,255,40))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
