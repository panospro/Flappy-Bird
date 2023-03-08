# # import pygame
# # import random
# # import os
# # from bird import Bird
# # from pipe import Pipe
# # # set up game window
# # WIDTH = 600
# # HEIGHT = 800
# # FPS = 60
# # pygame.init()
# # # pygame.mixer.init()
# # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # pygame.display.set_caption("Flappy Bird")
# # clock = pygame.time.Clock()

# # # set up game assets
# # game_folder = os.path.dirname(__file__)
# # snd_folder = os.path.join(game_folder, "snd")
# # background_img = pygame.image.load("flappy-bird-Python/images/background.png").convert()

# # # define game variables
# # pipe_gap = 400
# # pipe_frequency = 120
# # score = 0

# # # define game functions
# # def draw_text(text, size, x, y):
# #     font = pygame.font.Font(pygame.font.get_default_font(), size)
# #     text_surface = font.render(text, True, (255, 255, 255))
# #     text_rect = text_surface.get_rect()
# #     text_rect.center = (x, y)
# #     screen.blit(text_surface, text_rect)

# # def spawn_pipe():
# #     pipe_heights = [150, 200, 250, 300]
# #     pipe_height = random.choice(pipe_heights)
# #     top_pipe = Pipe(pipe_height - pipe_gap - 320)
# #     bottom_pipe = Pipe(pipe_height + pipe_gap)
# #     pipes.add(top_pipe)
# #     pipes.add(bottom_pipe)
# #     all_sprites.add(top_pipe)
# #     all_sprites.add(bottom_pipe)

# # # set up game sprites
# # all_sprites = pygame.sprite.Group()
# # pipes = pygame.sprite.Group()
# # bird = Bird()
# # all_sprites.add(bird)

# # # add initial pipes
# # for i in range(2):
# #     spawn_pipe()

# # # game loop
# # running = True
# # while running:
# #     # keep loop running at the right speed
# #     clock.tick(FPS)
    
# #     # process input
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False
# #         elif event.type == pygame.KEYDOWN:
# #             if event.key == pygame.K_SPACE:
# #                                 bird.jump()
    
# #     # update game state
# #     all_sprites.update()
    
# #     # spawn pipes
# #     if len(pipes) < 2 and bird.rect.right >= pipe_frequency:
# #         spawn_pipe()
    
# #     for pipe in pipes:
# #         if pipe.rect.right < bird.rect.left and not pipe.scored:
# #             score += 1
# #             # pipe.scored = True

# #     # check for collision with pipes
# #     hits = pygame.sprite.spritecollide(bird, pipes, False)
# #     if hits:
# #         # hit_sound.play()
# #         running = False
    
# #     # remove pipes that are off screen
# #     for pipe in pipes:
# #         if pipe.rect.right < 0:
# #             pipes.remove(pipe)
    
# #     # check for scoring
# #     for pipe in pipes:
# #         if bird.rect.left == pipe.rect.right:
# #             score += 1
# #             # point_sound.play()
    
# #     # check for mouse click
# #     if pygame.mouse.get_pressed()[0]:
# #         bird.jump()

# #     # draw game elements
# #     screen.blit(background_img, (0, 0))
# #     all_sprites.draw(screen)
# #     pipes.draw(screen)
# #     draw_text(str(score), 36, WIDTH/2, 50)
    
# #     # update the display
# #     pygame.display.flip()

# # # quit the game
# # pygame.quit()

# import pygame
# import random
# import os
# from bird import Bird
# from pipe import Pipe

# # set up game window
# WIDTH = 600
# HEIGHT = 800
# FPS = 60
# pygame.init()
# # pygame.mixer.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Flappy Bird")
# clock = pygame.time.Clock()

# # set up game assets
# game_folder = os.path.dirname(__file__)
# snd_folder = os.path.join(game_folder, "snd")
# background_img = pygame.image.load("flappy-bird-Python/images/background.png").convert()

# # define game variables
# pipe_gap = 300
# pipe_frequency = 120
# score = 0

# # define game functions
# def draw_text(text, size, x, y):
#     font = pygame.font.Font(pygame.font.get_default_font(), size)
#     text_surface = font.render(text, True, (255, 255, 255))
#     text_rect = text_surface.get_rect()
#     text_rect.center = (x, y)
#     screen.blit(text_surface, text_rect)

# def spawn_pipe():
#     pipe_heights = [150, 200, 250, 300]
#     pipe_height = random.choice(pipe_heights)
#     top_pipe = Pipe(pipe_height - pipe_gap - 320)
#     bottom_pipe = Pipe(pipe_height + pipe_gap)
#     pipes.add(top_pipe)
#     pipes.add(bottom_pipe)
#     all_sprites.add(top_pipe)
#     all_sprites.add(bottom_pipe)

# # set up game sprites
# all_sprites = pygame.sprite.Group()
# pipes = pygame.sprite.Group()
# bird = Bird()
# all_sprites.add(bird)

# # add initial pipes
# for i in range(2):
#     spawn_pipe()

# # game loop
# running = True
# while running:
#     # keep loop running at the right speed
#     clock.tick(FPS)
    
#     # process input
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 bird.jump()
    
#     # update game state
#     all_sprites.update()
    
#     # spawn pipes
#     if len(pipes) < 2 and bird.rect.right >= pipe_frequency:
#         spawn_pipe()
    
#     # check for collision with pipes
#     hits = pygame.sprite.spritecollide(bird, pipes, False)
#     if hits:
#         # hit_sound.play()
#         running = False
    
#     # remove pipes that are off screen
#     for pipe in pipes:
#         if pipe.rect.right < 0:
#             pipes.remove(pipe)
    
#     # check for scoring
#     for pipe in pipes:
#         if bird.rect.left == pipe.rect.right and not pipe.scored:
#             score += 1
#             pipe.scored = True
#             # point_sound.play()
    
#     # check for mouse click
#     if pygame.mouse.get_pressed()[0]:
#         bird.jump()

#     # draw game elements
#     screen.blit(background_img, (0, 0))
#     all_sprites.draw(screen)
#     pipes.draw(screen)
#     draw_text(str(score), 36, WIDTH/2, 50)
    
#     # update the display
#     pygame.display.flip()

# # quit the game 
# pygame.quit()

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
