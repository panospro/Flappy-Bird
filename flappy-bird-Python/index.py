import pygame 
from bird import Bird
from pipe import PipePair

# set up game window
WIDTH = 600
HEIGHT = 800
FPS = 60

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# load background image
bg_img = pygame.image.load("flappy-bird-Python/images/background.png").convert()

# create game objects 
bird = Bird()
pipes = PipePair() 

# set up clock
clock = pygame.time.Clock()

# set up font
font = pygame.font.SysFont(None, 48)

# game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # update game objects
    bird.update()
    pipes.update(bird)

    # check for collision
    if pygame.sprite.spritecollide(bird, pipes, False):
        running = False

    # draw background
    screen.blit(bg_img, (0, 0))

    # draw game objects
    bird.draw(screen)
    pipes.draw(screen) 

    # draw score
    score_text = font.render(str(pipes.score), True, (255, 255, 255))
    screen.blit(score_text, (WIDTH//2, 50))

    # update display
    pygame.display.update()

    # set up frame rate
    clock.tick(FPS)

# quit game
pygame.quit()
