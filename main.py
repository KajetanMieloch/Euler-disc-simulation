import pygame
import sys
import random
import math
import cv2
import numpy as np

class Disc:
    def __init__(self, x, y, radius, color, dx, dy, deltat):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = dx
        self.dy = dy
        self.deltat = deltat

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def move(self, width, height, cx, cy):
        Rc = 50
        dist_x = cx - self.x
        dist_y = cy - self.y
        r = math.sqrt(dist_x**2 + dist_y**2)

        if r < Rc:
            r = Rc
        
        force = 20000 / (r**3 + 100)

        fx = force * (dist_x)
        fy = force * (dist_y)

        self.dx += fx * self.deltat
        self.dy += fy * self.deltat

        self.x += self.dx * self.deltat
        self.y += self.dy * self.deltat

        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.dx = -self.dx
        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.dy = -self.dy

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Disc sim")
deltat = 0.05

cx, cy = width // 2, height // 2

N = 1000
discs = []

for _ in range(N):
    x = random.randint(50, width - 50)
    y = random.randint(50, height - 50)
    radius = random.randint(1, 10)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    dx = random.choice([-5, 5])
    dy = random.choice([-5, 5])
    discs.append(Disc(x, y, radius, color, dx, dy, deltat))

# Initialize OpenCV video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('gameplay.mp4', fourcc, 60.0, (width, height))

running = True
clock = pygame.time.Clock()
elapsed_time = 0
record_duration = 60  # 1 minute

while running and elapsed_time < record_duration:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))

    for disc in discs:
        disc.move(width, height, cx, cy)
        disc.draw(window)

    pygame.display.flip()

    # Capture frame from Pygame and convert it to OpenCV format
    frame = pygame.surfarray.array3d(window)
    frame = np.rot90(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # Write frame to video
    out.write(frame)

    clock.tick(120)  # Set frame rate to 60 fps
    elapsed_time += 1 / 60

out.release()
pygame.quit()
sys.exit()

