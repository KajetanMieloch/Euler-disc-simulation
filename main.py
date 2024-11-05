import pygame
import sys


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

    def move(self, width, height):
        self.x += self.dx
        self.y += self.dy

        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.dx = -self.dx
        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.dy = -self.dy

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Disc sim")

d = Disc(400, 300, 50, (255, 255, 255), 5, 5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))

    d.move(width, height)
    d.draw(window)

    pygame.display.flip()

pygame.quit()
sys.exit()