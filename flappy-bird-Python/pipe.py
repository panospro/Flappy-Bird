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
pygame.display.set_caption("Flappy Bird")

# load pipe image
pipe_img_top = pygame.image.load("flappy-bird-Python/images/fullPipeTop.png").convert_alpha()
pipe_img_bottom = pygame.image.load("flappy-bird-Python/images/fullPipeBottom.png").convert_alpha()

# Define the pipe class
class Pipe(pygame.sprite.Sprite):
    def __init__(self, height, is_top):
        pygame.sprite.Sprite.__init__(self)
        if is_top:
            self.image = pipe_img_top
        else:
            self.image = pipe_img_bottom
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        if is_top:
            self.rect.y = height

        else:
            self.rect.y = height
        self.speed = -4
        self.scored = False
    
    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.kill()
    
    def get_height(self):
        return self.rect.bottom

class PipePair(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.pipe_gap = 150
        self.pipe_frequency = 120
        self.score = 0
        self.pipes_passed = 0  # initialize number of pipes passed to 0
    
    def spawn_pipes(self):
        pipe_heights = [150, 200, 250, 300]
        pipe_height = random.choice(pipe_heights)
        top_pipe = Pipe(pipe_height - self.pipe_gap -650, True)
        bottom_pipe = Pipe(pipe_height + self.pipe_gap, False)
        self.add(top_pipe, bottom_pipe)
        
        
    def update(self, bird):
        pygame.sprite.Group.update(self)
        if len(self) < 2 and bird.rect.right >= self.pipe_frequency:
            self.spawn_pipes()
        for pipe in self.sprites():
            if bird.rect.left > pipe.rect.right and not pipe.scored:
                self.pipes_passed += 1
                pipe.scored = True
                if self.pipes_passed % 2 == 0:
                    self.score += 1
                
        for pipe in self.sprites():
            if pipe.rect.right < 0:
                self.remove(pipe)
