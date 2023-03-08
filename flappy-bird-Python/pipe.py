import pygame

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
        self.image = pipe_img_top if is_top else pipe_img_bottom
        self.rect = self.image.get_rect(x=WIDTH, y=height)
        self.speed = -4
        self.scored = False
    
    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.kill()
    
    def get_height(self):
        return self.rect.bottom

