import pygame
import pathlib

#initialize pygame
pygame.init()

#CONSTANTS
WHITE = (255,255 ,255)
path_to_walk_gifs = pathlib.Path("./assets/player/walk-frames/")
PLAYER_WALK_GIF_locations = [item.name for item in path_to_walk_gifs.glob("**/*") if item.is_file()]
#print(str(path_to_walk_gifs))
clock = pygame.time.Clock()
#the screen
swidth = 1024
sheight = 786
screen = pygame.display.set_mode((swidth,sheight))

music = pygame.mixer.music.load('./assets/stayin_alive.mp3')
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

class pavement():
    def __init__(self):
        self.width = 50
        self.height = 150
        self.x = 0
        self.y = sheight - self.height
        self.blocks = []

    def makeBlock(self,x,y,width,height):
        new_block = pygame.Rect(x,y,width,height)
        self.blocks.append(new_block)

    def makeBlocks(self,how_many):
        for block in how_many:
            self.makeBlock(self.x,self.y,self.width,self.height)
            self.x += self.width * 2

    def drawPavement(self):
        for block in self.blocks:
            pygame.draw.rect(screen,(100,100,100),block)

class sun():
    def __init__(self):
        self.x = 700
        self.y = 100
        self.center = (self.x,self.y)
        self.radius = 90
        self.color = (255,255,102)
        self.shadow_lines = []


    def stick_to_mouse(self):
        mouse_loc = pygame.mouse.get_pos()
        self.x = mouse_loc[0]
        self.y = mouse_loc[1]
        self.center = mouse_loc

    def draw_sun(self):
        self.stick_to_mouse()
        pygame.draw.circle(screen,self.color,self.center,self.radius)

    def cast_shadows(self,player_location,player_size):
        pass
        #imaginary line from center of sun to top of head
        #where it touches the ground (player x + player height -> feet)
        #is where the top of the shadow should be
        #the beginning of the shadow should be at feet
        #make just an elipse for now
        #pygame.draw.line(surface, color, start_pos, end_pos, width)

        #player_pos == (x,y), player_size == (width,height)
        start_pos = self.center
        end_pos_head = (player_location[0]+player_size[0]/2,player_location[1])
        end_pos_feet = (player_location[0]+player_size[0]/2,player_location[1]+player_size[1])
        pygame.draw.line(screen,(0,0,0),start_pos,end_pos_head) #NEED TO EXTEND THIS ONE TO THE FLOOR SOMEHOW
        pygame.draw.line(screen,(0,0,0),start_pos,end_pos_feet)




class player():
    def __init__(self):
        self.x = 200
        self.y = 570
        self.width = 90 ##x
        self.height = 160 ##y
        self.speed = 11
        self.walk_count = 0
        self.img = pygame.image.load("assets/player/walk-frames/frame_03_delay-0.1s.gif")
        self.walk_right = [pygame.image.load(str(path_to_walk_gifs)+"/"+frame) for frame in PLAYER_WALK_GIF_locations] #Grab all the walk frames in put them here
        self.resize_self(self.width,self.height)
        self.walk_left = [pygame.transform.flip(frame,True,False) for frame in self.walk_right]
        self.usable_keys = [pygame.K_a,pygame.K_d]
        self.walking_right = True
        self.first_move = True

    def resize_self(self,x,y):
        resized = []
        for surface in self.walk_right:
            resized.append(pygame.transform.scale(surface,(x,y)))
        self.walk_right = resized
        del resized
        self.img = pygame.transform.scale(self.img,(x,y))

    def location(self):
        return (self.x,self.y)

    def size(self):
        return (self.width,self.height)

    def move_it(self,key):
        #check if walk count is greater than the number of frames
        #if yes, reset back to starting walk frame
        if self.walk_count >= len(self.walk_right):
            self.walk_count = 0
        if self.first_move:
            pygame.mixer.music.play(-1)
            self.first_move = False

        #left and right and still
        if (key == "left" or key == "sleft") and self.x > 0:
            pygame.mixer.music.unpause()
            self.walking_right = False

            if key == "left":
                self.img = self.walk_left[self.walk_count]
            elif key == "sleft":
                self.img = self.walk_right[self.walk_count]

            self.walk_count += 1
            self.x -= self.speed
        elif (key == "right" or key == "sright")and self.x < swidth - self.width:
            pygame.mixer.music.unpause()
            self.walking_right = True

            if key == "right":
                self.img = self.walk_right[self.walk_count]
            elif key == "sright":
                self.img = self.walk_left[self.walk_count]

            self.walk_count += 1
            self.x += self.speed
        elif key == "still":
            pygame.mixer.music.pause()
            if self.walking_right:
                self.img = self.walk_right[4] #default still img for now
            else:
                self.img = self.walk_left[4]


    def drawSelf(self):
        screen.blit(self.img,(self.x,self.y))


pavement = pavement()
#pavement.makeBlocks(range(10))
pavement.makeBlock(0,sheight-100,swidth,100)
player_one = player()
the_sun = sun()

def draw_screen():
    screen.fill(WHITE)
    pavement.drawPavement()
    player_one.drawSelf()
    the_sun.draw_sun()
    the_sun.cast_shadows(player_one.location(),player_one.size())
    pygame.display.flip()
    pygame.display.update()

#game LOOP
running = True
while running:
    clock.tick(12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]:
        if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
            player_one.move_it("sleft")
        else:
            player_one.move_it("left")
    elif pressed[pygame.K_d]:
        if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
            player_one.move_it("sright")
        else:
            player_one.move_it("right")
    elif not any(pressed):
        player_one.move_it("still")

    draw_screen()


#if __name__ == "__main__":
#    main()

#for pyinstaller
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
