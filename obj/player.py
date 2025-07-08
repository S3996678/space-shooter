import pygame as pg
from config import Config as cf
from .gun import Gun


class Player:
    def __init__(self, screen):
        self.player_rect = cf.player_rect
        self.player_color = cf.player_color
        self.player_speed = cf.player_speed
        self.player_image = cf.player_image

        self.gun = Gun(screen)

        self.screen = screen

    def movement(self):
        key = pg.key.get_pressed()
        if key[pg.K_a] == True:
            self.player_rect.x -= self.player_speed
            if self.player_rect.x <= 0:
                self.player_rect.x = 0
        elif key[pg.K_d] == True:
            self.player_rect.x += self.player_speed
            if self.player_rect.right > cf.game_width:
                self.player_rect.right = cf.game_width

    def draw(self, screen):
        pg.draw.rect(screen, self.player_color, self.player_rect)
        screen.blit(self.player_image, (self.player_rect.x, self.player_rect.y))

    def get_player_pos(self):
        return self.player_rect

    def run(self):
        self.movement()
        self.draw(self.screen)
