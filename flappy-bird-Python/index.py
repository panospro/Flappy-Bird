import pygame 
from bird import Bird
from pipepair import PipePair

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

# set the hit sound and death
hit_sound = pygame.mixer.Sound("flappy-bird-Python/soundtracks/hit.mp3")
death_sound = pygame.mixer.Sound("flappy-bird-Python/soundtracks/die.mp3")

def reset_game():
    bird.reset()
    pipes.reset()
    return False

# game loop
running = True
game_over = False 
while (running or not game_over):
    if (not game_over):  # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        # update game objects
        bird.update()
        pipes.update(bird)

        # check for collision
        if pygame.sprite.spritecollide(bird, pipes, False):
            game_over = True
            hit_sound.play()
            death_sound.play()
            
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

    else:
        # create game over text
        game_over_text = font.render("Game Over", True, (255, 0, 0))

        # blit game over text to screen
        screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - game_over_text.get_height()//2))

        # update display
        pygame.display.update() 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_over = reset_game()

# quit game
pygame.quit()
