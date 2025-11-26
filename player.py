import pygame
import math

WHITE = (255, 255, 255)
BLUE = (70, 120, 220)

class Player:
    def __init__(self):
        self.width = 50
        self.height = 30
        self.x = 400
        self.y = 540
        self.speed = 6
        self.color = BLUE
        self.lives = 3
        self.shoot_cooldown = 0.25
        self.time_since_shot = 0

    def move(self, dx):
        self.x += dx * self.speed
        self.x = max(self.width // 2, min(800 - self.width // 2, self.x))

    def draw(self, surf):
        points = [
            (self.x, self.y - self.height // 2),
            (self.x - self.width // 2, self.y + self.height // 2),
            (self.x + self.width // 2, self.y + self.height // 2)
        ]
        pygame.draw.polygon(surf, self.color, points)
        pygame.draw.circle(surf, WHITE, (int(self.x), int(self.y)), 4)

    def can_shoot(self, dt):
        self.time_since_shot += dt
        if self.time_since_shot >= self.shoot_cooldown:
            self.time_since_shot = 0
            return True
        return False
