import pygame 
from game.screen.screen import Screen

class Menu(Screen):
    def __init__(self, globals, state):
        super().__init__(globals, state)

    def draw(self):
        Title = self.globals.TitleFont.render("Western Harry", 1, self.globals.WHITE)
        self.globals.ViewScreen.blit(Title, (self.globals.SCREEN.left + 20, 20))

        self.state.gotoScreen(self.state.screens.stage)

        return super().draw()