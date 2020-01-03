import pathlib
import pygame
import sprites
import random

tile_size = 64
path_to_rooms = pathlib.Path("./assets/rooms/")
path_to_room_blocks = pathlib.Path("./assets/rooms/room_0")

class Room():
    def __init__(self,png_path,invisiwalls_path,screen_size):
        self.tile_map = [] #
        self.tiles = pygame.sprite.Group()
        self.invisiwalls = pygame.sprite.Group()
        self.entry_point = None
        self.image = self.map_from_png(png_path)
        self.tile_map = self.tile_map_from_file(invisiwalls_path)
        self.rect = self.image.get_rect()
        self.offset_for_entry_tile(screen_size)
        self.build_invisiwalls()

    def map_from_png(self,png_path):
        default_tile_size = 16
        image = pygame.image.load(png_path)
        img_rect = image.get_rect()
        new_dimensions = (img_rect.width * (tile_size//default_tile_size),img_rect.height * (tile_size//default_tile_size))
        print(new_dimensions)
        image = pygame.transform.scale(image,new_dimensions)
        return image

    def offset_for_entry_tile(self,screen_size):
        #find entry tile --> 98
        row_loc = None
        col_loc = None
        for row in self.tile_map:
            if "98" in row:
                row_loc = self.tile_map.index(row)
                break
        col_loc = self.tile_map[row_loc].index("98")
        [off_x,off_y] = [row_loc*tile_size,col_loc*tile_size]
        print("map_rect x,y BEFORE: ",self.rect.x,self.rect.y)
        print(off_x,off_y," from ",row_loc,col_loc)
        self.rect.x = off_x - self.rect.width - screen_size[0]/2 + (self.rect.width-off_x)
        self.rect.y = off_y - self.rect.height - screen_size[1]/2
        print("map_rect x,y AFTER: ",self.rect.x,self.rect.y)



    def offset_to_center(self):
        self.rect.x -= self.rect.width/2
        self.rect.y -= self.rect.height/2

    def tile_map_from_file(self,blueprint_path):
        tile_map = []
        with open(blueprint_path,"r") as map:
            for line in map.readlines():
                tile_map.append(line.strip("\n").split(","))
        return tile_map

    def build_invisiwalls(self):
        x = self.rect.x
        y = self.rect.y
        for row in self.tile_map:
            x = self.rect.x
            for tile in row:
                if tile == "11":
                    self.invisiwalls.add(invisi_block(x,y))
                    x += tile_size
                elif tile in ["00","98"]:
                    x += tile_size
                else:
                    print("whoopsie!")
            y += tile_size

    def move_map(self,scroll):
        self.rect.x += scroll[0]
        self.rect.y += scroll[1]
        self.update_children_pos(scroll)

    def update_children_pos(self,scroll):
        for tile in self.tiles:
            tile.rect.x += scroll[0]
            tile.rect.y += scroll[1]
        for tile in self.invisiwalls:
            tile.rect.x += scroll[0]
            tile.rect.y += scroll[1]



class room_tile(pygame.sprite.Sprite):
    def __init__(self,x,y,bg_image_path,tile_code):
        super().__init__()
        self.tile_code = tile_code
        self.dimensions = (tile_size,tile_size)
        self.radius = tile_size - tile_size / 2
        self.image = pygame.image.load(bg_image_path)
        self.image = pygame.transform.scale(self.image,(tile_size,tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.return_self()

    def draw_self(self,surface,x,y):
        surface.blit(self.image,x,y)

    def return_self(self):
        return self

class outline_tile(room_tile):
    def __init__(self,x,y,tile_code):
        super().__init__(x,y,"./assets/rooms/room_0/wall.png",tile_code)
        self.image = pygame.Surface((tile_size,tile_size))
        self.image.set_alpha(0)
        self.image.fill((255,255,40))

class floor_tile(room_tile):
    def __init__(self,x,y,tile_code):
        self.image_path = random.choice(["./assets/rooms/room_0/floor.png","./assets/rooms/room_0/floor_0.png"])
        super().__init__(x,y,self.image_path,tile_code)

class object_tile(room_tile):
    def __init__(self,x,y,tile_code):
        self.image_path = "./assets/rooms/room_0/object.png"
        super().__init__(x,y,self.image_path,tile_code)

class door_tile(room_tile):
    def __init__(self,x,y,tile_code):
        self.image_path = "./assets/rooms/room_0/door.png"
        super().__init__(x,y,self.image_path,tile_code)

class wall_tile(room_tile):
    def __init__(self,x,y,tile_code):
        self.image_path = "./assets/rooms/room_0/wall.png"
        super().__init__(x,y,self.image_path,tile_code)

class invisi_block(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.dimensions = (tile_size,tile_size)
        self.image = pygame.Surface(self.dimensions)
        self.image.set_alpha(0)
        self.image.fill((255,255,40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.radius = self.dimensions[0] - self.dimensions[0] / 4


def create_invisiblock(x,y):
    invisiblock = invisi_block(x,y)
    sprites.all_sprites.add(invisiblock)
    sprites.block_sprites.add(invisiblock)
