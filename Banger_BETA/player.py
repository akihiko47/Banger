import math
from sounds import *
from effects import *

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, hp, cannon_file, filename):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.hp = hp
        self.cannon_image = pygame.image.load(cannon_file).convert_alpha()
        self.move_sound = False

    def update_player(self):
        """smokes"""
        if self.hp <= 50:
            add_plr_hit_smoke(self.rect.centerx, self.rect.centery)
        """player movements"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 4:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 602:
            self.rect.y += self.speed
        if keys[pygame.K_a] and self.rect.x > 4:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < 752:
            self.rect.x += self.speed
        if 1 in keys:
            if not self.move_sound:
                pygame.mixer.Sound.play(move_sound)
                self.move_sound = True
        else:
            self.move_sound = False
            pygame.mixer.Sound.stop(move_sound)

    def draw(self):
        """cannon rotation"""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.rect.centerx, mouse_y - self.rect.centery
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) - 90
        image = pygame.transform.rotate(self.cannon_image, int(angle))
        rect = image.get_rect(center=(self.rect.x+21, self.rect.y+21))

        """drawing"""
        screen.blit(self.image, self.rect)
        screen.blit(image, rect)
