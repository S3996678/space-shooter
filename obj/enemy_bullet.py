import pygame as pg
from config import Config as cf


class Enemy_gun:
    def __init__(self, screen):
        self.screen = screen

        self.bullet = cf.space_bullet_pic
        self.bulrect = []

        self.isbul = False

    def shoot(self):
        if self.isbul:
            for bullet in self.bulrect:
                bullet.move_ip(0, cf.space_bullet_speed)
                self.screen.blit(self.bullet, bullet)

    def trigger(self, enemypos):
        self.bulrect.append(cf.space_bullet.copy())
        pg.Rect.update(
            self.bulrect[-1], enemypos.x + cf.bulx / 2, enemypos.y, cf.bulx, cf.buly
        )
        self.isbul = True

    def get_bullet(self):
        return self.bulrect

    def remove_bullet(self, used=None):
        for bullet in self.bulrect:
            if bullet.y >= cf.game_height:
                self.bulrect.remove(bullet)
        if used:
            self.bulrect.remove(used)

    def run(self):
        self.shoot()
        self.remove_bullet()
