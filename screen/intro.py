import pygame 
from screen.screen import Screen
from game.button import Button

class Intro(Screen):
    def __init__(self, state):
        super().__init__(state)
        self.last = pygame.time.get_ticks()
        self.wait = 3000

    def draw(self):
        now = pygame.time.get_ticks()

        if self.state.currentLevel == 0:
            if Button(self.globals.ViewScreen, self.globals.SCREEN.centerx - (self.globals.Level1Img.get_rect().width+20), 
            self.globals.SCREEN.centery - (self.globals.Level1Img.get_rect().height+20), self.globals.Level1Img).draw():
                self.state.currentLevel = 1
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
            Title = self.globals.TitleFont.render("Level 1 intro", 1, self.globals.WHITE)
            text_width, text_height = self.globals.TitleFont.size("Level 1 intro")
            self.globals.ViewScreen.blit(Title, (self.globals.SCREEN.centerx - text_width//2, self.globals.SCREEN.centery - text_height//2))

            if now - self.last >= self.wait:
                self.state.gotoScreen(self.state.screens.stage)


        return super().draw()