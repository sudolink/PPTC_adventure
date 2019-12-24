import pygame
import player
import sprites

class Camera(pygame.sprite.Sprite):
    def __init__(self,room_entry_point):
        super().__init__()
        self.width = 800
        self.height = 600
        self.dimensions = (self.width,self.height)
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill((255,255,255))
        self.image.set_alpha(50)
        self.rect = self.image.get_rect()
        self.rect.center = room_entry_point
        sprites.all_sprites.add(self)
        sprites.visible_sprites.add(self)
        self.speed = 10
