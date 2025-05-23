import pygame as pg
from enemylayouts import lvl1


class Config:
    game_width = 1280
    game_height = 1280
    background = "black"
    fps = 60

    # player attributes
    ply_x = 100
    ply_y = 100
    player_rect = pg.Rect((game_width / 2, 3 * (game_height) / 4, ply_x, ply_y))
    player_color = (0, 0, 0)
    player_speed = 7
    player_image = pg.image.load("assets/images/spaceship.png")
    player_image = pg.transform.scale(player_image, (100, 100))
    pr = player_image.get_rect()

    # gun attributes
    bulx = 50
    buly = 50
    bullet_1_pic = pg.image.load("assets/images/bullet1.png")
    bullet_1_pic = pg.transform.scale(bullet_1_pic, (bulx, buly))
    bullet_1 = bullet_1_pic.get_rect()

    # space invader
    si_x = 75
    si_y = 75
    space_invader_speed = 1
    space_invader_color = (0, 0, 0)
    space_invader_pic = pg.image.load("assets/images/space_invader.png")
    space_invader_pic = pg.transform.scale(space_invader_pic, (si_x, si_y))

    # space invader's posistions
    pos = lvl1.construct()
    pos_level_1 = pos
