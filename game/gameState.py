from game import enums
from game.character import Character
from game.screen.stage import Stage
from game.screen.menu import Menu

class GameState:
    def __init__(self, globals):
        self.screens = enums.Screen
        self.currentScreen = self.screens.stage

        # menu screen
        scrMenu = Menu(globals)

        player = Character('player', 200, 200, 3, 5, globals.GRAVITY)
        player.actions = enums.Action
        scrStage = Stage(globals, player)

        self.view = {
            enums.Screen.menu: lambda : scrMenu.draw(),
            enums.Screen.stage: lambda : scrStage.draw()
        }

    def gotoScreen(self, screen):
        self.currentScreen = screen

    def render(self):
        return self.view[self.currentScreen]()
