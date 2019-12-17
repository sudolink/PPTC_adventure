import pathlib
import pygame

path_to_rooms = pathlib.Path("./assets/rooms/")

class room():
    def __init__(self,screen_size):
        self.bg = pygame.transform.scale(pygame.image.load("./assets/rooms/room_0/room_0.png"),screen_size)
        self.rect = self.bg.get_rect()
        self.rect.center = (screen_size[0]/2,screen_size[1]/2)


class invisi_block(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface([40,40])
        self.image.fill((255,255,40))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
