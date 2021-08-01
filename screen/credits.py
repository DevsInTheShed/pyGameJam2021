import pygame 
from screen.screen import Screen

class Credits(Screen):
    def __init__(self, state):
        super().__init__(state)
        

    def draw(self):
        Title = self.globals.TitleFont.render("Credits", 1, self.globals.WHITE)
        text_width, text_height = self.globals.TitleFont.size("Credits")
        self.globals.ViewScreen.blit(Title, (self.globals.SCREEN.centerx - text_width//2, 20))

        Design = self.globals.TitleFont.render("Game Design and Programming", 1, self.globals.WHITE)
        text_width, text_height = self.globals.TitleFont.size("Game Design and Programming")
        self.globals.ViewScreen.blit(Design, (self.globals.SCREEN.centerx - text_width//2, 100))

        DesignNames = self.globals.MediumFont.render("Matt Coles, Paul Kukiel, Aaron Sempf", 1, self.globals.WHITE)
        text_width, text_height = self.globals.MediumFont.size("Matt Coles, Paul Kukiel, Aaron Sempf")
        self.globals.ViewScreen.blit(DesignNames, (self.globals.SCREEN.centerx - text_width//2, 150))

        Art = self.globals.TitleFont.render("Game Art", 1, self.globals.WHITE)
        text_width, text_height = self.globals.TitleFont.size("Game Art")
        self.globals.ViewScreen.blit(Art, (self.globals.SCREEN.centerx - text_width//2, 300))

        ArtNames = self.globals.MediumFont.render("Matt Coles", 1, self.globals.WHITE)
        text_width, text_height = self.globals.MediumFont.size("Matt Coles")
        self.globals.ViewScreen.blit(ArtNames, (self.globals.SCREEN.centerx - text_width//2, 350))

        Music = self.globals.TitleFont.render("Music", 1, self.globals.WHITE)
        text_width, text_height = self.globals.TitleFont.size("Music")
        self.globals.ViewScreen.blit(Music, (self.globals.SCREEN.centerx - text_width//2, 450))

        MusicNames = self.globals.MediumFont.render("Noc.V - Thomas Stiegler", 1, self.globals.WHITE)
        text_width, text_height = self.globals.MediumFont.size("Noc.V - Thomas Stiegler")
        self.globals.ViewScreen.blit(MusicNames, (self.globals.SCREEN.centerx - text_width//2, 500))

        return super().draw()