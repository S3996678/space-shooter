import pygame as pg
from config import Config as cf


class Button:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, button_rect, lvl):
        mouse_pos = pg.mouse.get_pos()
        button_color = (
            (0, 130, 255) if button_rect.collidepoint(mouse_pos) else (0, 100, 200)
        )
        pg.draw.rect(self.screen, button_color, button_rect)
        text = cf.level_font.render(str(lvl), True, (255, 255, 255))
        self.screen.blit(text, text.get_rect(center=button_rect.center))
