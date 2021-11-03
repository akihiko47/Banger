from random import randint, choice
import math
import pygame
from data.scripts.effects import *

pygame.init()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed, hp, attack, cost, image):
        pygame.sprite.Sprite.__init__(self)
        r = randint(1, 3)
        if r == 1:
            self.x = choice([randint(-800, -20), randint(820, 1600)])
            self.y = choice([randint(-800, -20), randint(820, 1600)])
        elif r == 2:
            self.x = randint(-800, 1600)
            self.y = randint(-800, -20)
        else:
            self.x = randint(-800, 1600)
            self.y = randint(820, 1600)
        self.image = image
        self.new_image = self.image
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.speed = speed
        self.hp = hp
        self.attack = attack
        self.cost = cost
        self.full_hp = hp

    def update(self, plr_pos):
        if self.hp < self.full_hp:
            add_enemy_hit_smoke(self.rect.centerx, self.rect.centery)
        if self.hp <= 0:
            self.kill()
            return self.cost

        distance_x = self.rect.x - plr_pos[0]
        distance_y = self.rect.y - plr_pos[1]

        angle = math.atan2(distance_y, distance_x)
        speed_x = -(self.speed * math.cos(angle))
        speed_y = -(self.speed * math.sin(angle))

        self.rect.x += speed_x
        self.rect.y += speed_y

        angle_rot = (180 / math.pi) * -math.atan2(distance_y, distance_x) + 90
        self.image = pygame.transform.rotate(self.new_image, int(angle_rot))

        """smokes"""
        add_enemy_smokes(self.rect.centerx, self.rect.centery, [-speed_x, -speed_y])
