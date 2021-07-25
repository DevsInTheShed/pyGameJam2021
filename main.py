import os, pygame
from game import game_characters, enums

pygame.init()

screen_width = 800
screen_height = int(screen_width * 0.8)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Western Harry')
clock = pygame.time.Clock()
fps = 60
game_running = True
game_background_color = (61, 43, 31)
game_ground_color = (255, 200, 200)
GRAVITY = 0.75

player = game_characters.Character('player', 200, 200, 3, 5, GRAVITY)
player_move_left = False
player_move_right = False
player.actions = enums.Action

def draw_background():
    screen.fill(game_background_color)
    pygame.draw.line(screen, game_ground_color, (0, 300), (screen_width, 300))

while game_running:
    clock.tick(fps)
    draw_background()

    player.update_animation()
    player.draw(screen)

    if player.alive:
        if player.in_air:
            player.update_action(player.actions.jump)
        elif player_move_left or player_move_right:
            player.update_action(player.actions.run)
        else:
            player.update_action(player.actions.idle)
        player.move(player_move_left, player_move_right)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
            if event.key == pygame.K_LEFT:
                player_move_left = True
            if event.key == pygame.K_RIGHT:
                player_move_right = True
            if event.key == pygame.K_UP and player.alive:
                player.jump = True
            if event.key == pygame.K_SPACE:
                shoot = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_move_left = False
            if event.key == pygame.K_RIGHT:
                player_move_right = False
            if event.key == pygame.K_UP and player.alive:
                player.jump = False
            if event.key == pygame.K_SPACE:
                shoot = False

        if event.type == pygame.QUIT:
            game_running = False

    pygame.display.update()

pygame.quit()
