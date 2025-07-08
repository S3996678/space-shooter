import pygame as pg
from config import Config as cf


class Game_over:
    def __init__(self, screen, clock, score):
        self.screen = screen
        self.clock = clock
        self.score_text = cf.game_over_font.render(
            "SCORE: " + str(score), True, (255, 255, 255)
        )
        cf.play_game_over_music()
        self.main_menu_button = pg.Rect(0, 0, 300, 70)
        self.main_menu_button.center = (cf.game_width / 2, 1000)
        self.main_text = cf.game_over_menu_font.render("MENU", True, (255, 255, 255))
        self.menu_reset = False

    def draw(self):
        self.screen.blit(cf.menu_background, (0, 0))
        # title
        self.screen.blit(cf.game_over_title, (cf.game_width / 2 - 350, 0))
        # score text
        # Draw semi-transparent box behind score
        score_box_width = self.score_text.get_width() + 40
        score_box_height = self.score_text.get_height() + 20
        score_box = pg.Surface((score_box_width, score_box_height), pg.SRCALPHA)
        score_box.fill((0, 0, 0, 150))  # RGBA – 150 alpha for transparency

        box_rect = score_box.get_rect(center=(cf.game_width / 2, cf.game_height / 2))
        self.screen.blit(score_box, box_rect)

        text_rect = self.score_text.get_rect(
            center=(cf.game_width / 2, cf.game_height / 2)
        )
        self.screen.blit(self.score_text, text_rect)

        # menu button
        # hover color
        mouse_pos = pg.mouse.get_pos()
        button_color = (
            (0, 130, 255)
            if self.main_menu_button.collidepoint(mouse_pos)
            else (0, 100, 200)
        )

        pg.draw.rect(self.screen, button_color, self.main_menu_button)
        self.screen.blit(
            self.main_text, self.main_text.get_rect(center=self.main_menu_button.center)
        )
        pg.display.flip()
        self.clock.tick(cf.fps)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.main_menu_button.collidepoint(event.pos):
                    self.menu_reset = True
        return True

    def game_status_change(self):
        if not self.menu_reset:
            return None
        else:
            return True
