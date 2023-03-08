import pygame 
from bird import Bird
from pipepair import PipePair
import sys
sys.path.append("C:\Python311\Lib\site-packages")
import neat

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

def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        bird = Bird()
        pipes = PipePair()

        fitness = 0
        while True:
            # get the network's output
            if pipes.sprites():
                bottom_pipe = max(pipes.sprites(), key=lambda pipe: pipe.rect.bottom)
                top_pipe = min(pipes.sprites(), key=lambda pipe: pipe.rect.top)
                output = net.activate((bird.rect.center, abs(bird.rect.center - bottom_pipe.rect.bottom), abs(bird.rect.center - top_pipe.rect.top)))
            else:
                output = net.activate((bird.rect.center, 600, 800))
            # make the bird jump if the network's output is greater than 0.5
            if output[0] > 0.5:
                bird.jump()

            # update the game objects
            bird.update()
            pipes.update(bird)

            # check for collision
            if pygame.sprite.spritecollide(bird, pipes, False):
                genome.fitness = fitness
                break

            # increase fitness for each frame that the bird survives
            fitness += 1

            # update the display
            screen.blit(bg_img, (0, 0))
            bird.draw(screen)
            pipes.draw(screen)
            pygame.display.update()
            clock.tick(FPS)

        # set the genome's fitness score
        genome.fitness = fitness + (pipes.score * 100)

config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                            neat.DefaultSpeciesSet, neat.DefaultStagnation,
                            'flappy-bird-Python/config-feedforward.txt')

def run_neat():
    # create the population
    population = neat.Population(config)

    # add a stdout reporter to show progress in the terminal
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)

    # run the NEAT algorithm for up to 50 generations
    winner = population.run(eval_genomes, 50)

    # print the winning genome
    print('\nBest genome:\n{!s}'.format(winner))

    # show the winning bird in action
    net = neat.nn.FeedForwardNetwork.create(winner, config)
    bird = Bird()
    pipes = PipePair()
    while True:
        output = net.activate((bird.rect.center, abs(bird.rect.center - pipes.bottom), abs(bird.rect.center - pipes.top)))
        if output[0] > 0.5:
            bird.jump()
        bird.update()
        pipes.update(bird)
        screen.blit(bg_img, (0, 0))
        bird.draw(screen)
        pipes.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    run_neat()



    
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
