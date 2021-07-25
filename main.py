import os, pygame
from game.globals import *
from game.character import Character, enums

pygame.init()
pygame.display.set_caption('Western Harry')


player = Character('player', 200, 200, 3, 5, GRAVITY)
player_move_left = False
player_move_right = False
player.actions = enums.Action

def draw_background():
    ViewScreen.fill(ViewScreenBackgroundColor)
    pygame.draw.line(ViewScreen, GroundColor, (0, 300), (SCREEN.width, 300))

while GameRunning:
    Clock.tick(FPS)
    draw_background()

    player.update_animation()
    player.draw(ViewScreen)

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
            GameRunning = False

    pygame.display.update()

pygame.quit()
