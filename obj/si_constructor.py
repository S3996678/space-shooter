import pygame as pg
from config import Config as cf


class Constructor:
    def __init__(self):
        pass

    def space_invader_constructor(self):
        pos = cf.pos_level_1
        space_invader = []
        for p in pos:
            space_invader.append(pg.Rect(p[0], p[1], cf.si_x, cf.si_y))
        return space_invader
