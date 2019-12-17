import pygame

def handle_input(player):
    pressed = pygame.key.get_pressed()
    #check if no other keys are pressed
    if len(list(filter(lambda a: a == True,pressed))) < 3 and not ((pressed[pygame.K_w] and pressed[pygame.K_s]) or (pressed[pygame.K_a] and pressed[pygame.K_d])) and any(pressed):

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
