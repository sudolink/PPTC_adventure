import pygame
import sprites

class Viewport(pygame.sprite.Sprite):
    def __init__(self,screen_size):
        super().__init__()
        self.image = pygame.Surface(screen_size)
        self.rect = self.image.get_rect()
        self.image.fill((255,255,255))
        self.image.set_alpha(20)
        self.inner_view = Inner_View(screen_size,self.rect.center)
        #sprites.all_sprites.add(self.inner_view)
        #sprites.inner_view_sprite.add(self)

    def follow_player(self, scroll, player_loc):
        self.rect.x += scroll[0]
        self.rect.y += scroll[1]
        self.inner_view.rect.x += scroll[0]
        self.inner_view.rect.y += scroll[1]

    def player_collision(self, player_rect, scroll):
        collision = self.inner_view.rect.colliderect(player_rect)
        if collision:
            print("player in viewport")
        else:
            print("player out of viewport")

    def move(self,player_center):
        self.rect.center = player_center
        self.inner_view.rect.center = self.rect.center

class Inner_View(pygame.sprite.Sprite):
    def __init__(self,parent_size,parent_center):
        super().__init__()
        self.image = pygame.Surface((parent_size[0]/3,parent_size[1]/3))
        self.rect = self.image.get_rect()
        self.rect.center = parent_center
        self.image.fill((200,10,100))
        self.image.set_alpha(38)
