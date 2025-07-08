import pygame as pg
from config import Config as cf
from obj.menu_obj import level_button


class Menu:
    def __init__(self, screen, clock):
        cf.play_menu_music()

        self.screen = screen
        self.clock = clock
        self.button = level_button.Button(self.screen)
        self.game_level = None
        self.lvl1_button = pg.Rect(cf.game_width / 2 - 100, 400, 200, 60)
        self.lvl2_button = pg.Rect(cf.game_width / 2 - 100, 500, 200, 60)
        self.lvl3_button = pg.Rect(cf.game_width / 2 - 100, 600, 200, 60)
        self.lvl4_button = pg.Rect(cf.game_width / 2 - 100, 700, 200, 60)
        self.lvl5_button = pg.Rect(cf.game_width / 2 - 100, 800, 200, 60)

    def draw(self):
        self.screen.blit(cf.menu_background, (0, 0))

        # inside menu loop
        self.button.draw(self.lvl1_button, 1)
        self.button.draw(self.lvl2_button, 2)
        self.button.draw(self.lvl3_button, 3)
        self.button.draw(self.lvl4_button, 4)
        self.button.draw(self.lvl5_button, 5)
        self.screen.blit(cf.game_title, (cf.game_width / 2 - 350, 0))
        pg.display.flip()
        self.clock.tick(cf.fps)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.lvl1_button.collidepoint(event.pos):
                    self.game_level = 1
                if self.lvl2_button.collidepoint(event.pos):
                    self.game_level = 2
                if self.lvl3_button.collidepoint(event.pos):
                    self.game_level = 3
                if self.lvl4_button.collidepoint(event.pos):
                    self.game_level = 4
                if self.lvl5_button.collidepoint(event.pos):
                    self.game_level = 5

        return True

    def game_status_change(self):
        if not self.game_level:
            None
        elif self.game_level:
            return self.game_level
