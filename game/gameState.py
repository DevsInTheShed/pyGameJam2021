from game import enums
from game.character import Character
from screen import menu, intro, stage, end, credits
from game.enemy import Enemy
from game.enums import Action


class GameState:
    def __init__(self, globals):
        self.screens = enums.Screen
        self.currentScreen = self.screens.menu

        player = Character('player', 200, 200, 3, 5, globals.GRAVITY)
        player.actions = enums.Action
        enemy = Enemy('alien1', 400, 200, 3, 5, globals.GRAVITY)

        scrMenu = menu.Menu(self)
        scrIntro = intro.Intro(self)
        scrStage = stage.Stage(self, player, enemy)
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

    def render(self):
        return self.view[self.currentScreen]()