from sounds import *
from text import *
from parameters import *
import pygame


class Button:
    def __init__(self, width, height, x, y, inactive_color, active_color, text_color, border_width=5, border_angle=15):
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.text_color = text_color
        self.border_width = border_width
        self.border_angle = border_angle
        self.x = x
        self.y = y

    def draw(self, msg, font, mouse):
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            pygame.draw.rect(screen, self.active_color, (self.x, self.y, self.width, self.height),
                             self.border_width, self.border_angle)
        else:
            pygame.draw.rect(screen, self.inactive_color, (self.x, self.y, self.width, self.height),
                             self.border_width, self.border_angle)

        message_to_screen(msg, self.text_color, font, self.x + self.width // 2, self.y + self.height // 2)

    def is_over(self, mouse):
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            pygame.mixer.Sound.play(button_sound)
            return True

        return False


