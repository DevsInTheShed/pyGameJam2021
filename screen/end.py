import pygame 
from screen.screen import Screen

class End(Screen):
    def __init__(self, state):
        super().__init__(state)

    def draw(self):
        Title = self.globals.TitleFont.render('Game Over', 1, self.globals.WHITE)
        title_width, title_height = self.globals.TitleFont.size("Game Over")

        if self.state.win == True:
            ResultText = 'Congratulations'
        else:
            ResultText = 'Bad Luck'
        
        Result = self.globals.MediumFont.render(ResultText, 1, self.globals.WHITE)
        result_width, result_height = self.globals.MediumFont.size(ResultText)


        self.globals.ViewScreen.blit(Title, (self.globals.SCREEN.centerx - title_width//2, 100))
        self.globals.ViewScreen.blit(Result, (self.globals.SCREEN.centerx - result_width//2, 150))

        return super().draw()