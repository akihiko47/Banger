import pygame

pygame.init()

"""images"""
background_img = pygame.image.load('backgrounds/background.png').convert_alpha()
player_img_0 = pygame.image.load('player/player_model_0.png').convert_alpha()
player_img_1 = pygame.image.load('player/player_model_1.png').convert_alpha()
player_img_2 = pygame.image.load('player/player_model_2.png').convert_alpha()
bullet_img = pygame.image.load('player/shot_image.png').convert_alpha()
enemy_img_0 = pygame.image.load('enemies/enemy_model_0.png').convert_alpha()
enemy_img_1 = pygame.image.load('enemies/enemy_model_1.png').convert_alpha()
enemy_img_2 = pygame.image.load('enemies/enemy_model_2.png').convert_alpha()
icon_img = pygame.image.load('icon/icon.png').convert_alpha()
meteor_big_img = pygame.image.load('meteors/big.png').convert_alpha()
meteor_big_green_img = pygame.image.load('meteors/big_green.png').convert_alpha()
meteor_med_img = pygame.image.load('meteors/med.png').convert_alpha()
meteor_med_green_img = pygame.image.load('meteors/med_green.png').convert_alpha()
turret_body_img = pygame.image.load('turret/turret_body.png').convert_alpha()
turret_cannon_img = pygame.image.load('turret/turret_gun.png').convert_alpha()
turret_full_img = pygame.image.load('turret/turret_full.png').convert_alpha()
turret_full_green_img = pygame.image.load('turret/turret_full_green.png').convert_alpha()
sound_icon_img = pygame.image.load('icon/audioOn.png').convert_alpha()
sound_plus_img = pygame.image.load('icon/plus.png').convert_alpha()
sound_minus_img = pygame.image.load('icon/minus.png').convert_alpha()