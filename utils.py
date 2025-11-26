import pygame
import random
from enemy import Enemy

WHITE = (255, 255, 255)

font_name = pygame.font.get_default_font()

def draw_text(surf, text, size, x, y, color=WHITE, center=True):
    font = pygame.font.SysFont(font_name, size)
    surf_obj = font.render(text, True, color)
    rect = surf_obj.get_rect()
    rect.center = (x, y) if center else (x, y)
    surf.blit(surf_obj, rect)

def spawn_enemy(wave):
    r = random.random()
    if r < 0.6:
        kind = "basic"
        speed = 80 + wave * 6
        health = 1
    elif r < 0.9:
        kind = "zigzag"
        speed = 70 + wave * 5
        health = 1
    else:
        kind = "big"
        speed = 40 + wave * 3
        health = 2 + wave // 4

    x = random.randint(40, 760)
    return Enemy(x, -40, kind=kind, speed=speed, health=health)

def handle_collisions(bullets, enemies, player):
    score_gain = 0

    for b in bullets[:]:
        if b.owner == "player":
            for e in enemies[:]:
                if (e.x - e.width/2 <= b.x <= e.x + e.width/2 and
                    e.y - e.height/2 <= b.y <= e.y + e.height/2):

                    bullets.remove(b)
                    if e.hit():
                        enemies.remove(e)
                        score_gain += 100
                    break

    for e in enemies[:]:
        if (e.x - e.width/2 <= player.x <= e.x + e.width/2 and
            e.y - e.height/2 <= player.y <= e.y + e.height/2):
            enemies.remove(e)
            player.lives -= 1

    return score_gain
