import pygame
from nlc_dino_runner.utils.constants import (
    TITTLE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH)

class Game:
    def __init__(self):
        pygame.init()
        self.playing = False
        pygame.display.set_caption(TITTLE)
        pygame.display.set_caption (ICON)
        self.screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.x_pos_bg

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill((255, 255, 255))
        pygame.display.flip()

    def draw_background(self):
        self.screen.blit(BG, self.x_pos_bg, self. )
