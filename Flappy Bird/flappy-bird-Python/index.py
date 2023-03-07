import pygame

# initialize Pygame
pygame.init()

# set up the window
window_width = 500
window_height = 500
screen = pygame.display.set_mode((window_width, window_height))

# load the background image
background_image = pygame.image.load("background.png")


# draw the background image onto the window surface
screen.blit(background_image, (0, 0))

# update the display to show the background image
pygame.display.update()

# start the game loop
while True:
    # handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
