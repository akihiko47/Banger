import pygame

pygame.init()

pygame.mixer.pre_init(44100, 16, 2, 4096)

button_sound = pygame.mixer.Sound(r'data\sounds\button_pressing.wav')
bullet_sound = pygame.mixer.Sound(r'data\sounds\shot_sound.wav')
bullet_sound.set_volume(0.3)
death_sound = pygame.mixer.Sound(r'data\sounds\death.wav')
death_sound.set_volume(0.3)
change_sound = pygame.mixer.Sound(r'data\sounds\change_sound.wav')
change_sound.set_volume(0.3)
crash_sound = pygame.mixer.Sound(r'data\sounds\crash.wav')
crash_sound.set_volume(0.3)
place_sound = pygame.mixer.Sound(r'data\sounds\place.wav')
place_sound.set_volume(0.3)
move_sound = pygame.mixer.Sound(r'data\sounds\move_2.wav')
move_sound.set_volume(0.3)
hit_to_enemy_sound = pygame.mixer.Sound(r'data\sounds\hit_to_enemy.wav')
hit_to_enemy_sound.set_volume(0.3)


def change_volume(volume):
    button_sound.set_volume(volume)
    bullet_sound.set_volume(volume)
    death_sound.set_volume(volume)
    change_sound.set_volume(volume)
    crash_sound.set_volume(volume)
    place_sound.set_volume(volume)
    move_sound.set_volume(volume)
    hit_to_enemy_sound.set_volume(volume)
