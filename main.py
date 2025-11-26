import pygame
import sys
from player import Player
from bullet import Bullet
from enemy import Enemy
from utils import draw_text, spawn_enemy, handle_collisions

WIDTH, HEIGHT = 800, 600
FPS = 60

def show_main_menu():
    selected = 0
    options = ["Start", "Quit"]
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    return options[selected]

        screen.fill((20,20,40))
        draw_text(screen, "Galactic Rescue", 50, WIDTH//2, 120)

        for i, opt in enumerate(options):
            color = (255,255,0) if selected == i else (255,255,255)
            draw_text(screen, opt, 32, WIDTH//2, 250 + i*60, color=color)

        pygame.display.flip()
        clock.tick(FPS)

def run_game():
    player = Player()
    bullets = []
    enemies = []
    clock = pygame.time.Clock()

    last_time = pygame.time.get_ticks() / 1000
    spawn_timer = 0
    score = 0
    wave = 1

    while True:
        now = pygame.time.get_ticks() / 1000
        dt = now - last_time
        last_time = now

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        keys = pygame.key.get_pressed()

        dx = (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a])
        player.move(dx)

        if keys[pygame.K_SPACE] and player.can_shoot(dt):
            bullets.append(Bullet(player.x, player.y - 25))

        spawn_timer += dt
        if spawn_timer >= 1.0:
            spawn_timer = 0
            enemies.append(spawn_enemy(wave))

        for b in bullets[:]:
            b.update(dt)
            if b.off_screen():
                bullets.remove(b)

        for e in enemies[:]:
            e.update(dt)
            if e.is_off_screen():
                enemies.remove(e)
                player.lives -= 1

        score += handle_collisions(bullets, enemies, player)

        if player.lives <= 0:
            return

        screen.fill((10,10,20))
        draw_text(screen, f"Score: {score}", 20, 10, 10, center=False)
        draw_text(screen, f"Lives: {player.lives}", 20, WIDTH - 100, 10, center=False)

        player.draw(screen)
        for b in bullets:
            b.draw(screen)
        for e in enemies:
            e.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

def main():
    while True:
        choice = show_main_menu()
        if choice == "Start":
            run_game()
        else:
            pygame.quit()
            sys.exit()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galactic Rescue")
main()
