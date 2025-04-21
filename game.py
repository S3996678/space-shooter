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

    def handle_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def run(self):

        while self.running:
            self.handle_event()
            self.game_state.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
