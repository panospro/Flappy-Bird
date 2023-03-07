import pygame

# set up game window
WIDTH = 600
HEIGHT = 800
gravity = 0.25

pygame.init()
# pygame.mixer.init() // for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# load bird image
bird_img = pygame.image.load("flappy-bird-Python/images/bird.png").convert_alpha()

# Define the bird class
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bird_img
        self.rect = self.image.get_rect()
        self.rect.center = (150, HEIGHT/2)
        self.velocity = 0
    
    def update(self):
        self.velocity += gravity
        self.rect.y += self.velocity
        if self.rect.bottom > HEIGHT - 70:
            self.rect.bottom = HEIGHT - 70
            self.velocity = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity = 0
    
    def jump(self):
        self.velocity = -6
        # jump_sound.play()