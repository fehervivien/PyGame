import pygame
from paddle import Paddle
from ball import Ball

# A játék logikája, beleértve az input kezelést, a játék állapotának frissítését és a rajzolást.

class Game:
    def __init__(self):
        pygame.init()
        self.paddle = Paddle()
        self.ball = Ball()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 27)  # Kisebb betűméret a gombokhoz
        self.running = True
        self.game_over = False
        self.game_started = False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move("left")
        if keys[pygame.K_RIGHT]:
            self.paddle.move("right")

    def update(self):
        if not self.game_over and self.game_started:
            self.ball.move()
            if self.ball.bounce(self.paddle):
                self.score += 1
            if self.ball.rect.bottom >= 600:
                self.game_over = True

    def draw(self, screen):
        screen.fill((255, 255, 255))  # Fehér háttér
        if not self.game_started:
            self.draw_start_screen(screen)
        else:
            self.paddle.draw(screen)
            self.ball.draw(screen)
            score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
            screen.blit(score_text, (10, 10))
            if self.game_over:
                self.draw_game_over(screen)
        pygame.display.flip()

    def draw_start_screen(self, screen):
        start_text = self.small_font.render("Start", True, (0, 200, 0))
        start_rect = start_text.get_rect(center=(400, 260))  # Középre igazítjuk a szöveget
        pygame.draw.rect(screen, (0, 200, 0), (start_rect.left - 30, start_rect.top - 15, start_rect.width + 60, start_rect.height + 30), 2)
        screen.blit(start_text, start_rect)

    def draw_game_over(self, screen):
        game_over_text = self.font.render("Sajnos vesztettél! :(", True, (255, 0, 0))
        restart_text = self.small_font.render("Játék újrakezdése", True, (255, 165, 0))
        game_over_rect = game_over_text.get_rect(center=(400, 260))  # Középre igazítjuk a szöveget
        restart_rect = restart_text.get_rect(center=(400, 320))  # Középre igazítjuk a szöveget
        pygame.draw.rect(screen, (255, 165, 0), (restart_rect.left - 10, restart_rect.top - 10, restart_rect.width + 20, restart_rect.height + 20), 2)
        screen.blit(game_over_text, game_over_rect)
        screen.blit(restart_text, restart_rect)

    def reset(self):
        self.paddle = Paddle()
        self.ball = Ball()
        self.score = 0
        self.game_over = False
        self.game_started = True  # Azonnal elindítjuk a játékot

    def run(self):
        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if not self.game_started:
                        if 340 <= mouse_pos[0] <= 460 and 240 <= mouse_pos[1] <= 280:
                            self.game_started = True
                    elif self.game_over:
                        if 290 <= mouse_pos[0] <= 510 and 290 <= mouse_pos[1] <= 330:
                            self.reset()

            if self.game_started and not self.game_over:
                self.handle_input()
                self.update()
            self.draw(screen)
            clock.tick(60)

        pygame.quit()