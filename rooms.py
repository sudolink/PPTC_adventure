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
        self.room_tiles = []
        self.generate_room_blocks()

    def single_png_room(self):
        self.bg = pygame.transform.scale(pygame.image.load("./assets/rooms/room_0/room_0.png"),screen_size)
        self.rect = self.bg.get_rect()
        self.rect.center = (screen_size[0]/2,screen_size[1]/2)

    def generate_room_blocks(self):
        rows = self.rows
        collumns = self.collumns
        x = 64
        y = 64
        for row in range(rows-2):
            for collumn in range(collumns-2):
                new_tile = room_tile(x,y)
                self.room_tiles.append(new_tile)
                x+=new_tile.rect.w
            x = 64
            y += new_tile.rect.h

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


def create_invisiblock():
    blocks = []
    mouse_pos = pygame.mouse.get_pos()
    invisiblock = invisi_block(mouse_pos[0],mouse_pos[1])
    blocks.append(invisiblock)
    return blocks
