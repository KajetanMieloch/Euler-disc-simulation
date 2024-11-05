import pygame
import sys
import random

class Disc:
    def __init__(self, x, y, radius, color, dx, dy):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = dx
        self.dy = dy

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def move(self, width, height, deltat):
        self.x += self.dx * deltat
        self.y += self.dy * deltat

        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.dx = -self.dx
        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.dy = -self.dy

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Disc sim")

N = 1000
discs = []

for _ in range(N):
    x = random.randint(50, width - 50)
    y = random.randint(50, height - 50)
    radius = random.randint(1, 10)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    dx = random.choice([-5, 5])
    dy = random.choice([-5, 5])
    discs.append(Disc(x, y, radius, color, dx, dy))

running = True
deltat = 0.1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))

    for disc in discs:
        disc.move(width, height, deltat)
        disc.draw(window)

    pygame.display.flip()

pygame.quit()
sys.exit()