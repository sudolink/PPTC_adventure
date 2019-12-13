import pygame
import pathlib

#initialize pygame
pygame.init()

#CONSTANTS
WHITE = (255,255 ,255)
path_to_walk_gifs = pathlib.Path("./assets/player/walk-frames/")
PLAYER_WALK_GIF_locations = [item.name for item in path_to_walk_gifs.glob("**/*") if item.is_file()]
print(str(path_to_walk_gifs))

#the screen
screen = pygame.display.set_mode((800,600))

class player():
    def __init__(self):
        self.img = pygame.image.load("assets/player/walk-frames/frame_03_delay-0.1s.gif")
        self.walk = [pygame.image.load(str(path_to_walk_gifs)+"/"+frame) for frame in PLAYER_WALK_GIF_locations] #Grab all the walk frames in put them here
        print(self.walk)
        self.x = 200
        self.y = 200
        self.screen = screen
        self.usable_keys = [pygame.K_a,pygame.K_d]
        self.speed = 0.1
        self.turned_right = True
        self.resize_self(90,160)

    def resize_self(self,x,y):
        resized = []
        for surface in self.walk:
            resized.append(pygame.transform.scale(surface,(x,y)))
        self.walk = resized
        del resized
        self.img = pygame.transform.scale(self.img,(x,y))

    def move_it(self,key):
        if key == "left":
            ##mirror image and start playing walk loop
            if self.turned_right:
                self.img = pygame.transform.flip(self.img,True,False)
                self.turned_right = False

            self.x -= self.speed
        elif key == "right":
            if not self.turned_right:
                self.img = pygame.transform.flip(self.img,True,False)
                self.turned_right = True
            self.x += self.speed

    def drawSelf(self,where):
        where.blit(self.img,(self.x,self.y))


player_one = player()
#game LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]:
        player_one.move_it("left")
    elif pressed[pygame.K_d]:
        player_one.move_it("right")

    screen.fill(WHITE)
    player_one.drawSelf(screen)
    pygame.display.update()


#if __name__ == "__main__":
#    main()
