# The code generates a third circle as the result of colors of the first and second ones

import pygame
pygame.init()

canvas_width, canvas_height = 640, 480
canvas = pygame.display.set_mode((canvas_width, canvas_height))

white = (255,255,255)
black = (0,0,0)
gray  = (120,120,120)
blue  = (0,0,255)
green = (0,255,0)
red   = (255,0,0)


while True:
    first_color = red
    second_color = gray
    result_color =  (first_color[0]+second_color[0])/2,(first_color[1]+second_color[1])/2,(first_color[2]+second_color[2])/2

    pygame.draw.circle(canvas, first_color,  (320-100,240), 100)
    pygame.draw.circle(canvas, second_color, (320+100,240), 100)
    pygame.draw.circle(canvas, result_color, (320,140), 100)

    #print(result_color)
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
