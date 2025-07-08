import pygame as pg
from config import Config as cf
from states import playing, menu, game_over


class Game:
    # initialise game
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((cf.game_width, cf.game_height))
        self.clock = pg.time.Clock()
        self.running = True
        # self.game_state = playing.Playing(self.screen, self.clock)
        self.game_state = menu.Menu(self.screen, self.clock)

    def run(self):

        # loop game until end
        while self.running:
            self.running = self.game_state.handle_events()
            if self.game_state.game_status_change() is not None:
                if isinstance(self.game_state, menu.Menu):
                    pg.mixer.music.fadeout(1000)  # fades out over 1 second
                    lvl = self.game_state.game_status_change()
                    self.game_state = playing.Playing(self.screen, self.clock, lvl)
                elif isinstance(self.game_state, playing.Playing):
                    score = self.game_state.game_status_change()
                    self.game_state = game_over.Game_over(
                        self.screen, self.clock, score
                    )
                elif isinstance(self.game_state, game_over.Game_over):
                    self.game_state = menu.Menu(self.screen, self.clock)
            self.game_state.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
