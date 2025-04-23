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

    def draw(self):
        self.screen.fill(cf.background)

        # run player
        self.player.run()
        self.gun.run(self.player.get_player_pos())

        self.enemy.draw(self.screen)
        self.enemy.kill_controller(self.gun.get_bullet())
        # implement later fully
        self.enemy.game_over_controller()

        pg.display.flip()
        self.clock.tick(cf.fps)
