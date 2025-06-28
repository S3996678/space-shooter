import pygame as pg
from config import Config as cf
from states import playing


class Game:
    # initialise game
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((cf.game_width, cf.game_height))
        self.clock = pg.time.Clock()
        self.running = True
        self.game_state = playing.Playing(self.screen, self.clock)

    def run(self):

        # loop game until end
        while self.running:
            if not self.game_state.handle_events():
                self.running = False
            self.game_state.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
