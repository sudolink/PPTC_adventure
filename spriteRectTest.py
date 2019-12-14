import pygame
import pathlib

pygame.init()

BACKGROUND = (255,255,255)
path_to_walk_gifs = pathlib.Path("./assets/player/walk-frames/")
PLAYER_WALK_GIF_locations = [str(path_to_walk_gifs)+"/"+item.name for item in path_to_walk_gifs.glob("**/*") if item.is_file()]
print(PLAYER_WALK_GIF_locations)

screen = pygame.display.set_mode((1024,786))


did_it = False
while True:
    screen.fill(BACKGROUND)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()



    pygame.display.update()


class player()
