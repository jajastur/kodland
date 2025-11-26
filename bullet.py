import pygame

YELLOW = (240, 230, 80)

class Bullet:
    def __init__(self, x, y, vy=-400, color=YELLOW, radius=5, owner="player"):
        self.x = x
        self.y = y
        self.vy = vy
        self.color = color
        self.radius = radius
        self.owner = owner

    def update(self, dt):
        self.y += self.vy * dt

    def draw(self, surf):
        pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), self.radius)

    def off_screen(self):
        return self.y < -10 or self.y > 610
