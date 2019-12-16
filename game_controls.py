import pygame

usable_keys = ["w","s","a","d"] # event.unicode
usable_keys_pygame = [pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d] #event.key

def handle_input(player):
    pressed = pygame.key.get_pressed()

    #check if no other keys are pressed
    if len(list(filter(lambda a: a == True,pressed))) < 3 and not ((pressed[pygame.K_w] and pressed[pygame.K_s]) or (pressed[pygame.K_a] and pressed[pygame.K_d])) and any(pressed) and not player.check_collision():

        if not (pressed[pygame.K_a] or pressed[pygame.K_d]):
            if pressed[pygame.K_s]: player.move_it("down")
            if pressed[pygame.K_w]: player.move_it("up")

        if not (pressed[pygame.K_w] or pressed[pygame.K_s]):
            if pressed[pygame.K_a]: player.move_it("left")
            if pressed[pygame.K_d]: player.move_it("right")

        if (pressed[pygame.K_w] and pressed[pygame.K_d]): player.move_it("up_right")
        if (pressed[pygame.K_s] and pressed[pygame.K_a]): player.move_it("down_left")
        if (pressed[pygame.K_s] and pressed[pygame.K_d]): player.move_it("down_right")
        if (pressed[pygame.K_w] and pressed[pygame.K_a]): player.move_it("up_left")

    else:   #idle if more than 2 directions are being held down, if opposite directions are being held down, and if no directions
        player.be_idle()

    mouse_pressed = pygame.mouse.get_pressed() #(left,middle,right)
    if mouse_pressed[0]:
        pass
