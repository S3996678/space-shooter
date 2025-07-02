import pygame as pg
from config import Config as cf
from enemylayouts import lvl1


class Constructor:
    def __init__(self):
        self.pos_highVal = lvl1.construct("high")
        self.pos_medVal = lvl1.construct("medium")
        self.pos_lowVal = lvl1.construct("low")

    def space_invader_constructor(self):
        space_invader = {}
        space_invader["space_low"] = []
        space_invader["space_med"] = []
        space_invader["space_high"] = []
        for p in self.pos_highVal:
            space_invader["space_high"].append(pg.Rect(p[0], p[1], cf.si_x, cf.si_y))
        for p in self.pos_medVal:
            space_invader["space_med"].append(pg.Rect(p[0], p[1], cf.si_x, cf.si_y))
        for p in self.pos_lowVal:
            space_invader["space_low"].append(pg.Rect(p[0], p[1], cf.si_x, cf.si_y))
        return space_invader
