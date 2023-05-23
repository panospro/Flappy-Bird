import pygame
from pipe import Pipe
import random

class PipePair(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.pipe_gap = 150
        self.pipe_frequency = 120
        self.score = 0
        self.pipes_passed = 0  # initialize number of pipes passed to 0
        self.last_spawn_time = pygame.time.get_ticks()  # initialize last spawn time
        self.point_sound = pygame.mixer.Sound("flappy-bird-Python/soundtracks/point.mp3")

    def spawn_pipes(self):
        top_pipe_height = random.randint(100, 400)  # choose a random height for the top pipe
        bottom_pipe_height = top_pipe_height + self.pipe_gap  # calculate the height for the bottom pipe
        top_pipe = Pipe(top_pipe_height - self.pipe_gap - 650, True)
        bottom_pipe = Pipe(bottom_pipe_height, False)
        self.add(top_pipe, bottom_pipe)       
        
    def update(self, bird):
        pygame.sprite.Group.update(self)

        # Spawn pipes if the time elapsed since last spawn is greater than the desired frequency
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time >= self.pipe_frequency * 12:
            self.spawn_pipes()
            self.last_spawn_time = current_time
            
        for pipe in self.sprites():
            if bird.rect.left > pipe.rect.right and not pipe.scored:
                self.pipes_passed += 1
                pipe.scored = True
                if self.pipes_passed % 2 == 0:
                    self.score += 1
                    self.point_sound.play()  # play score sound when score is increased by 1
                
        for pipe in self.sprites():
            if pipe.rect.right < 0:
                self.remove(pipe)

    def reset(self):
        self.empty()  # remove all pipes from the group
        self.score = 0
        self.pipes_passed = 0
        self.last_spawn_time = pygame.time.get_ticks()
        
