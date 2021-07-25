import  pygame

SCREEN = pygame.Rect(0,0, 800, int(800 * 0.8))
ViewScreen = pygame.display.set_mode((SCREEN.width, SCREEN.height))
Clock = pygame.time.Clock()
FPS = 60
GameRunning = True
ViewScreenBackgroundColor = (61, 43, 31)
GroundColor = (255, 200, 200)
GRAVITY = 0.75