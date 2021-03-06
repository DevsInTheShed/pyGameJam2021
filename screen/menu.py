from screen.screen import Screen
from game.button import Button, ButtonText

class Menu(Screen):
    def __init__(self, state):
        super().__init__(state)

    def draw(self):
        Title = self.globals.TitleFont.render(self.globals.GameTitle, 1, self.globals.WHITE)
        self.globals.ViewScreen.blit(Title, (self.globals.SCREEN.left + 20, 20))

        if ButtonText(self.globals.ViewScreen, self.globals.SCREEN.right - 100, self.globals.SCREEN.bottom - 50, "Credits").draw():
            self.state.gotoScreen(self.state.screens.credits)
            pass
        
        if Button(self.globals.ViewScreen, self.globals.SCREEN.centerx - self.globals.StartImg.get_rect().width//2, \
            self.globals.SCREEN.centery, self.globals.StartImg).draw():
            self.state.gotoScreen(self.state.screens.intro)

        


        return super().draw()
