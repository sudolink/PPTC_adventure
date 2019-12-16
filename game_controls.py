import pygame

usable_keys = ["w","s","a","d"] # event.unicode
usable_keys_pygame = [pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d] #event.key

def handle_input(player):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a] and pressed[pygame.K_s]: player.move_it("downleft")
    if pressed[pygame.K_s]: player.move_it("down")
    if pressed[pygame.K_a] and pressed[pygame.K_d]: player.move_it("downright")
    if pressed[pygame.K_d]: player.move_it("right")
    if pressed[pygame.K_w] and pressed[pygame.K_d]: player.move_it("upright")
    if pressed[pygame.K_w]: player.move_it("up")
    if pressed[pygame.K_w] and pressed[pygame.K_a]: player.move_it("upleft")
    if pressed[pygame.K_a]: player.move_it("left")
