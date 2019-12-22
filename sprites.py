import pygame

all_sprites = pygame.sprite.Group()
block_sprites = pygame.sprite.Group()
visible_sprites = pygame.sprite.Group()

def find_visible_sprites(camera_colliding_list):
    visible_sprites.empty()
    for sprite in camera_colliding_list:
        visible_sprites.add(sprite)
