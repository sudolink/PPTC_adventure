#map_loader
import pygame
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from tkinter import *
import os
from rooms import tile_size

root = tk.Tk()
controls = tk.Frame(root, width = 1024, height = 786) #creates embed frame for pygame window
controls.grid(columnspan = (600), rowspan = 500) # Adds grid
controls.pack(side = RIGHT) #packs window to the left


file_sec_heading = tk.Frame(root, width = 100, height = 786)
file_buttons = tk.Frame(root, width = 100, height = 786)
loaded_file_sec = tk.Frame(root)

file_sec_heading.pack(side = TOP)
file_buttons.pack(side = TOP)
loaded_file_sec.pack(side = TOP)

os.environ['SDL_WINDOWID'] = str(controls.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

screen = pygame.display.set_mode((1024,786))
screen.fill(pygame.Color(0,0,0))

png_map = None
test_rect = pygame.Surface((100,100))
test_rect.fill((100,100,30))
pygame_items = [png_map,test_rect]
loaded_file_name = "No map loaded"

def load_file():
    fname = askopenfilename(filetypes=(("PNG Room", "*.png"),))
    if fname:
        try:
            global png_map
            png_map = pygame.image.load(fname)
            png_map.convert()
        except:
            showerror("Open Source File", "Failed to read file\n'%s'" % fname)
        else:
            loaded_file_name = fname
        return

def change_label_name():
    pass

pygame.display.init()

def draw_pygame():
    screen.fill((0,0,0))
    if png_map != None:
        screen.blit(png_map,(200,200))
    pygame.display.flip()

def drag():
    for item in pygame_items:
        item

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

    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:
        print("left click!")
    elif mouse_pressed[1]:
        print("middle_click!")
    elif mouse_pressed[2]:
        print("right click!")
