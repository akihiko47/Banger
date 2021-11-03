import random
from data.scripts.parameters import *
import pygame
from data.images.images import *

pygame.init()

smokes = []
enemy_smokes = []
enemy_hit_smoke = []
bullet_smokes = []
background_parts = []
background_cooldown = 60
background_reload = 0
player_shots = []
explosion_wave = []
explosion_smokes = []
hit_effects = []
plr_hit_smokes = []
turrets_shots = []
background_balls = []
background_smokes = []
ball_cooldown = 30
ball_reload = 0


def add_smokes(keys, cord_x, cord_y):  # [rad, vel, pos, shrink]
    if keys[pygame.K_w]:
        vel = [random.uniform(-1.0, 1.0), random.randint(3, 7)]
        smokes.append([5, vel, [cord_x, cord_y], random.uniform(0.2, 0.4)])
    if keys[pygame.K_d]:
        vel = [random.randint(-7, -3), random.uniform(-1.0, 1.0)]
        smokes.append([5, vel, [cord_x, cord_y], random.uniform(0.2, 0.4)])
    if keys[pygame.K_s]:
        vel = [random.uniform(-1.0, 1.0), random.randint(-7, -3)]
        smokes.append([5, vel, [cord_x, cord_y], random.uniform(0.2, 0.4)])
    if keys[pygame.K_a]:
        vel = [random.randint(3, 7), random.uniform(-1.0, 1.0)]
        smokes.append([5, vel, [cord_x, cord_y], random.uniform(0.2, 0.4)])


def add_enemy_hit_smoke(cord_x, cord_y):  # [pos rad shrink]
    cord_x += random.randint(-5, 5)
    cord_y += random.randint(-5, 5)
    enemy_hit_smoke.append([[cord_x, cord_y], random.randint(5, 10), random.uniform(0.1, 0.3)])


def add_plr_hit_smoke(cord_x, cord_y):   # [pos rad shrink]
    cord_x += random.randint(-5, 5)
    cord_y += random.randint(-5, 5)
    plr_hit_smokes.append([[cord_x, cord_y], random.randint(5, 10), random.uniform(0.1, 0.3)])


def add_enemy_smokes(cord_x, cord_y, vel):  # [pos, rad, shrink, vel, color]
    vel[0] += random.uniform(-0.6, 0.6)
    vel[1] += random.uniform(-0.6, 0.6)
    enemy_smokes.append([[cord_x, cord_y], 5, random.uniform(0.1, 0.3), vel, RED])
    enemy_smokes.append([[cord_x, cord_y], 5, random.uniform(0.3, 0.5), vel, RED_DARKER])


def add_bullet_smokes(cord_x, cord_y):  # [pos rad shrink]
    cord_x += random.randint(-5, 5)
    cord_y += random.randint(-5, 5)
    bullet_smokes.append([[cord_x, cord_y], 5, random.uniform(0.1, 0.4)])


def add_shot_effect(coord_x, coord_y):  # [pos, rad, growth, border, border_shrink]
    pos = [coord_x, coord_y]
    rad = 0
    growth = 3
    border = 20
    border_shrink = 1
    player_shots.append([pos, rad, growth, border, border_shrink])


def add_turret_shot(coord_x, coord_y):  # [pos, rad, growth, border, border_shrink]
    pos = [coord_x, coord_y]
    rad = 0
    growth = 3
    border = 20
    border_shrink = 1
    turrets_shots.append([pos, rad, growth, border, border_shrink])


def add_hit(coord_x, coord_y):
    pos = [coord_x, coord_y]
    rad = 0
    growth = 6
    border = 40
    border_shrink = 4
    hit_effects.append([pos, rad, growth, border, border_shrink])  # [pos, rad, growth, border, border_shrink]


def add_explosion(coord_x, coord_y):
    pos = [coord_x, coord_y]
    rad = 0
    growth = 6
    border = 30
    border_shrink = 2
    explosion_wave.append([pos, rad, growth, border, border_shrink])  # [pos, rad, growth, border, border_shrink]
    for i in range(20):
        pos = [coord_x, coord_y]
        rad = random.randint(10, 20)
        shrink = random.uniform(0.5, 0.9)
        vel = [random.randint(-3, 3), random.randint(-3, 3)]
        explosion_smokes.append([pos, rad, shrink, vel])  # [pos, rad, shrink, vel]


def add_background_ball():  # [pos, rad, shrink, vel]
    global ball_reload
    if not ball_reload:
        pos = [random.randint(0, 800), -100]
        rad = random.randint(50, 70)
        shrink = random.uniform(0.01, 0.1)
        vel = [0, random.uniform(1.0, 2.0)]
        background_balls.append([pos, rad, shrink, vel])
        ball_reload = ball_cooldown
    else:
        ball_reload -= 1
    for ball in background_balls:
        add_background_smokes(ball[0][0], ball[0][1], ball[1])


