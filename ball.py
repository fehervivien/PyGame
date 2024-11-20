import pygame
import random

"""A labda osztály, amely kezeli a labda mozgását és ütközéseit."""

# Labda osztály
class Ball:
    def __init__(self):
        self.size = 20
        self.rect = pygame.Rect((random.randint(0, 800 - self.size), 300), (self.size, self.size))
        self.speed = [5, -5]
        self.hit_paddle = False  # Új attribútum az ütközés nyomon követésére

    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def bounce(self, paddle):
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        if self.rect.colliderect(paddle.rect):
            if not self.hit_paddle:  # Csak akkor növeljük a pontszámot, ha még nem ütközött az ütővel
                self.speed[1] = -self.speed[1]
                self.hit_paddle = True
                return True  # Pontot ér el, ha eltalálja az ütőt
        else:
            self.hit_paddle = False  # Visszaállítjuk, ha már nem ütközik az ütővel
        return False

    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 0, 0), self.rect)  # Piros szín