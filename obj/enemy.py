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

    # to control the killing of enemies
    def kill_controller(self, bullet):
        for enemy in self.enemies:
            if enemy.colliderect(bullet):
                self.enemies.remove(enemy)
                return True

    # controlls the game over when enemy reaches the buttom
    def game_over_controller(self):
        for enemy in self.enemies:
            if enemy.y == cf.game_height:
                print("gameover")

    def run(self): ...
