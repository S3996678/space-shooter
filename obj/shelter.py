import pygame as pg
from config import Config as cf
import pprint


class Shelter:
    def __init__(self, screen):
        self.screen = screen
        self.shelter_pic = cf.shelter_bits_pic
        self.shelter_pos = []
        self.shelter = []

    # construct a shelter with the right pos
    def construct(self, pos=300):
        shelter_width = 20
        shelter_height = 10
        self.shelter_pos = []

        base_x = pos  # move shelter horizontally
        base_y = cf.game_height * 4 / 5  # move shelter vertically

        for x in range(shelter_width):  # top row
            self.shelter_pos.append([base_x + x * cf.shelter_xy, base_y])

        for y in range(1, shelter_height):  # left side
            self.shelter_pos.append([base_x, base_y + y * cf.shelter_xy])

        for y in range(1, shelter_height):  # right side
            self.shelter_pos.append(
                [
                    base_x + (shelter_width - 1) * cf.shelter_xy,
                    base_y + y * cf.shelter_xy,
                ]
            )
        # create a rect of all pix positions
        for p in self.shelter_pos:
            self.shelter.append(pg.Rect(p[0], p[1], cf.shelter_xy, cf.shelter_xy))
        for pix in self.shelter:
            self.screen.blit(self.shelter_pic, pix)

    # draw the shelter
    def draw(self):
        for pix in self.shelter:
            self.screen.blit(self.shelter_pic, pix)

    # update shelter if bullets hit
    def update_shelter(self, bullet):
        for pix in self.shelter:
            if pix.colliderect(bullet):
                print("HIT", pix, bullet, len(self.shelter))
                self.shelter.remove(pix)
                return True
        return False

    # create shelters at positions depending on level
    def constructor(self, level):
        if level == 1:
            self.construct(cf.game_height / 3)
            self.construct(cf.game_height * 2 / 3)
            self.construct(cf.game_height)
        if level == 2:
            self.construct(cf.game_height / 3)
            self.construct(cf.game_height * 2 / 3)
        if level == 3:
            self.construct(cf.game_height * 2 / 3)
        if level >= 4:
            return None
