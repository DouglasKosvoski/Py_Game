
import pygame, random, time
pygame.init()
pygame.key.set_repeat(1,1)

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
player_image = pygame.image.load("player.png")
gravity = 2
player_speed = 5
player_width, player_height = 140, 130
player_pos = [canvas_width/2 - (player_width/2), canvas_height/2 - (player_height/2)]

# enemy settings
hp = 5
enemy_image = pygame.image.load("enemy.png")
enemy_width, enemy_height = 100, 90
enemy_pos = [random.randint(1, canvas_width-enemy_width), 1]
limit_inferior, limit_superior = canvas_height/2, 0
left_limit, right_limit = 0, canvas_width - enemy_width
enemy_xspeed, enemy_yspeed = 5, 2

# bullet settings
bullet_image = pygame.image.load("white_shot.png")
max_bullets = 15
bullets = []
bullet_width = 20
bullet_height = 50
bullet_speed = 7


textObjectsColor = (255,0,0)
def text_objects(text, font):                                                           # define function to display a message if crash equals True
    textSurface = font.render(text, True, textObjectsColor)                             # text parameters
    return textSurface, textSurface.get_rect()                                          # return the message in a rectangle

def message_display(text):                                                              # fuction create text
    largeText = pygame.font.Font("freesansbold.ttf", 45)                                # define text font and size
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect = (canvas_width-150, 0)                            # show the message in the center of the display
    canvas.blit(TextSurf, TextRect)

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

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            if event.key == pygame.K_SPACE:
                # append the bullet in the middle of the player model
                bullets.append([player_pos[0]+(player_width/2)-(bullet_width/2), player_pos[1]])

                if len(bullets) > max_bullets:
                    bullets.pop(0)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if 0 <= player_pos[1] and player_pos[1] <= canvas_height - player_height:
                    player_pos[1] = player_pos[1] - player_speed

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

def player():
    canvas.blit(player_image, (player_pos[0], player_pos[1]))

    if player_pos[1] < canvas_height - player_height:
        player_pos[1] = player_pos[1] + gravity
    else:
        player_pos[1] = canvas_height - player_height

def enemy():
    global enemy_xspeed
    global enemy_yspeed

    canvas.blit(enemy_image, (enemy_pos[0], enemy_pos[1]))
    # moves vertically
    if limit_superior > enemy_pos[1] or enemy_pos[1] > limit_inferior:
        enemy_yspeed *= -1
    # moves horizontally
    if enemy_pos[0] <= left_limit or enemy_pos[0] > right_limit:
        enemy_xspeed *= -1

    enemy_pos[1] = enemy_pos[1] - enemy_yspeed
    enemy_pos[0] = enemy_pos[0] - enemy_xspeed

def shot():
    global hp
    global enemy_pos
    global bullets

    for i in range(len(bullets)):

        bullet_x = bullets[i][0]
        bullet_y = bullets[i][1]
        bullets[i][1] = bullets[i][1] - bullet_speed
        canvas.blit(bullet_image, [bullet_x, bullet_y])

        if enemy_pos[0] < bullets[i][0] and bullets[i][0] + bullet_width < enemy_pos[0] + enemy_width:
            if enemy_pos[1] < bullets[i][1] and bullets[i][1] + bullet_width < enemy_pos[1] + enemy_width:
                bullets[i] = [800, 800]#bullets.pop(i)
                hp -= 1

                if hp <= 0:
                    # TOCAR ANIMACAO DE EXPLOSAO AQUI //////////
                    enemy_pos = [random.randint(1, canvas_width-enemy_width), 1]
                    bullets = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
                               [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
                    hp = 5




while True:

    event_handler()
    background()
    player()
    enemy()
    shot()
    message_display('hp = {0}'.format(hp))


    frames.tick(fps)
    pygame.display.update()
