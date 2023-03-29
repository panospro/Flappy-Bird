import pygame
import neat
import os
import random
import sys 
from bird import Bird
from pipe import Pipe
from pipepair import PipePair

# Set up game window
WIDTH = 600
HEIGHT = 800
FPS = 60
gravity = 0.5
# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bg_img = pygame.image.load("flappy-bird-Python/images/background.png").convert()
bird_img = pygame.image.load("flappy-bird-Python/images/bird.png").convert()

pipe_img_top = pygame.image.load("flappy-bird-Python/images/fullPipeTop.png").convert()

pipe_img_bottom = pygame.image.load("flappy-bird-Python/images/fullPipeBottom.png").convert()

# Set up font
font = pygame.font.SysFont(None, 48)

# Set up clock
clock = pygame.time.Clock()

# Set up NEAT algorithm
def eval_genomes(genomes, config):
    global generation
    pipes = PipePair()
    nets = []
    ge = []
    birds = []

    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        birds.append(Bird())
        genome.fitness = 0
        ge.append(genome)

    while len(birds) > 0 and generation <= 50:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for i, bird in enumerate(birds):
            if pipes.sprites():
                bottom_pipe = max(pipes.sprites(), key=lambda pipe: pipe.rect.bottom)
                top_pipe = min(pipes.sprites(), key=lambda pipe: pipe.rect.top)
                output = nets[i].activate((bird.rect.center[1], abs(bird.rect.center[1] - bottom_pipe.rect.bottom), abs(bird.rect.center[1] - top_pipe.rect.top)))
            else:
                output = nets[i].activate((bird.rect.center[1], 600, 800))
            if output[0] > 0.5:
                bird.jump()

        for bird in birds:
            bird.update()

        pipes.update(birds[0])

        for i, bird in enumerate(birds):
            if pygame.sprite.spritecollide(bird, pipes, False):
                ge[i].fitness -= 1
                nets.pop(i)
                ge.pop(i)
                birds.pop(i)

        for i, bird in enumerate(birds):
            if bird.rect.bottom >= HEIGHT or bird.rect.top <= 0:
                ge[i].fitness -= 1
                nets.pop(i)
                ge.pop(i)
                birds.pop(i)

        for i, genome in enumerate(ge):
            genome.fitness += 0.1
        
        for i, bird in enumerate(birds):
            if pipes.sprites():
                next_pipe = min(pipes.sprites(), key=lambda pipe: pipe.rect.left if pipe.rect.left > bird.rect.right else WIDTH)
                if next_pipe.rect.left > bird.rect.right:
                    ge[i].fitness += 1

        if len(birds) == 0:
            break

        screen.blit(bg_img, (0, 0))
        for bird in birds:
            bird.draw(screen)
        pipes.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

    print(f"Generation {generation} complete")
    generation += 1

    # Reset game objects
    pipes.reset()
    nets = []
    ge = []
    birds = []

    # Create new population of birds
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        birds.append(Bird())
        genome.fitness = 0
        ge.append(genome)

# Set up NEAT configuration
local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'NEAT_config.txt')
config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

# Set up NEAT population
p = neat.Population(config)

# Add reporters to output statistics during training
p.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
p.add_reporter(stats)

# Run NEAT algorithm
generation = 1
winner = p.run(eval_genomes)

# Play game with winning network
if winner:
    net = neat.nn.FeedForwardNetwork.create(winner, config)
    bird = Bird()
    pipes = PipePair()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if pipes.sprites():
            bottom_pipe = max(pipes.sprites(), key=lambda pipe: pipe.rect.bottom)
            top_pipe = min(pipes.sprites(), key=lambda pipe: pipe.rect.top)
            output = net.activate((bird.rect.center[1], abs(bird.rect.center[1] - bottom_pipe.rect.bottom), abs(bird.rect.center[1] - top_pipe.rect.top)))
        else:
            output = net.activate((bird.rect.center[1], 600, 800))
        if output[0] > 0.5:
            bird.jump()

        bird.update()
        pipes.update(bird)

        if pygame.sprite.spritecollide(bird, pipes, False):
            break

        screen.blit(bg_img, (0, 0))
        bird.draw(screen)
        pipes.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()