# draw a certain pattern as result of the given angle value

import pygame, math
pygame.init()

canvas_width, canvas_height = 640, 480
canvas = pygame.display.set_mode((canvas_width, canvas_height))
fps = pygame.time.Clock()

white  = (255,255,255)
gray   = (120,120,120)
blue   = (20,80,210)
red    = (255,0,0)
green  = (0,255,0)
green1 = (0,80,0)
black  = (0,0,0)

angle = 0
radius = 200
speed = -1 / 360
graph = []

while True:
    pygame.draw.rect(canvas, black, [0, 0, canvas_width, canvas_height])     # BACKGROUND
    pygame.draw.ellipse(canvas, gray, [75, 125, radius, radius], 1)          # first circle
    pygame.draw.ellipse(canvas, gray, [170,220, radius/15, radius/15], 1)  # middle circle

    x = radius/2 * math.cos(angle)
    y = radius/2 * math.sin(angle)
    x += 175
    y += 225

    pygame.draw.line(canvas, green, [175,225], [x, y],2)

    graph.append(y)
    for i in range(len(graph), 0, -1):
        horizontal_speed = 1.2
        pygame.draw.ellipse(canvas, white, [(i*horizontal_speed)+350, graph[-i], 2, 2], 1)      # graph circle
        if len(graph) >= 350:
            graph.pop(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == pygame.K_UP:
                speed += 0.05
            elif event.key == pygame.K_DOWN:
                speed -= 0.05

    angle -= speed
    fps.tick(60)
    pygame.display.update()
