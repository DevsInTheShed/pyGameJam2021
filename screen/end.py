from game.button import Button
from screen.screen import Screen

class End(Screen):
    def __init__(self, state):
        super().__init__(state)

    def draw(self):
        Title = self.globals.TitleFont.render('Game Over', 1, self.globals.WHITE)
        title_width, title_height = self.globals.TitleFont.size("Game Over")

        if self.state.win == True:
            ResultText = 'Congratulations'
            if Button(self.globals.ViewScreen, self.globals.SCREEN.centerx - self.globals.VictoryImg.get_rect().width//2, \
            self.globals.SCREEN.centery, self.globals.VictoryImg).draw():
                self.state.init = True
                self.state.currentLevel = self.state.levels.none
                self.state.gotoScreen(self.state.screens.intro)
        else:
            ResultText = 'Bad Luck'
            if Button(self.globals.ViewScreen, self.globals.SCREEN.centerx - self.globals.StartImg.get_rect().width//2, \
            self.globals.SCREEN.centery, self.globals.StartImg).draw():
                self.state.init = True
                self.state.currentLevel = self.state.levels.none
                self.state.gotoScreen(self.state.screens.intro)
            
        Result = self.globals.MediumFont.render(ResultText, 1, self.globals.WHITE)
        result_width, result_height = self.globals.MediumFont.size(ResultText)

        self.globals.ViewScreen.blit(Title, (self.globals.SCREEN.centerx - title_width//2, 100))
        self.globals.ViewScreen.blit(Result, (self.globals.SCREEN.centerx - result_width//2, 150))

        return super().draw()