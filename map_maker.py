#map_loader
import pygame
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from tkinter import *
import os
from rooms import tile_size


pg_wsize = (1600,1200)
root = tk.Tk()
py_frame = tk.Frame(root, width = 1600, height = 1200) #creates embed frame for pygame window
py_frame.grid(columnspan = (600), rowspan = 500) # Adds grid
py_frame.pack(side = RIGHT) #packs window to the left


file_sec_heading = tk.Frame(root, width = 100, height = 786)
file_buttons = tk.Frame(root, width = 100, height = 786)
loaded_file_sec = tk.Frame(root)

file_sec_heading.pack(side = TOP)
file_buttons.pack(side = TOP)
loaded_file_sec.pack(side = TOP)

os.environ['SDL_WINDOWID'] = str(py_frame.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

screen = pygame.display.set_mode(pg_wsize)
screen.fill(pygame.Color(0,0,0))
loaded_file_name = "No map loaded"

map = None
map_layer = pygame.sprite.GroupSingle()


class Tile(pygame.sprite.Sprite):
    def __init__(self,tile_size,loc_tuple):
        super().__init__()
        self.base_tile_size = tile_size
        self.current_tile_size = self.base_tile_size
        self.make_surface((tile_size,tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = loc_tuple[0]
        self.rect.y = loc_tuple[1]

    def make_surface(self,dimensions):
        self.image = pygame.Surface(dimensions)
        self.image.fill((155,155,30))
        self.image.set_alpha(90)

    def resize(self,scaler):
        if self.not_negative_resize(scaler):
            del self.image
            nwidth = self.current_tile_size + scaler
            nheight = self.current_tile_size + scaler
            self.make_surface((nwidth,nheight))
            self.rect = self.image.get_rect()

    def not_negative_resize(self,scaler):
        return (self.rect.width + scaler > self.base_tile_size and self.rect.height + scaler > self.base_tile_size)

class Map(pygame.sprite.Sprite):
    def __init__(self,path,screen_size):
        super().__init__()
        self.base_tile_size = 16
        self.current_tile_size = self.base_tile_size
        self.image_path = path
        self.image = pygame.image.load(self.image_path)
        #self.image = pygame.transform.scale(self.image,())
        self.rect = self.image.get_rect()
        self.initial_dimensions = (self.rect.width,self.rect.height)
        self.rect.center = (self.rect.width/2,self.rect.height/2)
        self.rect.x = screen_size[0]/2 - self.rect.width/2
        self.rect.y = screen_size[1]/2 - self.rect.height/2
        self.tiles = []
        self.tile_sprites = pygame.sprite.Group()
        self.make_tiles()

    def resize(self,scaler):
        if self.not_negative_resize(scaler):
            del self.image
            self.image = pygame.image.load(self.image_path)
            self.image = pygame.transform.scale(self.image,(self.rect.width+scaler,self.rect.height+scaler))
            self.rect = self.image.get_rect()
            self.rect.center = (self.rect.width//2,self.rect.height//2)
            self.resize_tiles(scaler)

    def resize_tiles(self,scaler):
        for row in self.tiles:
            for tile in row:
                tile.resize(scaler)

    def make_tiles(self):
        tiles_x = self.rect.width // self.base_tile_size
        tiles_y = self.rect.height // self.base_tile_size
        x = self.rect.x
        y = self.rect.y
        for row in range(0,tiles_y):
            self.tiles.append([])
            for tile in range(0,tiles_x):
                self.tiles[row].append(Tile(self.base_tile_size,(x,y)))
                x += self.base_tile_size
                print(tile)
            x = self.rect.x
            y += self.base_tile_size

        for row in self.tiles:
            for tile in row:
                self.tile_sprites.add(tile)

        #print("###################\n16x16 tiles on:\n\t\tx axis: {}\n\t\ty axis: {}".format(tiles_x, tiles_y))


    def not_negative_resize(self,scaler):
        return (self.rect.width + scaler > self.initial_dimensions[0] and self.rect.height + scaler > self.initial_dimensions[1])


def load_file():
    fname = askopenfilename(filetypes=(("PNG Room", "*.png"),))
    if fname:
        try:
            png_map = pygame.image.load(fname)
        except:
            showerror("Open Source File", "Failed to read file\n'%s'" % fname)
        else:
            construct_map_obj(fname)
            loaded_file_name = fname
            del png_map
        return

def construct_map_obj(png):
    global map
    global pg_wsize
    map = Map(png,pg_wsize)
    map_layer.add(map)

pygame.display.init()

def draw_pygame():
    screen.fill((0,34,55))
    if len(map_layer) > 0:
        map_layer.update()
        map.tile_sprites.update()
        map_layer.draw(screen)
        map.tile_sprites.draw(screen)
    pygame.display.flip()

def draw_tk():
    new_map_button = Button(file_buttons,text = 'Map from PNG',  command=None)
    load_map_button = Button(file_buttons, text="Load Map", command=load_file)
    save_map_button = Button(file_buttons, text="Save Map", command=None)
    file_handle_section = Label(file_sec_heading,text="File Handling",width="20",height="1",bg="grey")
    file_handle_section.grid(row=0)
    new_map_button.grid(row=1,column=0)
    load_map_button.grid(row=1,column=1)
    save_map_button.grid(row=1,column=2)

    loaded_file_text = Label(loaded_file_sec,text=loaded_file_name, bg="#fff000")
    loaded_file_text.grid()

draw_tk()
while True:
    draw_pygame()
    pygame.display.update()
    root.update()
    pygame.event.pump()

    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:
        print("left click!")
    elif mouse_pressed[1]:
        print("middle_click!")
    elif mouse_pressed[2]:
        print("right click!")
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and map != None:
            if event.button == 4:
                map.resize(32)
            if event.button == 5:
                map.resize(-32)
