import pygame
import random
import math

RED   = (220, 60, 60)
GREEN = (60, 220, 60)
GRAY  = (140, 140, 140)

class Enemy:
    def __init__(self, x, y, kind="basic", speed=100, health=1):
        self.x = x
        self.y = y
        self.kind = kind
        self.speed = speed
        self.health = health
        self.width = 40 if kind != "big" else 70
        self.height = 28 if kind != "big" else 48
        self.color = RED if kind == "basic" else (GREEN if kind == "zigzag" else GRAY)

        self.angle = random.uniform(0, math.pi * 2)
        self.freq = 2.0

    def update(self, dt):
        if self.kind == "basic":
            self.y += self.speed * dt

        elif self.kind == "zigzag":
            self.y += self.speed * dt
            self.x += math.sin(self.angle) * 80 * dt
            self.angle += self.freq * dt * 2

        else:  # big
            self.y += (self.speed * 0.6) * dt

    def draw(self, surf):
        rect = pygame.Rect(
            int(self.x - self.width/2),
            int(self.y - self.height/2),
            self.width,
            self.height
        )
        pygame.draw.rect(surf, self.color, rect)

        if self.health > 1:
            hp_w = int(self.width * (self.health / 3))
            pygame.draw.rect(surf, (200,0,0), (rect.left, rect.top - 6, self.width, 4))
            pygame.draw.rect(surf, (0,200,0), (rect.left, rect.top - 6, hp_w, 4))

    def is_off_screen(self):
        return self.y > 650

    def hit(self, damage=1):
        self.health -= damage
        return self.health <= 0
