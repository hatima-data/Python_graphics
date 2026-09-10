import pygame
import math
import random
#heart

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Heart - Python")

clock = pygame.time.Clock()

CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
SCALE = 12

particles = []

def heart_point(t):
    x = 16 * math.sin(t) ** 3
    y = (
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )
    return x * SCALE, -y * SCALE

running = True
t = 0

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for _ in range(6):
        x, y = heart_point(t)
        particles.append([
            CENTER_X + x + random.uniform(-2, 2),
            CENTER_Y + y + random.uniform(-2, 2),
            255
        ])
    t += 0.02

    for p in particles[:]:
        p[2] -= 3
        if p[2] <= 0:
            particles.remove(p)
            continue

        alpha = max(0, min(255, p[2]))
        pygame.draw.circle(
            screen,
            (255, 0, alpha),
            (int(p[0]), int(p[1])),
            2
        )

    pygame.display.flip()

pygame.quit()