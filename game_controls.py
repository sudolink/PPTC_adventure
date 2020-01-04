import pygame
import sprites
from rooms import tile_size

mod_keys = [pygame.K_RSHIFT,pygame.K_LSHIFT]
move_keys = [pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d]
scroll_speed = 12#tile_size/8
map_moves = {"left":[scroll_speed,0],"right":[-scroll_speed,0],"up":[0,scroll_speed],"down":[0,-scroll_speed],
            "up_right":[-scroll_speed/2,scroll_speed/2],"up_left":[scroll_speed/2,scroll_speed/2],"down_right":[-scroll_speed/2,-scroll_speed/2],"down_left":[scroll_speed/2,-scroll_speed/2]}
player_moves = {"left":[-scroll_speed,0],"right":[scroll_speed,0],"up":[0,-scroll_speed],"down":[0,scroll_speed],
            "up_right":[scroll_speed/2,-scroll_speed/2],"up_left":[-scroll_speed/2,-scroll_speed/2],"down_right":[scroll_speed/2,scroll_speed/2],"down_left":[-scroll_speed/2,scroll_speed/2]}

def handle_input(room,player,viewport):
    pressed = pygame.key.get_pressed()
    mods_pressed = pygame.key.get_mods()#check for mod keys like LSHIFT

    viewport.move(player.rect.center)

    handle_collision(player,room)

    if any(pressed) and allowed_combination(pressed) and not opposite_keys(pressed):
        if not (pressed[pygame.K_a] or pressed[pygame.K_d]):
            if pressed[pygame.K_s]:
                player.move(player_moves["down"],"down")
                room.move_map(map_moves["down"])
            if pressed[pygame.K_w]:
                player.move(player_moves["up"],"up")
                room.move_map(map_moves["up"])

        if not (pressed[pygame.K_w] or pressed[pygame.K_s]):
            if pressed[pygame.K_a]:
                player.move(player_moves["left"],"left")
                room.move_map(map_moves["left"])
            if pressed[pygame.K_d]:
                player.move(player_moves["right"],"right")
                room.move_map(map_moves["right"])

        if (pressed[pygame.K_w] and pressed[pygame.K_d]):
            player.move(player_moves["up_right"],"up_right")
            room.move_map(map_moves["up_right"])
        if (pressed[pygame.K_s] and pressed[pygame.K_a]):
            player.move(player_moves["down_left"],"down_left")
            room.move_map(map_moves["down_left"])
        if (pressed[pygame.K_s] and pressed[pygame.K_d]):
            player.move(player_moves["down_right"],"down_right")
            room.move_map(map_moves["down_right"])
        if (pressed[pygame.K_w] and pressed[pygame.K_a]):
            player.move(player_moves["up_left"],"up_left")
            room.move_map(map_moves["up_left"])

        if pressed[pygame.K_ESCAPE]:
            pygame.quit()
    else:   #idle if more than 2 directions are being held down, if opposite directions are being held down, and if no directions
        #player-idle
        pass


def allowed_combination(pressed):
    how_many_pressed = 0
    for key in move_keys:
        how_many_pressed += pressed[key] #adds 1 if a move_key is being pressed
    return how_many_pressed < 3


def opposite_keys(pressed):
    return (pressed[pygame.K_w] & pressed[pygame.K_s]) or (pressed[pygame.K_a] and pressed[pygame.K_d])


def handle_collision(player,room):
    if player.collision_rect.check_collision(room.invisiwalls):
        opposite_direction = player.opposite_direction[player.direction]
        player.move(player_moves[opposite_direction],opposite_direction)
        player.be_idle()
        room.move_map(map_moves[opposite_direction])


#
# if not (pressed[pygame.K_a] or pressed[pygame.K_d]):
#     if pressed[pygame.K_s]:
#         room.move_map(map_moves["down"])
#     if pressed[pygame.K_w]:
#         room.move_map(map_moves["up"])
#
# if not (pressed[pygame.K_w] or pressed[pygame.K_s]):
#     if pressed[pygame.K_a]:
#         room.move_map(map_moves["left"])
#     if pressed[pygame.K_d]:
#         room.move_map(map_moves["right"])
#
# if (pressed[pygame.K_w] and pressed[pygame.K_d]):
#     room.move_map(map_moves["up_right"])
# if (pressed[pygame.K_s] and pressed[pygame.K_a]):
#     room.move_map(map_moves["down_left"])
# if (pressed[pygame.K_s] and pressed[pygame.K_d]):
#     room.move_map(map_moves["down_right"])
# if (pressed[pygame.K_w] and pressed[pygame.K_a]):
#     room.move_map(map_moves["up_left"])
