import pygame
import random

# Inicializáljuk a pygame-et
pygame.init()

# Színek
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Képernyő beállítások
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Egyszerű Pong Játék")

# Ütő beállítások
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
paddle_speed = 10
paddle = pygame.Rect((SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 30), (PADDLE_WIDTH, PADDLE_HEIGHT))

# Labda beállítások
BALL_SIZE = 10
ball = pygame.Rect((random.randint(0, SCREEN_WIDTH - BALL_SIZE), SCREEN_HEIGHT // 2), (BALL_SIZE, BALL_SIZE))
ball_speed = [5, -5]

# Pontszám
score = 0
font = pygame.font.Font(None, 36)

# Játék ciklus
running = True
while running:
    # Eseménykezelés
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ütő mozgatása
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
        paddle.right += paddle_speed

    # Labda mozgatása
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ütközések ellenőrzése
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]
        score += 1
    if ball.bottom >= SCREEN_HEIGHT:
        ball.x, ball.y = random.randint(0, SCREEN_WIDTH - BALL_SIZE), SCREEN_HEIGHT // 2
        ball_speed[1] = -5
        score = 0

    # Képernyő frissítése
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    score_text = font.render(f"Pontszám: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