def add_background_smokes(coord_x, coord_y, rad):  # [pos, rad, shrink]
    pos = [coord_x+random.randint(-rad//2, rad//2), coord_y+random.randint(-rad//2, rad//2) - rad//5]
    rad = random.randint(1, int(rad)//2 + 2)
    shrink = random.uniform(0.05, 0.1)
    background_smokes.append([pos, rad, shrink])


def clear_effects():
    global smokes, explosion_smokes, enemy_hit_smoke, enemy_smokes, bullet_smokes, background_parts, player_shots, \
        explosion_wave, hit_effects, plr_hit_smokes, turrets_shots, background_balls, background_smokes

    smokes = []
    enemy_smokes = []
    enemy_hit_smoke = []
    bullet_smokes = []
    background_parts = []
    player_shots = []
    explosion_wave = []
    explosion_smokes = []
    hit_effects = []
    plr_hit_smokes = []
    turrets_shots = []
    background_balls = []
    background_smokes = []


def draw_smokes():
    for i, smoke in sorted(enumerate(plr_hit_smokes), reverse=True):
        pygame.draw.circle(screen, BLUE, smoke[0], smoke[1])
        smoke[1] -= smoke[2]
        if smoke[1] <= 0:
            plr_hit_smokes.pop(i)
    for i, smoke in sorted(enumerate(smokes), reverse=True):
        pygame.draw.circle(screen, BLUE, smoke[2], smoke[0])
        smoke[0] -= smoke[3]
        smoke[2][0] += smoke[1][0]
        smoke[2][1] += smoke[1][1]
        if smoke[0] <= 0:
            smokes.pop(i)
    for i, smoke in sorted(enumerate(enemy_hit_smoke), reverse=True):
        pygame.draw.circle(screen, RED, smoke[0], smoke[1])
        smoke[1] -= smoke[2]
        if smoke[1] <= 0:
            enemy_hit_smoke.pop(i)
    for i, smoke in sorted(enumerate(enemy_smokes), reverse=True):
        pygame.draw.circle(screen, smoke[4], smoke[0], smoke[1])
        smoke[1] -= smoke[2]
        smoke[0][0] += smoke[3][0] * 3
        smoke[0][1] += smoke[3][1] * 3
        if smoke[1] <= 0:
            enemy_smokes.pop(i)
    for i, smoke in sorted(enumerate(bullet_smokes), reverse=True):
        pygame.draw.circle(screen, BLUE, smoke[0], smoke[1])
        smoke[1] -= smoke[2]
        if smoke[1] <= 0:
            bullet_smokes.pop(i)
    for i, exp in sorted(enumerate(explosion_wave), reverse=True):
        pygame.draw.circle(screen, RED, exp[0], exp[1], exp[3])
        exp[1] += exp[2]
        exp[3] -= exp[4]
        if exp[3] <= 0:
            explosion_wave.pop(i)
    for i, exp in sorted(enumerate(turrets_shots), reverse=True):
        pygame.draw.circle(screen, BLUE, exp[0], exp[1], exp[3])
        exp[1] += exp[2]
        exp[3] -= exp[4]
        if exp[3] <= 0:
            turrets_shots.pop(i)
    for i, exp in sorted(enumerate(explosion_smokes), reverse=True):
        pygame.draw.circle(screen, RED, exp[0], exp[1])
        exp[0][0] += exp[3][0]
        exp[0][1] += exp[3][1]
        exp[1] -= exp[2]
        if exp[1] <= 0:
            explosion_smokes.pop(i)
    for i, exp in sorted(enumerate(hit_effects), reverse=True):
        pygame.draw.circle(screen, RED, exp[0], exp[1], exp[3])
        exp[1] += exp[2]
        exp[3] -= exp[4]
        if exp[3] <= 0:
            hit_effects.pop(i)


def update_shot_effect(coord_x, coord_y):
    for i, effect in sorted(enumerate(player_shots), reverse=True):
        effect[0] = [coord_x, coord_y]
        pygame.draw.circle(screen, BLUE, effect[0], effect[1], effect[3])
        effect[1] += effect[2]
        effect[3] -= effect[4]
        if effect[3] <= 0:
            player_shots.pop(i)


def draw_background_effects():
    for i, ball in sorted(enumerate(background_balls), reverse=True):
        pygame.draw.circle(screen, (62, 50, 100), ball[0], ball[1])
        ball[0][0] += ball[3][0]
        ball[0][1] += ball[3][1]
        ball[1] -= ball[2]
        if ball[1] <= 0:
            background_balls.pop(i)
    for i, smoke in sorted(enumerate(background_smokes), reverse=True):
        pygame.draw.circle(screen, (62, 50, 100), smoke[0], smoke[1])
        smoke[1] -= smoke[2]
        if smoke[1] <= 0:
            background_smokes.pop(i)
