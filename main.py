import pygame
import sys

WIDTH = 320
HEIGHT = 310
FPS = 90

walls = []
level = [
    "wwwwwwwwwwwwwwwwwwww",
    "w                  w",
    "w         wwwwww   w",
    "w   wwww       w   w",
    "w   w        wwww  w",
    "w www  wwww        w",
    "w   w     ww       w",
    "w   w     w   www ww",
    "w   www www   w w  w",
    "w     w   w   w w  w",
    "www   w   wwwww w  w",
    "w w      ww        w",
    "w w   wwww   w     w",
    "w     w      www   w",
    "w      w    w      w",
    "w       w  w       w",
    "w  w     w w       w",
    "w  www      e   wwww",
    "wwwwwwwwwwwwwwwwwwww",
]
class Wall(pygame.sprite.Sprite):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                self.move(-dx, -dy)
        if self.rect.colliderect(endRect):
            pygame.quit()
            sys.exit




screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("labyrinth")
clock = pygame.time.Clock()
x = 0
y = 0
for i in level:
    for j in i:
        if j == "w":
            Wall((x, y))
        if j == "e":
            endRect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0
player = Player()
running = True
while running:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.move(-1, 0)
    elif keys[pygame.K_d]:
        player.move(1, 0)
    elif keys[pygame.K_w]:
        player.move(0, -1)
    elif keys[pygame.K_s]:
        player.move(0, 1)

    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect, 2)
    pygame.draw.rect(screen, (200, 55, 55), endRect, 2)
    pygame.draw.rect(screen, (55, 200, 55), player.rect, 2)
    pygame.display.flip()

