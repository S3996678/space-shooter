import pygame as pg
from config import Config as cf


class Gun:
    def __init__(self, screen):
        self.screen = screen

        self.bullet = cf.bullet_1_pic
        self.bulrect = []

        self.isbul = False

    # shoot function to move the bullet once it's been shot
    def shoot(self):
        if self.isbul:
            for bullet in self.bulrect:
                bullet.move_ip(0, -2)
                self.screen.blit(self.bullet, bullet)

    # updates bullets
    def trigger(self, player_pos):
        # update list with new bullet
        pg.Rect.update(
            self.bulrect[-1], player_pos.x + cf.bulx / 2, player_pos.y, cf.bulx, cf.buly
        )
        self.isbul = True

    # get the bullet function
    def get_bullet(self):
        return self.bulrect

    # remove bullet
    def remove_bullet(self, used=None):
        for bullet in self.bulrect:
            if bullet.y == 0:
                self.bulrect.remove(bullet)
        if used:
            self.bulrect.remove(used)

    # controll mouse clicks to shoot
    def mouse_click(self, player_pos, cooldown=False, mouse=False):
        if mouse and cooldown:
            self.bulrect.append(cf.bullet_1.copy())
            self.trigger(player_pos)

    # every time the mouse is clicked triggers a bullet then shoots
    def run(self):
        self.shoot()
        self.remove_bullet()
