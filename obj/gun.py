import pygame as pg
from config import Config as cf


class Gun:
    def __init__(self, screen):
        self.screen = screen

        self.bullet = cf.bullet_1_pic
        self.bulrect = cf.bullet_1

        self.isbul = False

    def shoot(self):
        if self.isbul:
            self.bulrect.move_ip(0, -2)
            self.screen.blit(self.bullet, self.bulrect)

    def trigger(self, player_pos):
        pg.Rect.update(
            self.bulrect, player_pos.x + cf.bulx / 2, player_pos.y, cf.bulx, cf.buly
        )
        self.isbul = True

    def run(self, player_pos):
        mouse = pg.mouse.get_pressed()
        if mouse[0] == True:
            self.trigger(player_pos)
        self.shoot()
