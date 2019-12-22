import pygame
import player
import sprites

class Camera(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 800
        self.height = 600
        self.dimensions = (self.width,self.height)
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill((255,255,255))
        self.image.set_alpha(50)
        self.rect = self.image.get_rect()
        self.player = player.Player(self.update_position)
        sprites.all_sprites.add(self)
        sprites.visible_sprites.add(self)

    def update_position(self):
        self.rect.center = self.player.rect.center

    def colliding_sprites(self):
        return pygame.sprite.spritecollide(self, sprites.all_sprites, False)
