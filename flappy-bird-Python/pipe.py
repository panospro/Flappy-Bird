# # import pygame

# # # set up game window
# # WIDTH = 600
# # HEIGHT = 800
# # gravity = 0.25

# # pygame.init()
# # # pygame.mixer.init() // for sound
# # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # pygame.display.set_caption("Flappy Bird")

# # # load pipe image
# # pipe_img = pygame.image.load("flappy-bird-Python/images/fullPipeBottom.png").convert_alpha()

# # # Define the pipe class
# # class Pipe(pygame.sprite.Sprite):
# #     def __init__(self, height):
# #         pygame.sprite.Sprite.__init__(self)
# #         self.image = pipe_img
# #         self.rect = self.image.get_rect()
# #         self.rect.x = WIDTH
# #         self.rect.y = height
# #         self.speed = -4
    
# #     def update(self):
# #         self.rect.x += self.speed
# #         if self.rect.right < 0:
# #             self.kill()
    
# #     def get_height(self):
# #         return self.rect.y + self.rect.height

# import pygame

# # set up game window
# WIDTH = 600
# HEIGHT = 800
# gravity = 0.25

# pygame.init()
# # pygame.mixer.init() // for sound
# # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Flappy Bird")

# # load pipe image
# pipe_img = pygame.image.load("flappy-bird-Python/images/fullPipeBottom.png").convert_alpha()

# # Define the pipe class
# class Pipe(pygame.sprite.Sprite):
#     def __init__(self, height):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pipe_img
#         self.rect = self.image.get_rect()
#         self.rect.x = WIDTH
#         self.rect.y = height
#         self.speed = -4
    
#     def update(self):
#         self.rect.x += self.speed
#         if self.rect.right < 0:
#             self.kill()
    
#     def get_height(self):
#         return self.rect.y + self.rect.height

import pygame
import random

# set up game window
WIDTH = 600
HEIGHT = 800
gravity = 0.25

pygame.init()
# pygame.mixer.init() // for sound
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# load pipe image
pipe_img_top = pygame.image.load("flappy-bird-Python/images/fullPipeTop.png").convert_alpha()
pipe_img_bottom = pygame.image.load("flappy-bird-Python/images/fullPipeBottom.png").convert_alpha()

# Define the pipe class
class Pipe(pygame.sprite.Sprite):
    def __init__(self, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pipe_img_top
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = height - self.rect.height
        self.speed = -4
        self.scored = False
    
    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.kill()
    
    def get_height(self):
        return self.rect.y + self.rect.height

class PipePair(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.pipe_gap = 150
        self.pipe_frequency = 120
        self.score = 0
    
    def spawn_pipes(self):
        pipe_heights = [150, 200, 250, 300]
        pipe_height = random.choice(pipe_heights)
        top_pipe = Pipe(pipe_height - self.pipe_gap -320)
        bottom_pipe = Pipe(pipe_height + self.pipe_gap)
        self.add(top_pipe)
        self.add(bottom_pipe)
        
    def update(self, bird):
        pygame.sprite.Group.update(self)
        if len(self) < 2 and bird.rect.right >= self.pipe_frequency:
            self.spawn_pipes()
        for pipe in self.sprites():
            if bird.rect.left > pipe.rect.right and not pipe.scored:
                self.score += 1
                pipe.scored = True
                # play score sound here
        for pipe in self.sprites():
            if pipe.rect.right < 0:
                self.remove(pipe)
