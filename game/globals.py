import os, pygame

pygame.font.init()

GameTitle = "Western Defender"

# Game and View State
SCREEN = pygame.Rect(0,0, 800, int(800 * 0.8))
ViewScreen = pygame.display.set_mode((SCREEN.width, SCREEN.height))
GameRunning = True
CharacterTypes = {
    "player": "player",
    "coop": "coop"
}

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
Level1Img = pygame.image.load(os.path.join('assets', 'sprites', 'button', 'level1.png'))
Level2Img = pygame.image.load(os.path.join('assets', 'sprites', 'button', 'level2.png'))
Level3Img = pygame.image.load(os.path.join('assets', 'sprites', 'button', 'level3.png'))
Level4Img = pygame.image.load(os.path.join('assets', 'sprites', 'button', 'level4.png'))
CharacerSprites = {
    "player": [],
    "coop": []
}

# Physics constants
Clock = pygame.time.Clock()
FPS = 60
GRAVITY = 0.75
CharacterScale = 3


for char_type in CharacterTypes:
    for animation in ['Idle', 'Run', 'Jump']:
        temp_list = []
        num_of_frames = len(os.listdir(os.path.join('assets', 'sprites', char_type, animation)))
        for i in range(num_of_frames):
            i = str(i)
            img = pygame.image.load(os.path.join('assets', 'sprites', char_type, animation, i+'.png')).convert_alpha()
            img = pygame.transform.scale(img, (int(img.get_width() * CharacterScale), int(img.get_height() * CharacterScale)))
            temp_list.append(img)

        CharacerSprites[char_type].append(temp_list)