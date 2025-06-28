import pygame as pg
from config import Config as cf
from obj import player
from obj import gun
from obj import enemy


class Playing:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.player = player.Player(self.screen)
        self.gun = gun.Gun(self.screen)
        self.enemy = enemy.Enemy()
        self.enemy.contsructor()

        self.click_cooldown = cf.gun_cooldown
        self.last_click_time = 0

    def draw(self):
        self.screen.fill(cf.background)

        # run player
        self.player.run()
        self.gun.run()

        # draw enemies
        self.enemy.draw(self.screen)

        # kill enemies
        active_bullets = self.gun.get_bullet()
        for bullet in active_bullets:
            if self.enemy.kill_controller(bullet):
                self.gun.remove_bullet(bullet)

        # implement later fully
        self.enemy.game_over_controller()

        pg.display.flip()
        self.clock.tick(cf.fps)

    def handle_events(self):
        self.current_time = pg.time.get_ticks()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False

            # if there is a left click and the gun has cooled down trigger shot
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.current_time - self.last_click_time >= self.click_cooldown:
                    self.gun.mouse_click(self.player.get_player_pos(), True, True)
                    self.last_click_time = self.current_time
        return True
