from screen.screen import Screen
from game.button import Button

class Menu(Screen):
    def __init__(self, state):
        super().__init__(state)

    def draw(self):
        Title = self.globals.TitleFont.render("Western Defender", 1, self.globals.WHITE)
        self.globals.ViewScreen.blit(Title, (self.globals.SCREEN.left + 20, 20))

        
        if Button(self.globals.ViewScreen, self.globals.SCREEN.centerx - self.globals.StartImg.get_rect().width//2, 
        self.globals.SCREEN.centery, self.globals.StartImg).draw():
            self.state.gotoScreen(self.state.screens.intro)

        return super().draw()
