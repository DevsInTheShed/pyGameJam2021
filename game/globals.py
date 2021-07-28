import os, pygame

pygame.font.init()

GameTitle = "Western Defender"

# Game and View State
SCREEN = pygame.Rect(0,0, 800, int(800 * 0.8))
ViewScreen = pygame.display.set_mode((SCREEN.width, SCREEN.height))
GameRunning = True
PlayerTypes = {
    "player": "player",
    "coop": "coop"
}
EnemyTypes = {
    "alien1": "alien1",
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
SmallFont = pygame.font.SysFont('comicsans', 20)

# Images 
StartImg = pygame.image.load(os.path.join('assets', 'sprites', 'button', 'single_player.png'))
Level1Img = pygame.image.load(os.path.join('assets', 'sprites', 'button', 'level1.png'))
Level2Img = pygame.image.load(os.path.join('assets', 'sprites', 'button', 'level2.png'))
Level3Img = pygame.image.load(os.path.join('assets', 'sprites', 'button', 'level3.png'))
Level4Img = pygame.image.load(os.path.join('assets', 'sprites', 'button', 'level4.png')) 
BulletImg = pygame.image.load(os.path.join('assets', 'sprites', 'icons', 'bullet.png')).convert_alpha()

HudChrome = pygame.image.load(os.path.join('assets', 'sprites', 'ui', 'hudChrome.png'))
ShotgunImg = pygame.image.load(os.path.join('assets', 'sprites', 'icons', 'shotgun.png'))

#background
pine1_img = pygame.image.load(os.path.join('assets', 'background', 'mountain.png')).convert_alpha()
pine2_img = pygame.image.load(os.path.join('assets', 'background', 'pine1.png')).convert_alpha()
mountain_img = pygame.image.load(os.path.join('assets', 'background', 'pine2.png')).convert_alpha()
sky_img = pygame.image.load(os.path.join('assets', 'background', 'sky_cloud.png')).convert_alpha()

PlayerSprites = {
    "player": [],
    "coop": []
}
EnemySprites = {
    "alien1": [],
}

# Physics constants
Clock = pygame.time.Clock()
FPS = 60
GRAVITY = 0.75
CharacterScale = 3
TileSize = 50

bg_scroll = 0

def getCharacterSprites(characterTypes, animationTypes, spriteList):
    for char_type in characterTypes:
        for animation in animationTypes:
            temp_list = []
            num_of_frames = len(os.listdir(os.path.join('assets', 'sprites', 'characters', char_type, animation)))
            for i in range(num_of_frames):
                i = str(i)
                img = pygame.image.load(os.path.join('assets', 'sprites', 'characters', char_type, animation, i+'.png')).convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * CharacterScale), int(img.get_height() * CharacterScale)))
                temp_list.append(img)

            spriteList[char_type].append(temp_list)

animation_types = ['Idle', 'Run', 'Jump', 'Death']
getCharacterSprites(PlayerTypes, animation_types, PlayerSprites)
getCharacterSprites(EnemyTypes, animation_types, EnemySprites)

# for char_type in PlayerTypes:
#     for animation in animation_types:
#         temp_list = []
#         num_of_frames = len(os.listdir(os.path.join('assets', 'sprites', char_type, animation)))
#         for i in range(num_of_frames):
#             i = str(i)
#             img = pygame.image.load(os.path.join('assets', 'sprites', char_type, animation, i+'.png')).convert_alpha()
#             img = pygame.transform.scale(img, (int(img.get_width() * CharacterScale), int(img.get_height() * CharacterScale)))
#             temp_list.append(img)

#         PlayerSprites[char_type].append(temp_list)

# for char_type in EnemyTypes:
#     for animation in animation_types:
#         temp_list = []
#         num_of_frames = len(os.listdir(os.path.join('assets', 'sprites', 'enemy', char_type, animation)))
#         for i in range(num_of_frames):
#             i = str(i)
#             img = pygame.image.load(os.path.join('assets', 'sprites', 'enemy', self.char_type, animation, i+'.png')).convert_alpha()
#             img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
#             temp_list.append(img)

#         self.animation_list.append(temp_list)
