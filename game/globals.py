import os, pygame
from pygame import transform
from pygame.constants import FULLSCREEN

pygame.font.init()

GameTitle = "Western Defender"

# Game and View State
SCREEN = pygame.Rect(0,0, 800, int(800 * 0.8))
ViewScreen = pygame.display.set_mode((SCREEN.width, SCREEN.height))
GameRunning = True
PlayerTypes = {
    "player": "player"
}
EnemyTypes = {
    "alien1": "alien1",
}

# Color constants
BackgroundColor = (220, 220, 144)
GroundColor = (220, 220, 144)
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
FlameImg = pygame.image.load(os.path.join('assets', 'sprites', 'icons', 'flame.png')).convert_alpha()

HudChrome = pygame.image.load(os.path.join('assets', 'sprites', 'ui', 'hudChrome.png'))
ShotgunImg = pygame.image.load(os.path.join('assets', 'sprites', 'icons', 'shotgun.png'))
RocketImg = pygame.image.load(os.path.join('assets', 'sprites', 'icons', 'rocket.png'))
FlamethrowerImg = pygame.image.load(os.path.join('assets', 'sprites', 'icons', 'flamethrower.png'))

#background
mountain_img = pygame.image.load(os.path.join('assets', 'background', 'mountain.png')).convert_alpha()
pine1_img = pygame.image.load(os.path.join('assets', 'background', 'pine1.png')).convert_alpha()
pine2_img = pygame.image.load(os.path.join('assets', 'background', 'pine2.png')).convert_alpha()
sky_img = pygame.image.load(os.path.join('assets', 'background', 'sky_cloud.png')).convert_alpha()

# level tiles
ROWS = 16
TileSize = SCREEN.height // ROWS
TileTypes = 27
TileList = []

for x in range(TileTypes):
    img = pygame.image.load(os.path.join('assets', 'tiles', f'{x}.png'))
    img = pygame.transform.scale(img, (TileSize, TileSize))
    TileList.append(img)


PlayerSprites = {
    "player": {
        "shotgun": [],
        "flamethrower": [],
        "rocket": [],
    }
}
EnemySprites = {
    "alien1": {
        "laser": [],
    },
}

# Physics constants
Clock = pygame.time.Clock()
FPS = 60
GRAVITY = 0.75
CharacterScale = 2
ScrollThreashold = 100



def getCharacterSprites(characterTypes, animationTypes, weaponTpes, spriteList):
    for char_type in characterTypes:
        for weapon in weaponTpes:
            for animation in animationTypes:
                temp_list = []
                num_of_frames = len(os.listdir(os.path.join('assets', 'sprites', 'characters', char_type, weapon, animation)))
                for i in range(num_of_frames):
                    i = str(i)
                    img = pygame.image.load(os.path.join('assets', 'sprites', 'characters', char_type, weapon, animation, f'{i}.png')).convert_alpha()
                    img = pygame.transform.scale(img, (int(img.get_width() * CharacterScale), int(img.get_height() * CharacterScale)))
                    temp_list.append(img)

                spriteList[char_type][weapon].append(temp_list)



animation_types = ['Idle', 'Run', 'Jump', 'Death', 'Fly', 'Shoot']
weapon_types = ["shotgun", "flamethrower", "rocket"]
getCharacterSprites(PlayerTypes, animation_types, weapon_types, PlayerSprites)
getCharacterSprites(EnemyTypes, animation_types, ["laser"], EnemySprites)

