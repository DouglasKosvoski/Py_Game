# The code generates a third circle as the result of colors of the first and second ones

import pygame
pygame.init()

canvas_width, canvas_height = 640, 480
canvas = pygame.display.set_mode((canvas_width, canvas_height))

first_color = list(map(int, input("Enter RGB 1: ").split(',')))
second_color = list(map(int, input("Enter RGB 2: ").split(',')))

result_color = ((first_color[0] + second_color[0]) / 2,
                (first_color[1] + second_color[1]) / 2,
                (first_color[2] + second_color[2]) / 2)


while True:
    pygame.draw.circle(canvas, first_color,  (320-100,240), 100)
    pygame.draw.circle(canvas, second_color, (320+100,240), 100)
    pygame.draw.circle(canvas, result_color, (320,140), 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    pygame.display.update()
