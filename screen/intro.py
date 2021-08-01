import pygame, os
from screen.screen import Screen
from game.button import Button
from game.globals import CutScene1_img, CutScene2_img, CutScene3_img

class Intro(Screen):
    def __init__(self, state):
        super().__init__(state)
        self.last = pygame.time.get_ticks()
        self.wait = 3000


    def draw(self):
        now = pygame.time.get_ticks()

        if self.state.currentLevel == self.state.levels.none:
            if Button(self.globals.ViewScreen, self.globals.SCREEN.centerx - (self.globals.Level1Img.get_rect().width+20), 
            self.globals.SCREEN.centery - (self.globals.Level1Img.get_rect().height+20), self.globals.Level1Img).draw():
                self.state.currentLevel = self.state.levels.one
                now = pygame.time.get_ticks()
                self.last = now

            if Button(self.globals.ViewScreen, self.globals.SCREEN.centerx + 20, 
            self.globals.SCREEN.centery - (self.globals.Level2Img.get_rect().height+20), self.globals.Level2Img).draw():
                pass

            if Button(self.globals.ViewScreen, self.globals.SCREEN.centerx - (self.globals.Level3Img.get_rect().width+20), 
            self.globals.SCREEN.centery + 20, self.globals.Level3Img).draw():
                pass

            if Button(self.globals.ViewScreen, self.globals.SCREEN.centerx + 20, 
            self.globals.SCREEN.centery + 20, self.globals.Level4Img).draw():
                pass

        else:
            # set up level intro
            self.globals.ViewScreen.blit(CutScene1_img, (self.globals.SCREEN.centerx / 2, self.globals.SCREEN.centery / 2))
            self.wait
            self.globals.ViewScreen.blit(CutScene2_img, (self.globals.SCREEN.centerx / 2, self.globals.SCREEN.centery / 2))
            self.wait
            self.globals.ViewScreen.blit(CutScene3_img, (self.globals.SCREEN.centerx / 2, self.globals.SCREEN.centery / 2))
            self.wait

            if now - self.last >= self.wait:
                self.state.gotoScreen(self.state.screens.stage)


        return super().draw()