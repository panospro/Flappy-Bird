import pygame 
from bird import Bird
from pipepair import PipePair

class FlappyBird:
    def __init__(self):
        # set up game window
        self.WIDTH = 600
        self.HEIGHT = 800
        self.FPS = 60

        # initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Flappy Bird")

        # load background image
        self.bg_img = pygame.image.load("flappy-bird-Python/images/background.png").convert()

        # create game objects 
        self.bird = Bird()
        self.pipes = PipePair() 

        # set up clock
        self.clock = pygame.time.Clock()

        # set up font
        self.font = pygame.font.SysFont(None, 48)
        self.game_over = False 
        # set the hit sound and death
        # self.hit_sound = pygame.mixer.Sound("flappy-bird-Python/soundtracks/hit.mp3")
        # self.death_sound = pygame.mixer.Sound("flappy-bird-Python/soundtracks/die.mp3")

    def reset_game(self):
        self.bird.reset()
        self.pipes.reset()
        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.jump()

    def update(self):
        self.bird.update()
        self.pipes.update(self.bird)

        if pygame.sprite.spritecollide(self.bird, self.pipes, False):
            self.game_over = True
            # self.hit_sound.play()
            # self.death_sound.play()

    def draw(self):
        # draw background
        self.screen.blit(self.bg_img, (0, 0))

        # draw game objects
        self.bird.draw(self.screen)
        self.pipes.draw(self.screen) 

        # draw score
        score_text = self.font.render(str(self.pipes.score), True, (255, 255, 255))
        self.screen.blit(score_text, (self.WIDTH//2, 50))

    def run(self):
        running = True

        while running:
            running = not self.handle_events()

            if not self.game_over:
                self.handle_events()
                self.update()
                self.draw()

                # update display
                pygame.display.update()

                # set up frame rate
                self.clock.tick(self.FPS)

            else:
                # create game over text
                game_over_text = self.font.render("Game Over", True, (255, 0, 0))

                # blit game over text to screen
                self.screen.blit(game_over_text, (self.WIDTH//2 - game_over_text.get_width()//2, self.HEIGHT//2 - game_over_text.get_height()//2))

                # update display
                pygame.display.update() 

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.reset_game()

        pygame.quit()

if __name__ == '__main__':
    game = FlappyBird()
    game.run()