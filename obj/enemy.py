import pygame as pg
from config import Config as cf
from .si_constructor import Constructor
import random


class Enemy:
    def __init__(self):
        self.contstruct = Constructor()
        self.direction_right = True
        self.score = 0

    # construct all enemies
    def contsructor(self):
        self.enemies = self.contstruct.space_invader_constructor()

    # draw and move all enemies
    def draw(self, screen, lvl):
        size = "space_high"
        # loop over all evemies
        for type, enemies in self.enemies.items():
            # go throuh all enemies and move and draw them in right direction
            for enemy in enemies:
                size = type
                if self.direction_right:
                    enemy.move_ip(getattr(cf, f"space_invader_speed_{lvl}"), 0)
                elif not self.direction_right:
                    enemy.move_ip(-getattr(cf, f"space_invader_speed_{lvl}"), 0)
                # pg.draw.rect(screen, cf.space_invader_color, enemy)
                screen.blit(getattr(cf, f"{size}_pic"), (enemy.x, enemy.y))

                # If enemy reaches ends change directions and move down
                if enemy.x + cf.si_x >= cf.game_width:
                    self.direction_right = False
                    for type, enemies in self.enemies.items():
                        for enemy in enemies:
                            size = type
                            enemy.move_ip(0, 50)
                            # pg.draw.rect(screen, cf.space_invader_color, enemy)
                            screen.blit(getattr(cf, f"{size}_pic"), (enemy.x, enemy.y))
                elif enemy.x == 0:
                    self.direction_right = True
                    for type, enemies in self.enemies.items():
                        for enemy in enemies:
                            size = type
                            enemy.move_ip(0, 50)
                            # pg.draw.rect(screen, cf.space_invader_color, enemy)
                            screen.blit(getattr(cf, f"{size}_pic"), (enemy.x, enemy.y))
        # if enemies finished reset enemies
        if all(
            isinstance(enemy, list) and not enemy for enemy in self.enemies.values()
        ):
            print("All lists are empty")
            self.enemies = self.contstruct.space_invader_constructor()

    # to control the killing of enemies
    def kill_controller(self, bullet, lvl):
        for type, enemies in self.enemies.items():
            for enemy in enemies:
                if enemy.colliderect(bullet):
                    self.enemies[type].remove(enemy)
                    score_dict = getattr(cf, f"space_invader_scores_{lvl}")
                    self.score += score_dict[type]
                    return True

    # controlls the game over when enemy reaches the buttom
    def game_over_controller(self):
        for type, enemies in self.enemies.items():
            for enemy in enemies:
                if enemy.y == cf.game_height:
                    print("gameover")

    def enemy_shooter(self):
        available_levels = [lvl for lvl in self.enemies if self.enemies[lvl]]
        if not available_levels:
            return None  # No enemies left
        # pick a random level invader then an invader
        level = random.choice(available_levels)
        invader = random.choice(self.enemies[level])
        return invader

    def get_score(self):
        return self.score
