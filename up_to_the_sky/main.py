
import pygame
pygame.init()
pygame.key.set_repeat(1,1)

# imports from local files
from colors import Red, Blue, White, Green

# define display and refresh rate
canvas_width, canvas_height = 350, 600
canvas = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption("Up To The Sky")
frames = pygame.time.Clock()
fps = 60

# background settings
background_pos = [[0, 0], [0, -600]]

# player settings
gravity = 2
player_speed = 5
player_width, player_height = 140, 130
player_pos = [canvas_width/2 - (player_width/2), canvas_height/1.25 - (player_height/2)]


def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            elif event.key == pygame.K_a:
                if player_pos[0] <= 0:
                    player_pos[0] = 0
                else:
                    player_pos[0] = player_pos[0] - player_speed

            elif event.key == pygame.K_d:
                if player_pos[0] >= canvas_width - player_width:
                    player_pos[0] = canvas_width - player_width
                else:
                    player_pos[0] = player_pos[0] + player_speed

            elif event.key == pygame.K_w:
                player_pos[1] = player_pos[1] - player_speed


def player(color):
    enemy_image = pygame.image.load("enemy.png")
    player_image = pygame.image.load("player.png")

    if player_pos[1] < canvas_height - player_height:
        player_pos[1] = player_pos[1] + gravity
    else:
        player_pos[1] = canvas_height - player_height

    canvas.blit(player_image, (player_pos[0], player_pos[1]))
    canvas.blit(enemy_image, (0, 0))

def background():
    sky_image = pygame.image.load("sky.png")
    canvas.blit(sky_image, (background_pos[0][0], background_pos[0][1]))
    canvas.blit(sky_image, (background_pos[1][0], background_pos[1][1]))


    for i in range(len(background_pos)):
        if background_pos[i][1] > canvas_height:
            background_pos.pop(i)
            background_pos.append([0, -600])
        else:
            background_pos[0][1] = background_pos[0][1] + 1
            background_pos[1][1] = background_pos[1][1] + 1

while True:

    background()
    event_handler()
    player(color=Blue)

    frames.tick(fps)
    pygame.display.update()
