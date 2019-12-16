import pygame

usable_keys = ["w","s","a","d"] # event.unicode
usable_keys_pygame = [pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d] #event.key

def handle_input(player):
    pressed = pygame.key.get_pressed()

    #check if no other keys are pressed
    if not (pressed[pygame.K_a] or pressed[pygame.K_d]):
        if pressed[pygame.K_s]: player.move_it("down")
        if pressed[pygame.K_w]: player.move_it("up")

    if not (pressed[pygame.K_w] or pressed[pygame.K_s]):
        if pressed[pygame.K_a]: player.move_it("left")
        if pressed[pygame.K_d]: player.move_it("right")

    #diagonal walking
    if (pressed[pygame.K_s] and pressed[pygame.K_a]): player.move_it("down_left")
    if (pressed[pygame.K_s] and pressed[pygame.K_d]): player.move_it("down_right")
    if (pressed[pygame.K_w] and pressed[pygame.K_a]): player.move_it("up_left")
    if (pressed[pygame.K_w] and pressed[pygame.K_d]): player.move_it("up_right")


    if not any(pressed) : player.be_idle()
