
import pygame, random
pygame.init()
pygame.key.set_repeat(1,1)

# imports from local files
from colors import Red, Blue, White, Green

# define display and refresh rate
canvas_width, canvas_height = 500, 800
canvas = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption("Up To The Sky")
frames = pygame.time.Clock()
fps = 60

# background settings
sky_image = pygame.image.load("sky.png")
background_speed = 1
sky_image_width = 500
sky_image_height = 800
background_pos = [[0, 0], [0, -sky_image_height]]

# player settings
gravity = 2
player_speed = 5
player_width, player_height = 140, 130
player_pos = [canvas_width/2 - (player_width/2), canvas_height/2 - (player_height/2)]

# enemy settings
enemy_down = True
enemy_left = False
enemy_right = False

enemy_image = pygame.image.load("enemy.png")
enemy_width, enemy_height = 100, 90
enemy_pos = [399,0]#[random.randint(1, canvas_width-enemy_width), 0]
enemy_speed = 1

limit_inferior = canvas_height/2 - (enemy_height/2)
right_limit = canvas_width - (enemy_width/2) - 150
left_limit = 150

def background():
    canvas.blit(sky_image, (background_pos[0][0], background_pos[0][1]))
    canvas.blit(sky_image, (background_pos[1][0], background_pos[1][1]))

    for i in range(len(background_pos)):
        if background_pos[i][1] > canvas_height:
            background_pos.pop(i)
            background_pos.append([0, -sky_image_height])
        else:
            background_pos[0][1] = background_pos[0][1] + background_speed
            background_pos[1][1] = background_pos[1][1] + background_speed

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

def player():
    player_image = pygame.image.load("player.png")

    if player_pos[1] < canvas_height - player_height:
        player_pos[1] = player_pos[1] + gravity
    else:
        player_pos[1] = canvas_height - player_height

    canvas.blit(player_image, (player_pos[0], player_pos[1]))

def enemy(enemy_down, enemy_left, enemy_right):
    canvas.blit(enemy_image, (enemy_pos[0], enemy_pos[1]))

    # if enemy is not in the bottom of the screen
    if enemy_pos[1] < limit_inferior:
        enemy_down = True
    else:
        enemy_down = False

    # if enemy is in the left corner
    if 0 < enemy_pos[0] and enemy_pos[0] <= left_limit:
        enemy_left = False
        enemy_right = True

   # if enemy is in the right corner
    elif right_limit < enemy_pos[0] and enemy_pos[0] < canvas_width - enemy_width:
        enemy_right = False
        enemy_left = True

    print('LIMIT LEFT =', left_limit)
    print('LIMIT RIGHT =', right_limit)
    print('RIGHT =',enemy_right)
    print('LEFT  =',enemy_left)
    print('DOWN  =',enemy_down)
    print()

    if enemy_down == True:
        enemy_pos[1] = enemy_pos[1] + enemy_speed

    if enemy_left == True:# and enemy_right == False:
        enemy_pos[0] = enemy_pos[0] - enemy_speed

    elif enemy_right == True:# and enemy_left == False:
        enemy_pos[0] = enemy_pos[0] + enemy_speed



while True:

    background()
    event_handler()
    player()
    enemy(enemy_down, enemy_left, enemy_right)

    frames.tick(fps)
    pygame.display.update()
