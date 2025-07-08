import pygame as pg
from enemylayouts import lvl1


class Config:
    game_width = 1800
    game_height = 1280
    background = "black"
    fps = 60
    pg.mixer.init()

    # player attributes
    ply_x = 63
    ply_y = 100
    player_rect = pg.Rect((game_width / 2, 8 * (game_height) / 9, ply_x, ply_y))
    player_color = (0, 0, 0)
    player_speed = 7
    player_image = pg.image.load("assets/images/spaceship.png")
    player_image = pg.transform.scale(player_image, (63, 100))
    pr = player_image.get_rect(center=(game_width / 2, 8 * game_height / 9))

    # gun attributes
    bulx = 25
    buly = 25
    bullet_1_pic = pg.image.load("assets/images/bullet1.png")
    bullet_1_pic = pg.transform.scale(bullet_1_pic, (bulx, buly))
    bullet_1 = bullet_1_pic.get_rect()
    bullet_speed = 5
    # bullet attributes
    pg.font.init()
    bullet_starting_count = 10
    font = pg.font.SysFont(None, 48)  # default font, size 48

    # space invader
    si_x = 75
    si_y = 75
    space_invader_color = (0, 0, 0)
    space_med_pic = pg.image.load("assets/images/space_invader.png")
    space_med_pic = pg.transform.scale(space_med_pic, (si_x, si_y))

    space_low_pic = pg.image.load("assets/images/space_low.png")
    space_low_pic = pg.transform.scale(space_low_pic, (si_x, si_y))

    space_high_pic = pg.image.load("assets/images/space_high.png")
    space_high_pic = pg.transform.scale(space_high_pic, (si_x, si_y))

    invader_drop_rate = 1

    space_bullet_pic = pg.image.load("assets/images/enemy_bullet.png")
    space_bullet_pic = pg.transform.scale(space_bullet_pic, (25, 25))
    space_bullet = space_bullet_pic.get_rect()
    space_bullet_speed = 5

    # score
    score_count_colour = (255, 255, 255)
    score_count_position = (100, game_height - 100)  # score count position

    # shelter
    shelter_xy = 10
    shelter_bits_pic = pg.image.load("assets/images/shelter_pix.png")
    shelter_bits_pic = pg.transform.scale(shelter_bits_pic, (shelter_xy, shelter_xy))

    # level attributes
    # lvl 1:
    space_invader_scores_1 = {"space_low": 10, "space_med": 20, "space_high": 40}
    gun_cooldown_1 = 500  # cooldown
    space_invader_speed_1 = 1

    # lvl 2:
    space_invader_scores_2 = {"space_low": 20, "space_med": 40, "space_high": 80}
    gun_cooldown_2 = 850  # cooldown
    space_invader_speed_2 = 1

    # lvl 3:
    space_invader_scores_3 = {"space_low": 40, "space_med": 60, "space_high": 120}
    gun_cooldown_3 = 850  # cooldown
    space_invader_speed_3 = 2

    # lvl 4:
    space_invader_scores_4 = {"space_low": 60, "space_med": 100, "space_high": 160}
    gun_cooldown_4 = 850  # cooldown
    space_invader_speed_4 = 2

    # lvl 5:
    space_invader_scores_5 = {"space_low": 100, "space_med": 140, "space_high": 200}
    gun_cooldown_5 = 950  # cooldown
    space_invader_speed_5 = 2

    # menu
    menu_background = pg.image.load("assets/images/menu_background.png")
    menu_background = pg.transform.scale(menu_background, (game_width, game_height))

    level_font = pg.font.SysFont(None, 48)

    game_title = pg.image.load("assets/images/title.png")
    game_title = pg.transform.scale(game_title, (700, 400))

    # game over
    game_over_font = pg.font.SysFont(None, 72)
    game_over_menu_font = pg.font.SysFont(None, 72)
    game_over_title = pg.image.load("assets/images/game_over_text.png")
    game_over_title = pg.transform.scale(game_over_title, (700, 400))

    # sounds

    # shooting sound
    shoot_sound = pg.mixer.Sound("assets/sounds/shoot.wav")
    lost_sound = pg.mixer.Sound("assets/sounds/lost_sound.wav")
    lost_sound.set_volume(0.2)

    # play the menu music
    def play_menu_music():
        pg.mixer.music.load("assets/sounds/menu_music.mp3")
        pg.mixer.music.play(-1)

    def play_game_music():
        pg.mixer.music.load("assets/sounds/playing_music.ogg")
        pg.mixer.music.set_volume(0.3)
        pg.mixer.music.play(-1)

    def play_game_over_music():
        pg.mixer.music.load("assets/sounds/game_over_music.mp3")
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(0.3)
