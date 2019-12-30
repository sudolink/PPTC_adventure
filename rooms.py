import pathlib
import pygame
import sprites
import random

tile_size = 64
path_to_rooms = pathlib.Path("./assets/rooms/")
path_to_room_blocks = pathlib.Path("./assets/rooms/room_0")

class Room():
    def __init__(self,blueprint_path,screen_size):
        self.tile_map = [] #
        self.tiles = pygame.sprite.Group()
        self.invisiwalls = pygame.sprite.Group()
        self.entry_point = None
        self.tile_map_from_file(blueprint_path)
        self.dimensions = (len(self.tile_map[0])*tile_size,len(self.tile_map)*tile_size)
        self.width = self.dimensions[0]
        self.height = self.dimensions[1]
        self.image = pygame.Surface((self.width,self.height))
        self.rect = self.image.get_rect()
        self.image.set_alpha(255)
        self.image.fill((255,10,255))
        self.entry_loc = (0,0)
        self.build_from_blueprint()
        self.offset_for_entry_tile(screen_size) #offset layout to center on entry door
        self.build_invisiwalls()
        # print(self.entry_loc)
        # print(self.dimensions)

    def tile_map_from_file(self,blueprint_path):
        with open(blueprint_path,"r") as map:
            for line in map.readlines():
                self.tile_map.append(line.strip("\n").split(","))

    def build_invisiwalls(self):
        for tile in self.tiles:
            if tile.tile_code in ["00","01","33"]: #emptyspace, wall, or object
                tile_pos = tile.rect.center
                invisiblock = invisi_block(tile_pos[0],tile_pos[1])
                self.invisiwalls.add(invisiblock)

    def build_from_blueprint(self):
        y = self.rect.y
        for line in self.tile_map:
            x = self.rect.x
            for tile in line:
                if tile == "00":
                    outline = outline_tile(x,y,tile)
                    self.tiles.add(outline)
                    x += tile_size
                elif tile == "01":
                    wall = wall_tile(x,y,tile)
                    self.tiles.add(wall)
                    x += tile_size
                elif tile == "02":
                    floor = floor_tile(x,y,tile)
                    self.tiles.add(floor)
                    x += tile_size
                elif tile == "33":
                    object = object_tile(x,y,tile)
                    self.tiles.add(object)
                    x += tile_size
                elif tile == "99":
                    door = door_tile(x,y,tile)
                    self.tiles.add(door)
                    x += tile_size
                elif tile == "98":
                    door = door_tile(x,y,tile)
                    self.entry_point = door.rect.center
                    self.tiles.add(door)
                    x += tile_size
                else:
                    print("build_from_blueprint went horribly wrong!")
            y += tile_size

    def offset_for_entry_tile(self,screen_size):
        #find entry tile --> 98
        offset = [tile.rect.center for tile in self.tiles if tile.tile_code == "98"][0]
        self.entry_loc = (screen_size[0]/2-200,screen_size[1]/2)
        for tile in self.tiles:
            tile.rect.x -= offset[0] - screen_size[0]/2
            tile.rect.y -= offset[1] - screen_size[1]/1.2

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
        self.rect.center = (x,y)
        self.return_self()

    def draw_self(self,surface,x,y):
        surface.blit(self.image,x,y)

    def return_self(self):
        return self

class outline_tile(room_tile):
    def __init__(self,x,y,tile_code):
        super().__init__(x,y,"./assets/rooms/room_0/wall.png",tile_code)
        self.image = pygame.Surface((tile_size,tile_size))
        self.image.set_alpha(40)
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
        self.image.set_alpha(90)
        self.image.fill((255,255,40))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.radius = self.dimensions[0] - self.dimensions[0] / 4


def create_invisiblock(x,y):
    invisiblock = invisi_block(x,y)
    sprites.all_sprites.add(invisiblock)
    sprites.block_sprites.add(invisiblock)
