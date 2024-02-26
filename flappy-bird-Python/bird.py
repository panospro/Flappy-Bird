import pygame

# set up game window
WIDTH = 600
HEIGHT = 800
gravity = 0.6

pygame.init()
# pygame.mixer.init() // for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load bird image 
bird_img = pygame.image.load("flappy-bird-Python/images/bird.png").convert_alpha()

# Define the bird class
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bird_img
        self.rect = self.image.get_rect()
        self.rect.center = (150, HEIGHT/2)
        self.velocity = 0
        self.jump_sound = pygame.mixer.Sound("flappy-bird-Python/soundtracks/wing.mp3")
        self.jump_sound.set_volume(0.3)  # set volume to 50%

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
        self.velocity = -8
        self.jump_sound.play()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def reset(self):
        self.rect.center = (150, HEIGHT/4)
        self.velocity = 0
