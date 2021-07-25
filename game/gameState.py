from game import enums
from game.character import Character
from game.screen import menu, intro, stage, credits, end
from game.enemy import Enemy
from game.enums import Action


class GameState:
    def __init__(self, globals):
        self.screens = enums.Screen
        self.currentScreen = self.screens.menu

        player = Character('player', 200, 200, 3, 5, globals.GRAVITY)
        player.actions = enums.Action
        enemy = Enemy('alien1', 400, 200, 3, 5, globals.GRAVITY)

        scrMenu = menu.Menu(globals, self)
        scrIntro = intro.Intro(globals, self)
        scrStage = stage.Stage(globals, self, player, enemy)
        scrEnd = end.End(globals, self)
        scrCredits = credits.Credits(globals, self)


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
