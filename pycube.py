# Draw a hardcoded cube on the given X and Y using lines

import pygame, random

pygame.init()

canvas_width, canvas_height = 400,400
canvas = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption("Cube on PyGame")

blue = (80,120,200)
white = (255,255,255)

x = 50
y = 150
z = 70
length = 280

def draw_cube(color):
    # FRONT SQUARE
    pygame.draw.line(canvas, color, [x, y],      [length, y], 2)                 # A1
    pygame.draw.line(canvas, color, [length, y], [length,length], 2)             # B1
    pygame.draw.line(canvas, color, [x, length], [length, length], 2)            # C1
    pygame.draw.line(canvas, color, [x, y],      [x, length], 2)                 # D1
    # BACK SQUARE
    pygame.draw.line(canvas, color, [x+z, y-z],      [length+z, y-z], 2)         # A2
    pygame.draw.line(canvas, color, [length+z, y-z], [length+z, length-z], 2)    # B2
    pygame.draw.line(canvas, color, [x+z, length-z], [length+z, length-z], 2)    # C2
    pygame.draw.line(canvas, color, [x+z, y-z],      [x+z, length-z], 2)         # D2
    # CONNECTORS BETWEEN THE SQUARES
    pygame.draw.line(canvas, color, [x,y],            [x+z, y-z], 2)             # A3
    pygame.draw.line(canvas, color, [length, y],      [length+z, y-z], 2)        # B3
    pygame.draw.line(canvas, color, [x, length],      [x+z, length-z], 2)        # C3
    pygame.draw.line(canvas, color, [length, length], [length+z, length-z], 2)   # D3



while True:
    pygame.draw.rect(canvas, blue, [0,0,canvas_width,canvas_height])
    draw_cube(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    pygame.display.update()
