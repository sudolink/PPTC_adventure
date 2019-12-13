import pygame


#initialize pygame

pygame.init()


#the screen
screen = pygame.display.set_mode((800,600))


#game LOOP
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False



#if __name__ == "__main__":
#    main()
