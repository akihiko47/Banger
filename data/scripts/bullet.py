import math
import pygame
from data.scripts.effects import *

pygame.init()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, mouse_x, mouse_y, speed, image):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.dest_x = mouse_x
        self.dest_y = mouse_y

    def update(self, *args):
        """smokes"""
        add_bullet_smokes(self.rect.centerx, self.rect.centery)

        distance_x = self.x - self.dest_x
        distance_y = self.y - self.dest_y

        angle = math.atan2(distance_y, distance_x)
        speed_x = -(self.speed * math.cos(angle))
        speed_y = -(self.speed * math.sin(angle))

        self.rect.x += int(speed_x)
        self.rect.y += int(speed_y)
