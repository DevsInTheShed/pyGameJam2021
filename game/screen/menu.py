import pygame 
from game.screen.screen import Screen

class Menu(Screen):
    def __init__(self, globals, state):
        super().__init__(globals, state)

    def draw(self):
        Title = self.globals.TitleFont.render("Western Harry", 1, self.globals.WHITE)
        self.globals.ViewScreen.blit(Title, (self.globals.SCREEN.left + 20, 20))

        
        if Button(self.globals.ViewScreen, self.globals.SCREEN.centerx - self.globals.StartImg.get_rect().width//2, 
        self.globals.SCREEN.centery, self.globals.StartImg).draw():
            self.state.gotoScreen(self.state.screens.stage)

        return super().draw()


class Button:
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
    
    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
            
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
        self.screen.blit(self.image, self.rect)

        return action