import pygame
import sprites
tile_size = 32

mod_keys = [pygame.K_RSHIFT,pygame.K_LSHIFT]
move_keys = [pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d]

def handle_input(room):
    pressed = pygame.key.get_pressed()

    #check for mod keys like LSHIFT
    mods_pressed = pygame.key.get_mods()



    if allowed_combination(pressed) and not opposite_keys_pressed(pressed) and any(pressed):
        if not (pressed[pygame.K_a] or pressed[pygame.K_d]):
            if pressed[pygame.K_s]:
                room.move_tiles_with_room(0,10)
                print(room.rect.center)
            if pressed[pygame.K_w]:
                pass

        if not (pressed[pygame.K_w] or pressed[pygame.K_s]):
            if pressed[pygame.K_a]:
                pass
            if pressed[pygame.K_d]:
                pass

        if (pressed[pygame.K_w] and pressed[pygame.K_d]):
            pass
        if (pressed[pygame.K_s] and pressed[pygame.K_a]):
            pass
        if (pressed[pygame.K_s] and pressed[pygame.K_d]):
            pass
        if (pressed[pygame.K_w] and pressed[pygame.K_a]):
            pass

    else:   #idle if more than 2 directions are being held down, if opposite directions are being held down, and if no directions
        #player-idle
        pass


def allowed_combination(pressed):
    how_many_pressed = 0
    for key in move_keys:
        how_many_pressed += pressed[key] #adds 1 if a move_key is being pressed
    return how_many_pressed < 3


def opposite_keys_pressed(pressed):
    return (pressed[pygame.K_w] & pressed[pygame.K_s]) or (pressed[pygame.K_a] and pressed[pygame.K_d])
