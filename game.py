import pygame
from paddle import Paddle
from ball import Ball

# A játék logikája, beleértve az input kezelést, 
# a játék állapotának frissítését és a rajzolást.
class Game:
    def __init__(self):
        pygame.init()  # a pygame inicializálása
        self.paddle = Paddle()
        self.ball = Ball()
        self.score = 0
        self.font = pygame.font.Font(None, 36)  # Betűtípus inicializálása
        self.running = True

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move("left")
        if keys[pygame.K_RIGHT]:
            self.paddle.move("right")

    def update(self):
        self.ball.move()
        if not self.ball.bounce(self.paddle):
            self.reset()
        elif self.ball.rect.colliderect(self.paddle.rect):
            self.score += 1

    def reset(self):
        self.ball = Ball()
        self.score = 0

    def draw(self, screen):
        screen.fill((255, 255, 255))  # fehér háttér
        self.paddle.draw(screen)
        self.ball.draw(screen)
        score_text = self.font.render(f"Pontszám: {self.score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()

    def run(self):
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Egyszerű Pong Játék")

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.handle_input()
            self.update()
            self.draw(screen)
            pygame.time.Clock().tick(60)

        pygame.quit()
