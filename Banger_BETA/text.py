import pygame
from parameters import screen

pygame.init()

small_font = pygame.font.Font('fonts/Squirk.ttf', 20)
med_font = pygame.font.Font('fonts/Squirk.ttf', 45)
large_font = pygame.font.Font('fonts/Squirk.ttf', 80)


def message_to_screen(msg, color, font, x, y):
    sc_text = font.render(msg, True, color)
    pos = sc_text.get_rect(center=(x, y))
    screen.blit(sc_text, pos)
