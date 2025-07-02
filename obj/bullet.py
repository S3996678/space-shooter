import pygame as pg
from config import Config as cf


class Bullet:
    def __init__(self, screen):
        self.screen = screen
        self.font = cf.font
        self.bullet_count = cf.bullet_starting_count

    # display bullets
    def dis_bullets(self):
        self.text = self.font.render(
            f"{self.bullet_count}", True, cf.bullet_count_colour
        )
        self.screen.blit(self.text, cf.bullet_count_position)

    # update bullet count minus 1 each bullet used
    def update_bullet_count(self, used=False):
        if used:
            self.bullet_count -= 1

    def check_bullet_available(self):
        if self.bullet_count <= 0:
            return False
        else:
            return True
