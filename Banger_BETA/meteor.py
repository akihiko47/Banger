from text import *
from parameters import *
from images import *

pygame.init()


class Meteor(pygame.sprite.Sprite):
    def __init__(self, x, y, image, damage, hp):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.rect.x = x
        self.rect.y = y
        self.damage = damage
        self.hp = hp

    def update(self):
        if self.hp <= 0:
            self.kill()

    def draw(self, surf):
        surf.blit(self.image, (self.rect.x, self.rect.y))
        if self.image == meteor_med_img:
            message_to_screen(str(self.hp), YELLOW, small_font, self.rect.x+20, self.rect.y+20)
        else:
            message_to_screen(str(self.hp), YELLOW, small_font, self.rect.x + 40, self.rect.y + 40)
