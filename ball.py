import pygame
import random

"""A labda osztály, amely kezeli a labda mozgását 
   és ütközéseit."""

# Labda osztály
class Ball:
    def __init__(self):
        self.size = 20
        self.rect = pygame.Rect((random.randint(0, 800 - self.size), 300), (self.size, self.size))
        self.speed = [5, -5]

    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def bounce(self, paddle):
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0 or self.rect.colliderect(paddle.rect):
            self.speed[1] = -self.speed[1]
        if self.rect.bottom >= 600:
            return False  # Játék vége
        return True

    def draw(self, screen):
        pygame.draw.ellipse(screen, (0, 0, 255), self.rect)  # Fehér szín
