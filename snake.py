import pygame, random
pygame.init()

display_width, display_height = 640, 480
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")
pygame.key.set_repeat(1,1)
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red   = (255, 0, 0)
green = (20, 140, 80)
blue  = (20, 80, 200)

grid_color = black
score = 0
# snake cordinates
snake_pos = [(320, 240)]#s,(340, 240),(360, 240)]
snake_movement = 20
snake_width, snake_height = 20, 20
snake_color = white

apple_width, apple_height = 20, 20
apple_x = random.randint(0, display_width - apple_width) // 20 * 20
apple_y = random.randint(0, display_height - apple_height) // 20 * 20


def background(color):
    pygame.draw.rect(display, color, (0, 0, display_width, display_height))

def grid():
    for x in range(0,display_width,20):
        pygame.draw.rect(display,grid_color,[x,0,1,display_height])
    for y in range(0,display_height,20):
        pygame.draw.rect(display,grid_color,[0,y,display_width,1])

def snake():
    for i in range(len(snake_pos)):
        pygame.draw.rect(display, snake_color, (snake_pos[i][0], snake_pos[i][1], snake_width, snake_height))

def apple(color):
    pygame.draw.rect(display, color, (apple_x, apple_y, apple_width, apple_height))


while True:

    for i in range(len(snake_pos) -1, 0, -1):
        snake_pos[i] = (snake_pos[i-1][0], snake_pos[i-1][1])

    background(blue)
    grid()
    apple(red)
    snake()

    if snake_pos[0][0] == apple_x and snake_pos[0][1] == apple_y:
        apple_x = random.randint(0, display_width - apple_width) // 20 * 20
        apple_y = random.randint(0, display_height - apple_height) // 20 * 20
        snake_pos.append((snake_pos[-1],260))
        score += 1
        print("SCORE = ", score)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            elif event.key == pygame.K_w:
                if snake_pos[0][1] - snake_height <= 0:
                    snake_pos[0] = (snake_pos[0][0], 0)
                else:
                    snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - snake_movement)

            elif event.key == pygame.K_s:
                if snake_pos[0][1] + snake_height >= display_height:
                    snake_pos[0] = (snake_pos[0][0], display_height - snake_height)
                else:
                    snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + snake_movement)

            elif event.key == pygame.K_a:
                if snake_pos[0][0] <= 0:
                    snake_pos[0] = (0, snake_pos[0][1])
                else:
                    snake_pos[0] = (snake_pos[0][0] - snake_movement, snake_pos[0][1])

            elif event.key == pygame.K_d:
                if snake_pos[0][0] + snake_width >= display_width:
                    snake_pos[0] = (display_width - snake_width, snake_pos[0][1])
                else:
                    snake_pos[0] = (snake_pos[0][0] + snake_movement, snake_pos[0][1])


    pygame.display.update()
    clock.tick(20)
