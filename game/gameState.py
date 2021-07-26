from game.player import Player
from game import enums, globals
from game.character import Character
from screen import menu, intro, stage, end, credits
from game.enemy import Enemy
from game.enums import Action


class GameState:
    def __init__(self):
        self.screens = enums.Screen
        self.currentScreen = self.screens.menu
        self.levels = enums.Level
        self.currentLevel = self.levels.none
        self.score = 0

        scrMenu = menu.Menu(self)
        scrIntro = intro.Intro(self)
        scrStage = stage.Stage(self)
        scrEnd = end.End(self)
        scrCredits = credits.Credits(self)


        self.view = {
            enums.Screen.menu: lambda : scrMenu.draw(),
            enums.Screen.intro: lambda : scrIntro.draw(),
            enums.Screen.stage: lambda : scrStage.draw(),
            enums.Screen.end: lambda : scrEnd.draw(),
            enums.Screen.credits: lambda : scrCredits.draw(),
        }

    def gotoScreen(self, screen):
        self.currentScreen = screen

    def update_score(self, increment):
        self.score = self.score + increment

    def render(self):
        globals.ViewScreen.fill(globals.BLACK)
        return self.view[self.currentScreen]()
