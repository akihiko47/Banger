from button import *
from enemy import *
from player import *
from pause import *
from meteor import *
from turret import *
from effects import *
import pygame
import random
from time import sleep

pygame.init()


class Game:
    def __init__(self):
        """icon"""
        pygame.display.set_icon(icon_img)
        pygame.display.set_caption('The Banger!')

        """fps part"""
        self.clock = pygame.time.Clock()
        self.FPS = 60

        """sound"""
        self.volume = 0.3

        """difficulty level"""
        self.diff_c = [(29, 204, 31), (217, 205, 39), (235, 88, 52)]
        self.difficulty = 0

        """groups"""
        self.plr_bullets = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.enemy_types_0 = (
            {'image': enemy_img_0, 'speed': random.uniform(1.5, 2.0), 'hp': 1, 'damage': 5, 'cost': 2},
            {'image': enemy_img_1, 'speed': random.uniform(4.0, 5.0), 'hp': 1, 'damage': 10, 'cost': 6},
            {'image': enemy_img_2, 'speed': random.uniform(3.0, 3.5), 'hp': 3, 'damage': 20, 'cost': 10})

        self.enemy_types_1 = (
            {'image': enemy_img_0, 'speed': random.uniform(1.5, 2.0), 'hp': 1, 'damage': 10, 'cost': 1},
            {'image': enemy_img_1, 'speed': random.uniform(4.0, 5.0), 'hp': 1, 'damage': 20, 'cost': 4},
            {'image': enemy_img_2, 'speed': random.uniform(3.0, 3.5), 'hp': 4, 'damage': 30, 'cost': 8})

        self.enemy_types_2 = (
            {'image': enemy_img_0, 'speed': random.uniform(1.5, 2.0), 'hp': 1, 'damage': 20, 'cost': 1},
            {'image': enemy_img_1, 'speed': random.uniform(4.0, 5.0), 'hp': 2, 'damage': 30, 'cost': 4},
            {'image': enemy_img_2, 'speed': random.uniform(3.0, 3.5), 'hp': 5, 'damage': 40, 'cost': 8})

        """waves"""
        self.wave = 0
        self.wave_cooldown = 10
        self.wave_times = {5: 10, 10: 15, 10000: 20}
        self.waves_0 = (
            '1', '1' * 3, '1' * 4, '2', '1' * 6, '2' * 3, '2' * 3 + '1' * 5, '3', '3' * 2, '3' * 3, '1' * 10,
            '1' * 15 + '2' * 5 + '3', '2' * 10, '3' * 5, '3' * 10, '3' * 10 + '2' * 10, '3' * 15, '3' * 30, '3' * 50)
        self.waves_1 = (
            '1' * 2, '1' * 3, '1' * 3 + '2', '2' * 2, '2' * 4, '2' * 5 + '1' * 3, '3', '3' * 3,
            '3' * 3 + '2' * 3 + '1' * 3, '1' * 10,
            '2' * 5, '3' * 10, '3' * 10 + '1' * 10, '2' * 15, '1' * 30, '1' * 10 + '2' * 15, '3' * 20, '3' * 30)
        self.waves_2 = ('1'*3, '2', '3', '3' * 3, '3' * 3 + '2' * 3 + '1' * 3, '3' * 5, '2' * 5 + '3' * 5, '3' * 10)

        """values"""
        self.plr = None
        self.player_hp = 100
        self.player_pos = (W // 2, H // 2)

        self.player_durability = 1
        self.durability_cost = 5

        self.player_speed = 3
        self.speed_cost = 5

        self.player_body_level = 0
        self.player_cannon_level = 0

        self.player_damage = 1
        self.damage_cost = 5

        self.reload_cooldown = 120
        self.reload_cost = 5
        self.reload = 0
        self.bullet_speed = 9

        self.time = 0
        self.money = 0

        """meteors"""
        self.meteors = pygame.sprite.Group()
        self.placing_med = False
        self.placing_big = False
        self.meteors_reload = 20
        self.meteors_cooldown = 20
        self.med_cost = 10
        self.big_cost = 50

        """turret"""
        self.placing_turret = False
        self.turret_cost = 100
        self.turrets = pygame.sprite.Group()
        self.turret_damage = 2
        self.turrets_bullets = pygame.sprite.Group()
        self.turret_reload_cooldown = 60
        self.turret_reload = 0

        """screen shake"""
        self.screen_shake = 0

    def game_menu(self):
        menu = True

        """changing time to 0 for the next game"""
        self.time = 0

        """music"""
        pygame.mixer.music.load('sounds/menu_music.mp3')
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1)

        """sound buttons"""
        sound_plus_button = Button(51, 51, 65, 730, YELLOW, ORANGE, YELLOW, 2, 5)
        sound_minus_button = Button(51, 51, 125, 730, YELLOW, ORANGE, YELLOW, 2, 5)

        """start button"""
        start_button = Button(550, 100, 125, 100, YELLOW, ORANGE, YELLOW)

        """effects"""
        clear_effects()

        while menu:

            """changing colors of difficulty buttons"""
            color0, color1, color2 = YELLOW, YELLOW, YELLOW
            if self.difficulty == 0:
                color0 = ORANGE
            elif self.difficulty == 1:
                color1 = ORANGE
            else:
                color2 = ORANGE

            easy_button = Button(300, 70, 250, 300, YELLOW, ORANGE, color0)
            med_button = Button(300, 70, 250, 390, YELLOW, ORANGE, color1)
            hard_button = Button(300, 70, 250, 480, YELLOW, ORANGE, color2)

            """background"""
            mouse = pygame.mouse.get_pos()
            screen.blit(background_img, (-mouse[0] // 3, -mouse[1] // 3))
            add_background_ball()
            draw_background_effects()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        menu = False
                        self.game()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_button.is_over(mouse):
                        self.change_difficulty(0)
                    if med_button.is_over(mouse):
                        self.change_difficulty(1)
                    if hard_button.is_over(mouse):
                        self.change_difficulty(2)
                    if start_button.is_over(mouse):
                        self.game()
                    if sound_plus_button.is_over(mouse):
                        self.change_volume_plus()
                    if sound_minus_button.is_over(mouse):
                        self.change_volume_minus()

            """drawing diff buttons"""
            easy_button.draw('EASY', med_font, mouse)
            med_button.draw('MEDIUM', med_font, mouse)
            hard_button.draw('HARD', med_font, mouse)

            message_to_screen('Difficulties:', YELLOW, med_font, 400, 270)

            """sound"""
            sound_plus_button.draw('', small_font, mouse)
            sound_minus_button.draw('', small_font, mouse)

            screen.blit(sound_icon_img, (15, 730))
            screen.blit(sound_plus_img, (65, 730))
            screen.blit(sound_minus_img, (125, 730))

            """making start game button"""
            start_button.draw('Start Game', large_font, mouse)

            """display update"""
            pygame.display.update()
            self.clock.tick(self.FPS)

    def change_volume_plus(self):
        if self.volume < 1:
            self.volume += 0.1
        pygame.mixer.music.set_volume(self.volume)
        change_volume(self.volume)

    def change_volume_minus(self):
        if 0 < self.volume:
            self.volume -= 0.1
        pygame.mixer.music.set_volume(self.volume)
        change_volume(self.volume)

    def create_player(self, x, y):
        """creates new player to change models"""
        if self.plr:
            hp = self.plr.hp
        else:
            hp = self.player_hp
        return Player(x, y,
                      self.player_speed,
                      hp,
                      f'player/cannon_{self.player_cannon_level}.png',
                      f'player/player_model_{self.player_body_level}.png')

    def collide_enemies_plr(self, plr):
        """check collision between enemies and player"""
        for enemy in self.enemy_group:
            if plr.rect.colliderect(enemy):
                pygame.mixer.Sound.play(crash_sound)
                add_explosion(enemy.rect.centerx, enemy.rect.centery)
                plr.hp -= enemy.attack * self.player_durability
                self.screen_shake = 20
                enemy.kill()

    def collide_bullets_enemy(self, plr):
        """check collision between bullets and enemies"""
        for enemy in self.enemy_group:
            for bullet in self.plr_bullets:
                if bullet.rect.colliderect(enemy):
                    bullet.kill()
                    pygame.mixer.Sound.play(hit_to_enemy_sound)
                    add_hit(enemy.rect.centerx, enemy.rect.centery)
                    enemy.hp -= self.player_damage
                    cost = enemy.update((plr.rect.x, plr.rect.y))
                    if cost:
                        add_explosion(enemy.rect.centerx, enemy.rect.centery)
                        pygame.mixer.Sound.play(crash_sound)
                        self.screen_shake = 10
                        self.money += cost

    def collide_turrets_bullets_enemy(self, plr):
        """check collision between bullets and enemies"""
        for enemy in self.enemy_group:
            for bullet in self.turrets_bullets:
                if bullet.rect.colliderect(enemy):
                    bullet.kill()
                    pygame.mixer.Sound.play(hit_to_enemy_sound)
                    add_hit(enemy.rect.centerx, enemy.rect.centery)
                    enemy.hp -= self.turret_damage
                    cost = enemy.update((plr.rect.x, plr.rect.y))
                    if cost:
                        add_explosion(enemy.rect.centerx, enemy.rect.centery)
                        pygame.mixer.Sound.play(crash_sound)
                        self.screen_shake = 10
                        self.money += cost

    def collide_meteors_enemy(self, plr):
        """check collision between meteors and enemies"""
        for enemy in self.enemy_group:
            for meteor in self.meteors:
                if meteor.rect.colliderect(enemy):
                    meteor.hp -= enemy.attack
                    enemy.hp -= meteor.damage
                    add_hit(enemy.rect.centerx, enemy.rect.centery)
                    cost = enemy.update((plr.rect.x, plr.rect.y))
                    if cost:
                        pygame.mixer.Sound.play(crash_sound)
                        add_explosion(enemy.rect.centerx, enemy.rect.centery)
                        self.screen_shake = 5
                        self.money += cost

    def death_screen(self):

        """values to start"""
        self.plr = None
        self.player_hp = 100
        self.player_pos = (W // 2, H // 2)

        self.player_durability = 1
        self.durability_cost = 5

        self.player_speed = 3
        self.speed_cost = 5

        self.player_body_level = 0
        self.player_cannon_level = 0

        self.player_damage = 1
        self.damage_cost = 5

        self.reload_cooldown = 120
        self.reload_cost = 5

        self.reload = 0
        self.bullet_speed = 9

        self.money = 0
        self.wave = 0

        """meteors"""
        self.meteors.empty()
        self.placing_med = False
        self.placing_big = False

        """music"""
        pygame.mixer.music.fadeout(1)

        """delete enemies"""
        self.enemy_group.empty()
        self.plr_bullets.empty()

        death = True

        """buttons"""
        menu_button = Button(500, 55, 150, 350, YELLOW, ORANGE, YELLOW)
        exit_button = Button(250, 90, 275, 500, YELLOW, ORANGE, YELLOW)

        """effects"""
        clear_effects()

        """death effect"""
        pygame.mixer.Sound.play(death_sound)
        pygame.draw.rect(screen, RED, (0, 0, 800, 800))
        pygame.display.update()
        sleep(2)
        pygame.mixer.music.load('sounds/sad.mp3')
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1)

        while death:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_button.is_over(mouse):
                        self.game_menu()
                    if exit_button.is_over(mouse):
                        quit()

            """background"""
            screen.fill((0, 0, 0))
            screen.blit(background_img, (0, 0))
            add_background_ball()
            draw_background_effects()

            """score message"""
            message_to_screen('DEAD', RED, large_font, 400, 100)
            message_to_screen(f'you survived {self.time} seconds', RED, med_font, 400, 200)
            if self.difficulty == 0:
                message_to_screen(f'on easy difficulty', RED, med_font, 400, 250)
            if self.difficulty == 1:
                message_to_screen(f'on medium difficulty', RED, med_font, 400, 250)
            if self.difficulty == 2:
                message_to_screen(f'on hard difficulty', RED, med_font, 400, 250)

            """drawing buttons"""
            menu_button.draw('Return to menu', med_font, mouse)
            exit_button.draw('EXIT', large_font, mouse)

            """update display"""
            pygame.display.update()
            self.clock.tick(self.FPS)
        self.time = 0

    def add_enemy_to_group(self, group, wave):
        """adds enemies to enemy group"""
        for unit in wave:
            self.enemy_group.add(Enemy(group[int(unit) - 1]['speed'],
                                       group[int(unit) - 1]['hp'],
                                       group[int(unit) - 1]['damage'],
                                       group[int(unit) - 1]['cost'],
                                       group[int(unit) - 1]['image']))

    def spawn_wave(self):
        """spawn waves from difficulty and time"""
        if self.difficulty == 0:
            try:
                self.add_enemy_to_group(self.enemy_types_0, self.waves_0[self.wave])
            except IndexError:
                self.add_enemy_to_group(self.enemy_types_0, '22' * self.wave)
        elif self.difficulty == 1:
            try:
                self.add_enemy_to_group(self.enemy_types_1, self.waves_1[self.wave])
            except IndexError:
                self.add_enemy_to_group(self.enemy_types_1, '3' * self.wave)
        else:
            try:
                self.add_enemy_to_group(self.enemy_types_2, self.waves_2[self.wave])
            except IndexError:
                self.add_enemy_to_group(self.enemy_types_2, '33' * self.wave)
        self.wave += 1

    def game(self):
        """values"""
        self.plr = self.create_player(W // 2, H // 2)

        """music"""
        pygame.mixer.music.fadeout(1)
        pygame.mixer.Sound.play(change_sound)
        sleep(1)
        if self.difficulty == 0:
            pygame.mixer.music.load('sounds/easy_music.mp3')
        elif self.difficulty == 1:
            pygame.mixer.music.load('sounds/medium_music.mp3')
        else:
            pygame.mixer.music.load('sounds/hard_music.mp3')
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1)

        """effects"""
        shake_dist = 0
        clear_effects()

        second = 60
        in_game = True
        while in_game:

            """screen shake"""
            if self.screen_shake > 0:
                r = randint(1, 2)
                if r == 1:
                    shake_dist = -self.screen_shake
                else:
                    shake_dist = self.screen_shake
                self.screen_shake -= 1

            """game menu buttons"""
            durability_button = Button(280, 30, 510 + shake_dist, 655 + shake_dist, YELLOW, ORANGE, YELLOW, 2, 5)
            speed_button = Button(280, 30, 510 + shake_dist, 691 + shake_dist, YELLOW, ORANGE, YELLOW, 2, 5)
            damage_button = Button(280, 30, 510 + shake_dist, 727 + shake_dist, YELLOW, ORANGE, YELLOW, 2, 5)
            reload_button = Button(280, 30, 510 + shake_dist, 764 + shake_dist, YELLOW, ORANGE, YELLOW, 2, 5)

            meteor_med_button = Button(90, 90, 50 + shake_dist, 701 + shake_dist, YELLOW, ORANGE, YELLOW, 2, 5)
            meteor_big_button = Button(90, 90, 155 + shake_dist, 701 + shake_dist, YELLOW, ORANGE, YELLOW, 2, 5)

            turret_button = Button(130, 130, 320 + shake_dist, 660 + shake_dist, YELLOW, ORANGE, YELLOW, 2, 5)

            """mouse"""
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if durability_button.is_over(mouse):
                        self.change_durability()
                    if speed_button.is_over(mouse):
                        self.change_speed()
                    if damage_button.is_over(mouse):
                        self.change_damage()
                    if reload_button.is_over(mouse):
                        self.change_reload()
                    if meteor_med_button.is_over(mouse):
                        self.place_med()
                    if meteor_big_button.is_over(mouse):
                        self.place_big()
                    if turret_button.is_over(mouse):
                        self.place_turret()

            """get inputs from user"""
            click = pygame.mouse.get_pressed(3)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pause()

            """background"""
            screen.blit(background_img, (-self.plr.rect.centerx//10-20, -self.plr.rect.centery//10-20))
            add_background_ball()
            draw_background_effects()

            """bullets logic"""
            if not self.reload:
                if click[0] and mouse[1] < 650:
                    pygame.mixer.Sound.play(bullet_sound)
                    add_shot_effect(self.plr.rect.centerx, self.plr.rect.centery)
                    self.screen_shake = 3

                    new_bullet = Bullet(self.plr.rect.x + 21, self.plr.rect.y + 21, mouse[0], mouse[1],
                                        self.bullet_speed, bullet_img)
                    self.plr_bullets.add(new_bullet)
                    self.reload = self.reload_cooldown
            else:
                self.reload -= 1

            self.plr_bullets.draw(screen)
            self.plr_bullets.update()

            """movement smokes and enemy smokes"""
            add_smokes(keys, self.plr.rect.centerx, self.plr.rect.centery)
            draw_smokes()

            """update player"""
            update_shot_effect(self.plr.rect.centerx, self.plr.rect.centery)
            self.plr.update_player()
            self.plr.draw()
            self.player_pos = (self.plr.rect.x, self.plr.rect.y)

            """enemies"""
            self.enemy_group.draw(screen)
            self.enemy_group.update((self.plr.rect.x, self.plr.rect.y))

            """collision"""
            self.collide_enemies_plr(self.plr)
            self.collide_bullets_enemy(self.plr)

            """death screen"""
            if self.plr.hp <= 0:
                self.death_screen()

            """meteors draw and collision"""
            self.collide_meteors_enemy(self.plr)
            for meteor in self.meteors:
                meteor.draw(screen)
            self.meteors.update()

            """draw turrets bullets"""
            self.turrets_bullets.update()
            self.turrets_bullets.draw(screen)
            self.collide_turrets_bullets_enemy(self.plr)

            """game menu"""
            pygame.draw.rect(screen, ORANGE, (508+shake_dist, 615+shake_dist, 285, 30))  # hp background
            pygame.draw.rect(screen, YELLOW, (510+shake_dist, 617+shake_dist, self.plr.hp * 3 - 19, 26))  # hp gr line

            pygame.draw.rect(screen, ORANGE, (0+shake_dist, 650+shake_dist, 800, 150))  # main menu background
            pygame.draw.rect(screen, DEEP_BLUE, (2+shake_dist, 652+shake_dist, 796, 146))  # main menu foreground

            """game menu buttons"""
            durability_button.draw(f'upgrade durability = {self.durability_cost}',
                                   small_font, mouse)
            speed_button.draw(f'upgrade speed = {self.speed_cost}',
                              small_font, mouse)
            damage_button.draw(f'upgrade damage = {self.damage_cost}',
                               small_font, mouse)
            reload_button.draw(f'upgrade firing rate = {self.reload_cost}',
                               small_font, mouse)

            """meteors"""
            meteor_med_button.draw('', small_font, mouse)
            screen.blit(meteor_med_img, (72+shake_dist, 725+shake_dist))
            message_to_screen(str(self.med_cost), YELLOW, small_font, 70+shake_dist, 715+shake_dist)

            meteor_big_button.draw('', small_font, mouse)
            screen.blit(meteor_big_img, (159+shake_dist, 707+shake_dist))
            message_to_screen(str(self.big_cost), YELLOW, small_font, 180+shake_dist, 715+shake_dist)

            """turret"""
            turret_button.draw('', small_font, mouse)
            screen.blit(turret_full_img, (364+shake_dist, 685+shake_dist))
            message_to_screen(str(self.turret_cost), YELLOW, small_font, 343+shake_dist, 678+shake_dist)

            """turrets logic"""
            for turret in self.turrets:
                shoot = turret.update_draw_shoot(self.enemy_group)
                if shoot:
                    pygame.mixer.Sound.play(bullet_sound)
                    add_turret_shot(turret.rect.centerx, turret.rect.centery)
                    self.turrets_bullets.add(shoot)

            """data on screen"""
            message_to_screen(f'Points: {self.money}', YELLOW, med_font, 150+shake_dist, 680+shake_dist)

            pygame.draw.rect(screen, ORANGE, (300+shake_dist, -15+shake_dist, 200, 110), 5, 15, 0, 0, 15)
            message_to_screen(f'Time: {self.time}', YELLOW, med_font, 400+shake_dist, 30+shake_dist)
            message_to_screen(f'Wave {self.wave}', YELLOW, small_font, 400+shake_dist, 70+shake_dist)

            """medium meteor"""
            if self.placing_med and self.money >= self.med_cost and not self.placing_big and not self.placing_turret:
                screen.blit(meteor_med_green_img, (mouse[0] - 20, mouse[1] - 20))
                if not self.meteors_reload:
                    if mouse[1] < 630:
                        if click[0] and not self.meteors_reload:
                            self.money -= self.med_cost
                            pygame.mixer.Sound.play(place_sound)
                            self.meteors.add(Meteor(mouse[0]-20, mouse[1]-20, meteor_med_img, 10, 60))
                            self.placing_med = False
                            self.meteors_reload = self.meteors_cooldown
                    if click[2]:
                        self.placing_med = False
                        self.meteors_reload = self.meteors_cooldown
                else:
                    self.meteors_reload -= 1
            else:
                self.placing_med = False

            """big meteor"""
            if self.placing_big and self.money >= self.big_cost and not self.placing_med and not self.placing_turret:
                screen.blit(meteor_big_green_img, (mouse[0] - 40, mouse[1] - 40))
                if not self.meteors_reload:
                    if mouse[1] < 610:
                        if click[0] and not self.meteors_reload:
                            self.money -= self.big_cost
                            pygame.mixer.Sound.play(place_sound)
                            self.meteors.add(Meteor(mouse[0]-40, mouse[1]-40, meteor_big_img, 20, 180))
                            self.placing_big = False
                            self.meteors_reload = self.meteors_cooldown
                    if click[2]:
                        self.placing_big = False
                        self.meteors_reload = self.meteors_cooldown
                else:
                    self.meteors_reload -= 1
            else:
                self.placing_big = False

            """turret buy logic"""
            if self.placing_turret and self.money >= self.turret_cost and not self.placing_med and not self.placing_big:
                screen.blit(turret_full_green_img, (mouse[0]-20, mouse[1]-50))
                if not self.meteors_reload:
                    if mouse[1] < 630:
                        if click[0] and not self.meteors_reload:
                            self.money -= self.turret_cost
                            pygame.mixer.Sound.play(place_sound)
                            self.turrets.add(Turret(mouse[0]+1, mouse[1]+5, turret_body_img, turret_cannon_img,
                                                    self.turret_damage, self.turret_reload_cooldown, self.bullet_speed))
                            self.placing_turret = False
                            self.meteors_reload = self.meteors_cooldown
                        if click[2]:
                            self.placing_turret = False
                            self.meteors_reload = self.meteors_cooldown
                else:
                    self.meteors_reload -= 1
            else:
                self.placing_turret = False

            """time and wave spawn part"""
            for wave, time in self.wave_times.items():
                if self.wave < wave:
                    self.wave_cooldown = time
                    break

            if second >= 0:
                second -= 1
            else:
                self.time += 1
                second = 60
                if (self.time + 19) % self.wave_cooldown == 0:
                    self.spawn_wave()

            """update display"""
            pygame.display.update()
            self.clock.tick(self.FPS)

    """game menu (buy) functions"""

    def place_turret(self):
        self.placing_turret = True

    def place_med(self):
        self.placing_med = True

    def place_big(self):
        self.placing_big = True

    def change_difficulty(self, new_dif):
        """changes difficulty from difficulty buttons"""
        self.difficulty = new_dif

    def change_durability(self):
        if self.durability_cost == 5 and self.money >= 5:
            pygame.mixer.Sound.play(change_sound)
            self.money -= 5
            self.player_durability = 0.8
            self.durability_cost = 10
        elif self.durability_cost == 10 and self.money >= 10:
            self.player_body_level = 1
            pygame.mixer.Sound.play(change_sound)
            self.plr = self.create_player(self.player_pos[0]+21, self.player_pos[1]+21)

            self.money -= 10
            self.player_durability = 0.6
            self.durability_cost = 30
        elif self.durability_cost == 30 and self.money >= 30:
            pygame.mixer.Sound.play(change_sound)
            self.money -= 30
            self.player_durability = 0.4
            self.durability_cost = 100
        elif self.durability_cost == 100 and self.money >= 100:
            self.player_body_level = 2
            self.plr = self.create_player(self.player_pos[0]+21, self.player_pos[1]+21)

            pygame.mixer.Sound.play(change_sound)
            self.money -= 100
            self.player_durability = 0.1
            self.durability_cost = 'MAX'

    def change_speed(self):
        if self.speed_cost == 5 and self.money >= 5:
            pygame.mixer.Sound.play(change_sound)
            self.money -= 5
            self.player_speed = 4
            self.speed_cost = 10
            self.plr = self.create_player(self.player_pos[0]+21, self.player_pos[1]+21)
        elif self.speed_cost == 10 and self.money >= 10:
            pygame.mixer.Sound.play(change_sound)
            self.money -= 10
            self.player_speed = 5
            self.speed_cost = 30
            self.plr = self.create_player(self.player_pos[0]+21, self.player_pos[1]+21)
        elif self.speed_cost == 30 and self.money >= 30:
            pygame.mixer.Sound.play(change_sound)
            self.money -= 30
            self.player_speed = 6
            self.speed_cost = 100
            self.plr = self.create_player(self.player_pos[0]+21, self.player_pos[1]+21)
        elif self.speed_cost == 100 and self.money >= 100:
            pygame.mixer.Sound.play(change_sound)
            self.money -= 100
            self.player_speed = 7
            self.plr = self.create_player(self.player_pos[0]+21, self.player_pos[1]+21)
            self.speed_cost = 'MAX'

    def change_damage(self):
        if self.damage_cost == 5 and self.money >= 5:
            pygame.mixer.Sound.play(change_sound)
            self.money -= 5
            self.player_damage = 2
            self.damage_cost = 10
        elif self.damage_cost == 10 and self.money >= 10:
            self.player_cannon_level = 1
            pygame.mixer.Sound.play(change_sound)
            self.plr = self.create_player(self.player_pos[0]+21, self.player_pos[1]+21)

            self.money -= 10
            self.player_damage = 3
            self.damage_cost = 30
        elif self.damage_cost == 30 and self.money >= 30:
            pygame.mixer.Sound.play(change_sound)
            self.money -= 30
            self.player_damage = 5
            self.damage_cost = 100
        elif self.damage_cost == 100 and self.money >= 100:
            self.player_cannon_level = 2
            self.plr = self.create_player(self.player_pos[0]+21, self.player_pos[1]+21)

            pygame.mixer.Sound.play(change_sound)
            self.money -= 100
            self.player_damage = 8
            self.damage_cost = 'MAX'

    def change_reload(self):
        if self.reload_cost == 5 and self.money >= 5:
            pygame.mixer.Sound.play(change_sound)
            self.money -= 5
            self.reload_cooldown = 90
            self.reload_cost = 10
        elif self.reload_cost == 10 and self.money >= 10:
            pygame.mixer.Sound.play(change_sound)
            self.money -= 10
            self.reload_cooldown = 60
            self.reload_cost = 30
        elif self.reload_cost == 30 and self.money >= 30:
            pygame.mixer.Sound.play(change_sound)
            self.money -= 30
            self.reload_cooldown = 30
            self.reload_cost = 100
        elif self.reload_cost == 100 and self.money >= 100:
            pygame.mixer.Sound.play(change_sound)
            self.money -= 100
            self.reload_cooldown = 15
            self.reload_cost = 'MAX'
