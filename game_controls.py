import pygame
tile_size = 32

mod_keys = [pygame.K_RSHIFT,pygame.K_LSHIFT]
move_keys = [pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d]

def handle_input(player):
    pressed = pygame.key.get_pressed()

    #check for mod keys like LSHIFT
    mods_pressed = pygame.key.get_mods()
    if mods_pressed == pygame.KMOD_LSHIFT:
        player.speed = tile_size/3
    else:
        player.speed = tile_size/4


    if allowed_combination(pressed) and not opposite_keys_pressed(pressed) and any(pressed):
        disable_direction = player.prevent_movement_into_colliding_object()
        if not (pressed[pygame.K_a] or pressed[pygame.K_d]):
            if pressed[pygame.K_s] and disable_direction != "down": player.move_it("down")
            if pressed[pygame.K_w] and disable_direction != "up": player.move_it("up")

        if not (pressed[pygame.K_w] or pressed[pygame.K_s]):
            if pressed[pygame.K_a] and disable_direction != "left": player.move_it("left")
            if pressed[pygame.K_d] and disable_direction != "right": player.move_it("right")

        if (pressed[pygame.K_w] and pressed[pygame.K_d]) and disable_direction != "up_right": player.move_it("up_right")
        if (pressed[pygame.K_s] and pressed[pygame.K_a]) and disable_direction != "down_left": player.move_it("down_left")
        if (pressed[pygame.K_s] and pressed[pygame.K_d]) and disable_direction != "down_right": player.move_it("down_right")
        if (pressed[pygame.K_w] and pressed[pygame.K_a]) and disable_direction != "up_left": player.move_it("up_left")

    else:   #idle if more than 2 directions are being held down, if opposite directions are being held down, and if no directions
        player.be_idle()


def allowed_combination(pressed):
    how_many_pressed = 0
    for key in move_keys:
        how_many_pressed += pressed[key] #adds 1 if a move_key is being pressed
    return how_many_pressed < 3


def opposite_keys_pressed(pressed):
    return (pressed[pygame.K_w] & pressed[pygame.K_s]) or (pressed[pygame.K_a] and pressed[pygame.K_d])
