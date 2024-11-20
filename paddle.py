import pygame

"""Az ütő osztály, amely kezeli az ütő mozgását és megjelenítését."""

# Ütő osztály
class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.rect = pygame.Rect((400 - self.width // 2, 570), (self.width, self.height))  # Középre állítva
        self.speed = 10

    def move(self, direction):
        if direction == "left" and self.rect.left > 0:
            self.rect.left -= self.speed
        elif direction == "right" and self.rect.right < 800:
            self.rect.right += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)  # Fehér szín