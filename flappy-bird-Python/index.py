import pygame
import random
import os
from bird import Bird

# set up game window
WIDTH = 600
HEIGHT = 800
FPS = 60
pygame.init()
# pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# set up game assets
game_folder = os.path.dirname(__file__)
snd_folder = os.path.join(game_folder, "snd")
background_img = pygame.image.load("flappy-bird-Python/images/background.png").convert()
bird_img = pygame.image.load("flappy-bird-Python/images/bird.png").convert_alpha()
pipe_img = pygame.image.load("flappy-bird-Python/images/fullPipeBottom.png").convert_alpha()
# hit_sound = pygame.mixer.Sound(os.path.join(snd_folder, "hit.wav"))
# point_sound = pygame.mixer.Sound(os.path.join(snd_folder, "point.wav"))
# jump_sound = pygame.mixer.Sound(os.path.join(snd_folder, "wing.wav"))

# define game variables
gravity = 0.25
bird_velocity = 0
pipe_gap = 100
pipe_frequency = 120
score = 0

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

# define game functions
def draw_text(text, size, x, y):
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def spawn_pipe():
    pipe_heights = [150, 200, 250, 300]
    pipe_height = random.choice(pipe_heights)
    top_pipe = Pipe(pipe_height - pipe_gap - 320)
    bottom_pipe = Pipe(pipe_height + pipe_gap)
    pipes.add(top_pipe)
    pipes.add(bottom_pipe)

# set up game sprites
all_sprites = pygame.sprite.Group()
pipes = pygame.sprite.Group()
bird = Bird()
all_sprites.add(bird)

# game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    
    # process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                                bird.jump()
    
    # update game state
    all_sprites.update()
    
    # spawn pipes
    if len(pipes) < 2 and bird.rect.right >= pipe_frequency:
        spawn_pipe()
    
    # check for collision with pipes
    hits = pygame.sprite.spritecollide(bird, pipes, False)
    if hits:
        # hit_sound.play()
        running = False
    
    # remove pipes that are off screen
    for pipe in pipes:
        if pipe.rect.right < 0:
            pipes.remove(pipe)
    
    # check for scoring
    for pipe in pipes:
        if bird.rect.left == pipe.rect.right:
            score += 1
            # point_sound.play()
    
    # draw game elements
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)
    pipes.draw(screen)
    draw_text(str(score), 36, WIDTH/2, 50)
    
    # update the display
    pygame.display.flip()

# quit the game
pygame.quit()

