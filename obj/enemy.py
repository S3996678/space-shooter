import pygame as pg
from config import Config as cf
from .si_constructor import Constructor


class Enemy:
    def __init__(self):
        self.contstruct = Constructor()

    # construct all enemies
    def contsructor(self):
        self.enemies = self.contstruct.space_invader_constructor()

    # draw and move all enemies
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.move_ip(0, cf.space_invader_speed)
            pg.draw.rect(screen, cf.space_invader_color, enemy)
            screen.blit(cf.space_invader_pic, (enemy.x, enemy.y))

    def run(self): ...
