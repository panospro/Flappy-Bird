# def eval_genomes(genomes, config):
#     for genome_id, genome in genomes:
#         net = neat.nn.FeedForwardNetwork.create(genome, config)
#         bird = Bird()
#         pipes = PipePair()

#         fitness = 0
#         while True:
#             # get the network's output
#             if pipes.sprites():
#                 bottom_pipe = max(pipes.sprites(), key=lambda pipe: pipe.rect.bottom)
#                 top_pipe = min(pipes.sprites(), key=lambda pipe: pipe.rect.top)
#                 output = net.activate((bird.rect.center, abs(bird.rect.center - bottom_pipe.rect.bottom), abs(bird.rect.center - top_pipe.rect.top)))
#             else:
#                 output = net.activate((bird.rect.center, 600, 800))
#             # make the bird jump if the network's output is greater than 0.5
#             if output[0] > 0.5:
#                 bird.jump()

#             # update the game objects
#             bird.update()
#             pipes.update(bird)

#             # check for collision
#             if pygame.sprite.spritecollide(bird, pipes, False):
#                 genome.fitness = fitness
#                 break

#             # increase fitness for each frame that the bird survives
#             fitness += 1

#             # update the display
#             screen.blit(bg_img, (0, 0))
#             bird.draw(screen)
#             pipes.draw(screen)
#             pygame.display.update()
#             clock.tick(FPS)

#         # set the genome's fitness score
#         genome.fitness = fitness + (pipes.score * 100)

# config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
#                             neat.DefaultSpeciesSet, neat.DefaultStagnation,
#                             'flappy-bird-Python/config-feedforward.txt')

# def run_neat(config):
#     # create the population
#     population = neat.Population(config)

#     # add a stdout reporter to show progress in the terminal
#     population.add_reporter(neat.StdOutReporter(True))
#     stats = neat.StatisticsReporter()
#     population.add_reporter(stats)

#     # run the NEAT algorithm for up to 50 generations
#     winner = population.run(eval_genomes, 50)

#     # print the winning genome
#     print('\nBest genome:\n{!s}'.format(winner))

#     # show the winning bird in action
#     net = neat.nn.FeedForwardNetwork.create(winner, config)
#     bird = Bird()
#     pipes = PipePair()
#     while True:
#         output = net.activate((bird.rect.center, abs(bird.rect.center - pipes.bottom), abs(bird.rect.center - pipes.top)))
#         if output[0] > 0.5:
#             bird.jump()
#         bird.update()
#         pipes.update(bird)
#         screen.blit(bg_img, (0, 0))
#         bird.draw(screen)
#         pipes.draw(screen)
#         pygame.display.update()
#         clock.tick(FPS)

import sys
sys.path.append("C:\Python311\Lib\site-packages")
import neat
import os
import pygame 
from bird import Bird
from pipepair import PipePair

# Set up the game window
SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load the background image and set up the clock
bg_img = pygame.image.load("flappy-bird-Python/images/background.png").convert()
clock = pygame.time.Clock()
FPS = 60

# Define the evaluation function
def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        bird = Bird(SCREEN_WIDTH, SCREEN_HEIGHT)
        pipes = PipePair(SCREEN_WIDTH, SCREEN_HEIGHT)

        fitness = 0
        while True:
            # get the network's output
            if pipes.sprites():
                bottom_pipe = max(pipes.sprites(), key=lambda pipe: pipe.rect.bottom)
                top_pipe = min(pipes.sprites(), key=lambda pipe: pipe.rect.top)
                output = net.activate((bird.rect.center[1], abs(bird.rect.center[1] - bottom_pipe.rect.bottom), abs(bird.rect.center[1] - top_pipe.rect.top)))
            else:
                output = net.activate((bird.rect.center[1], 600, 800))
            # make the bird jump if the network's output is greater than 0.5
            if output[0] > 0.5:
                bird.jump()

            # update the game objects
            bird.update()
            pipes.update()

            # check for collision
            if bird.check_collision(pipes):
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

# Set up the NEAT configuration and population
config_file = "flappy-bird-Python/config-feedforward.txt"
config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_file)
print(123,config)
population = neat.Population(config)

# Add reporters to show progress during training
population.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
population.add_reporter(stats)

# Run the NEAT algorithm for up to 50 generations
winner = population.run(eval_genomes, 50)

# Print the winning genome
print('\nBest genome:\n{!s}'.format(winner))

# Show the winning bird in action
net = neat.nn.FeedForwardNetwork.create(winner, config)
bird = Bird(SCREEN_WIDTH, SCREEN_HEIGHT)
pipes = PipePair(SCREEN_WIDTH, SCREEN_HEIGHT)
while True:
    output = net.activate((bird.rect.center[1], abs(bird.rect.center[1] - pipes.bottom), abs(bird.rect.center[1] - pipes.top)))
    if output[0] > 0.5:
        bird.jump()
    bird.update()
    pipes.update()
    screen.blit(bg_img, (0, 0))
    bird.draw(screen)
    pipes.draw(screen)
    pygame.display.update
