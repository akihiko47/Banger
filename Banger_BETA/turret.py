
from bullet import *
from images import *
from effects import *

pygame.init()


class Turret(pygame.sprite.Sprite):
    def __init__(self, x, y, image, cannon_image, damage, cooldown, bullet_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.cannon_image = cannon_image
        self.rect = self.image.get_rect(center=(x, y))
        self.damage = damage
        self.last_move = 0
        self.cooldown = cooldown
        self.reload = 0
        self.bullet_speed = bullet_speed

    def update_draw_shoot(self, enemies):
        closest = 1000
        closest_enemy = None
        for enemy in enemies:
            rel_x, rel_y = enemy.rect.x - self.rect.x - 21, enemy.rect.y - self.rect.y - 21
            dist = (rel_x**2 + rel_y**2)**0.5
            if dist < closest:
                closest = dist
                closest_enemy = enemy
        screen.blit(self.image, self.rect)

        """cannon rotation"""
        if closest_enemy:
            mouse_x, mouse_y = closest_enemy.rect.x, closest_enemy.rect.y
            rel_x, rel_y = mouse_x - self.rect.x - 21, mouse_y - self.rect.y - 21
            angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) - 90
            image = pygame.transform.rotate(self.cannon_image, int(angle))
            rect = image.get_rect(center=(self.rect.x + 21, self.rect.y + 21))
            screen.blit(image, rect)
            self.last_move = angle
        else:
            image = pygame.transform.rotate(self.cannon_image, self.last_move)
            rect = image.get_rect(center=(self.rect.x + 21, self.rect.y + 21))
            screen.blit(image, rect)

        """shoot"""
        if self.reload <= 0 and closest_enemy:
            self.reload = self.cooldown
            return Bullet(self.rect.x+19, self.rect.y+21, closest_enemy.rect.x, closest_enemy.rect.y,
                          self.bullet_speed, bullet_img)
        else:
            self.reload -= 1
            return None
