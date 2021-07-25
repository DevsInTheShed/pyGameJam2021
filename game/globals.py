import os, pygame

pygame.font.init()

# Game and View State
SCREEN = pygame.Rect(0,0, 800, int(800 * 0.8))
ViewScreen = pygame.display.set_mode((SCREEN.width, SCREEN.height))
GameRunning = True

# Color constants
ViewScreenBackgroundColor = (61, 43, 31)
GroundColor = (255, 200, 200)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

# Fonts
TitleFont = pygame.font.SysFont('comicsans', 40)

# Images 
StartImg = pygame.image.load(os.path.join('assets', 'sprites', 'button', 'single_player.png'))


# Physics constants
Clock = pygame.time.Clock()
FPS = 60
GRAVITY = 0.75
