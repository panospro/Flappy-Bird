import pygame

# set up game window
WIDTH = 600
HEIGHT = 800
gravity = 0.25

pygame.init()
# pygame.mixer.init() // for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# load pipe image
pipe_img = pygame.image.load("flappy-bird-Python/images/fullPipeBottom.png").convert_alpha()

# Define the pipe class
class Pipe(pygame.sprite.Sprite):
    def __init__(self, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pipe_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = height
        self.speed = -4
    
    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.kill()
    
    def get_height(self):
        return self.rect.y + self.rect.height