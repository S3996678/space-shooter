import pygame as pg
from config import Config as cf
from obj import player, gun, enemy, bullet, enemy_bullet, shelter
import random


class Playing:
    def __init__(self, screen, clock, lvl):
        cf.play_game_music()

        self.playing = True
        self.screen = screen
        self.clock = clock
        self.lvl = lvl
        self.player = player.Player(self.screen)
        self.gun = gun.Gun(self.screen)
        # self.bullet = bullet.Bullet(self.screen)
        self.enemy = enemy.Enemy()
        self.enemy_bullet = enemy_bullet.Enemy_gun(self.screen)
        self.enemy.contsructor()
        self.shelter = shelter.Shelter(self.screen)
        self.shelter.constructor(self.lvl)

        self.click_cooldown = getattr(cf, f"gun_cooldown_{lvl}")
        self.last_click_time = 0
        self.last_enemy_trigger = 0

    def draw(self):
        self.screen.blit(cf.menu_background, (0, 0))

        # run player
        self.player.run()
        self.gun.run()
        self.enemy_bullet.run()

        # draw enemies
        self.enemy.draw(self.screen, self.lvl)

        # kill enemies
        active_bullets = self.gun.get_bullet()
        for bullet in active_bullets:
            if self.enemy.kill_controller(bullet, self.lvl):

                self.gun.remove_bullet(bullet)

        # implement later fully
        if self.enemy.game_over_controller():
            self.playing = False

        active_enemy_bullets = self.enemy_bullet.get_bullet()
        for bullet in active_enemy_bullets:
            if self.player.get_player_pos().colliderect(bullet):
                cf.lost_sound.play()
                self.playing = False

        # shelter
        self.shelter.draw()
        # remove bullet and shelter if contact is made
        for bullet in active_bullets:
            if self.shelter.update_shelter(bullet):
                self.gun.remove_bullet(bullet)
        for bullet in active_enemy_bullets:
            if self.shelter.update_shelter(bullet):
                self.enemy_bullet.remove_bullet(bullet)

        # score handler
        score_text = cf.font.render(
            "score: " + str(self.enemy.get_score()), True, cf.score_count_colour
        )
        self.screen.blit(score_text, cf.score_count_position)

        pg.display.flip()
        self.clock.tick(cf.fps)

    def handle_events(self):
        self.current_time = pg.time.get_ticks()

        if self.current_time - self.last_enemy_trigger >= 1000:
            self.last_enemy_trigger = self.current_time
            if random.randint(1, cf.invader_drop_rate) == 1:
                self.drop_enemy_bullets()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False

            # if there is a left click and the gun has cooled down trigger shot
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.current_time - self.last_click_time >= self.click_cooldown:
                    self.gun.mouse_click(self.player.get_player_pos(), True, True)
                    cf.shoot_sound.play()
                    self.last_click_time = self.current_time

        return True

    def drop_enemy_bullets(self):
        if self.lvl == 1 or self.lvl == 2:
            enemy_bull = self.enemy.enemy_shooter()
            if enemy_bull:
                self.enemy_bullet.trigger(enemy_bull)
        elif self.lvl == 3:
            for i in range(2):
                enemy_bull = self.enemy.enemy_shooter()
                if enemy_bull:
                    self.enemy_bullet.trigger(enemy_bull)
        elif self.lvl == 4:
            for i in range(3):
                enemy_bull = self.enemy.enemy_shooter()
                if enemy_bull:
                    self.enemy_bullet.trigger(enemy_bull)
        elif self.lvl == 5:
            for i in range(4):
                enemy_bull = self.enemy.enemy_shooter()
                if enemy_bull:
                    self.enemy_bullet.trigger(enemy_bull)

    def game_status_change(self):
        if self.playing:
            return None
        else:
            return self.enemy.get_score()
