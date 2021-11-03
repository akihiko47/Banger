import pygame

pygame.init()

pygame.mixer.init(48000, -16, 1, 1024)

button_sound = pygame.mixer.Sound('sounds/button_pressing.mp3')
bullet_sound = pygame.mixer.Sound('sounds/shot_sound.mp3')
bullet_sound.set_volume(0.3)
death_sound = pygame.mixer.Sound('sounds/death.wav')
death_sound.set_volume(0.3)
change_sound = pygame.mixer.Sound('sounds/change_sound.mp3')
change_sound.set_volume(0.3)
crash_sound = pygame.mixer.Sound('sounds/crash.wav')
crash_sound.set_volume(0.3)
place_sound = pygame.mixer.Sound('sounds/place.wav')
place_sound.set_volume(0.3)
move_sound = pygame.mixer.Sound('sounds/move_2.mp3')
move_sound.set_volume(0.3)
hit_to_enemy_sound = pygame.mixer.Sound('sounds/hit_to_enemy.wav')
hit_to_enemy_sound.set_volume(0.3)


def change_volume(volume):
    button_sound.set_volume(volume)
    bullet_sound.set_volume(volume)
    death_sound.set_volume(volume)
    change_sound.set_volume(volume)
    crash_sound.set_volume(volume)
    place_sound.set_volume(volume)
    move_sound.set_volume(volume)
