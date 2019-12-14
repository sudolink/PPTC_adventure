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

class player():
    def __init__(self):
        self.x = 200
        self.y = 400
        self.width = 90 ##x
        self.height = 160 ##y
        self.speed = 10
        self.walk_count = 0
        self.img = pygame.image.load("assets/player/walk-frames/frame_03_delay-0.1s.gif")
        self.walk_right = [pygame.image.load(str(path_to_walk_gifs)+"/"+frame) for frame in PLAYER_WALK_GIF_locations] #Grab all the walk frames in put them here
        self.resize_self(self.width,self.height)
        self.walk_left = [pygame.transform.flip(frame,True,False) for frame in self.walk_right]
        print(self.walk_left)
        self.usable_keys = [pygame.K_a,pygame.K_d]
        self.walking_right = True

    def resize_self(self,x,y):
        resized = []
        for surface in self.walk_right:
            resized.append(pygame.transform.scale(surface,(x,y)))
        self.walk_right = resized
        del resized
        self.img = pygame.transform.scale(self.img,(x,y))

    def move_it(self,key):
        #check if walk count is greater than the number of frames
        #if yes, reset back to starting walk frame
        if self.walk_count >= len(self.walk_right):
            self.walk_count = 0

        #left and right and still
        if key == "left" and self.x > 0:
            self.img = self.walk_left[self.walk_count]
            self.walk_count += 1
            self.x -= self.speed
        elif key == "right" and self.x < swidth - self.width:
            self.img = self.walk_right[self.walk_count]
            self.walk_count += 1
            self.x += self.speed
        elif key == "still":
            self.img = self.walk_right[4] #default still img for now


    def drawSelf(self):
        screen.blit(self.img,(self.x,self.y))


player_one = player()

def draw_screen():
    screen.fill(WHITE)
    player_one.drawSelf()
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
        player_one.move_it("left")
    elif pressed[pygame.K_d]:
        player_one.move_it("right")
    elif not any(pressed):
        player_one.move_it("still")

    draw_screen()


#if __name__ == "__main__":
#    main()
