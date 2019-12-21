import pathlib
import pygame
import sprites

tile_size = 64
path_to_rooms = pathlib.Path("./assets/rooms/")
path_to_room_blocks = pathlib.Path("./assets/rooms/room_0")

class room():
    def __init__(self,blueprint_path):
        self.tile_map = [] #
        self.tiles = []
        self.tile_map_from_file(blueprint_path)
        self.build_from_blueprint()
        self.dimensions = (len(self.tile_map[0])*tile_size,len(self.tile_map)*tile_size)
        print(self.dimensions)

    def tile_map_from_file(self,blueprint_path):
        with open(blueprint_path,"r") as map:
            for line in map.readlines():
                self.tile_map.append(line.strip("\n").split(","))

    def build_from_blueprint(self):

        y = 0
        for line in self.tile_map:
            x = 0
            for tile in line:
                if tile == "00":
                    x += tile_size
                elif tile == "01":
                    wall = wall_tile(x,y)
                    self.tiles.append(wall)
                    sprites.all_sprites.add(wall)
                    sprites.block_sprites.add(wall)
                    x += tile_size
                elif tile == "02":
                    floor = floor_tile(x,y)
                    self.tiles.append(floor)
                    sprites.all_sprites.add(floor)
                    x += tile_size
                elif tile == "33":
                    object = object_tile(x,y)
                    self.tiles.append(object)
                    sprites.all_sprites.add(object)
                    sprites.block_sprites.add(object)
                    x += tile_size
                elif tile == "99":
                    door = door_tile(x,y)
                    self.tiles.append(door)
                    sprites.all_sprites.add(door)
                    x += tile_size
                else:
                    print("build_from_blueprint went horribly wrong!")
            y += tile_size



class room_tile(pygame.sprite.Sprite):
    def __init__(self,x,y,bg_image_path):
        super().__init__()
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

class floor_tile(room_tile):
    def __init__(self,x,y):
        self.image_path = "./assets/rooms/room_0/floor.png"
        super().__init__(x,y,self.image_path)

class object_tile(room_tile):
    def __init__(self,x,y):
        self.image_path = "./assets/rooms/room_0/object.png"
        super().__init__(x,y,self.image_path)

class door_tile(room_tile):
    def __init__(self,x,y):
        self.image_path = "./assets/rooms/room_0/door.png"
        super().__init__(x,y,self.image_path)

class wall_tile(room_tile):
    def __init__(self,x,y):
        self.image_path = "./assets/rooms/room_0/wall.png"
        super().__init__(x,y,self.image_path)

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
