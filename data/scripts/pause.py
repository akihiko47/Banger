from data.sounds.sounds import *
from data.scripts.parameters import *
from data.images.images import *
from data.scripts.parameters import *
from data.images.fonts.text import *
import pygame

pygame.init()

clock = pygame.time.Clock()


def pause():
    in_pause = True
    """sounds"""
    pygame.mixer.music.pause()
    pygame.mixer.Sound.play(change_sound)

    while in_pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            in_pause = False

        message_to_screen(screen, 'Paused', YELLOW, large_font, 400, 300)
        message_to_screen(screen, 'press space to continue', YELLOW, med_font, 400, 380)

        """update display"""
        pygame.display.update()
        clock.tick(60)

    """sounds"""
    pygame.mixer.Sound.play(change_sound)
    pygame.mixer.music.unpause()
