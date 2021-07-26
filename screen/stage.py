import pygame 
from screen.screen import Screen
from level.level_1 import *

class Stage(Screen):
    def __init__(self, state, player1):
        super().__init__(state)
        self.player1 = player1
        self.playerState = {
            "player1": {"moveLeft": False, "moveRight": False}
        }
        self.shoot = False
        self.lvl1 = Level_1()

    def draw(self):
        self.lvl1.draw()

        self.player1.update_animation()
        self.player1.draw(self.globals.ViewScreen)


        if self.player1.alive:
            if self.shoot:
                self.player1.shoot()
            if self.player1.in_air:
                self.player1.update_action(self.player1.actions.jump)
            elif self.playerState["player1"]["moveLeft"] or self.playerState["player1"]["moveRight"]:
                self.player1.update_action(self.player1.actions.run)
            else:
                self.player1.update_action(self.player1.actions.idle)
            self.player1.move(self.playerState["player1"]["moveLeft"], self.playerState["player1"]["moveRight"])

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_LEFT:
                    self.playerState["player1"]["moveLeft"] = True
                if event.key == pygame.K_RIGHT:
                    self.playerState["player1"]["moveRight"] = True
                if event.key == pygame.K_UP and self.player1.alive:
                    self.player1.jump = True
                if event.key == pygame.K_SPACE:
                    self.shoot = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.playerState["player1"]["moveLeft"] = False
                if event.key == pygame.K_RIGHT:
                    self.playerState["player1"]["moveRight"] = False
                if event.key == pygame.K_UP and self.player1.alive:
                    self.player1.jump = False
                if event.key == pygame.K_SPACE:
                    self.shoot = False
            
            if event.type == pygame.QUIT:
                return False
        
        return super().draw()

