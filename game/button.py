from game.globals import SmallFont, WHITE
import pygame

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


class ButtonText:
    def __init__(self, screen, x, y, text):
        self.screen = screen
        self.text = SmallFont.render(text, 1, WHITE)
        text_width, text_height = SmallFont.size(text)
        self.rect = pygame.Rect(x, y, text_width, text_height)
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
            
        self.screen.blit(self.text, self.rect)

        return action