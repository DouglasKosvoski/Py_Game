import pygame, random
pygame.init()

canvas_width, canvas_height = 640, 480
canvas = pygame.display.set_mode((canvas_width, canvas_height))
fps = pygame.time.Clock()

gray  = (120,120,120)
red   = (255,50,100)
blue  = (80, 120, 200)
white = (255,255,255)

speed = 5
radius = 40
y = int(canvas_height-100 - radius)

def background(color):
    lineX, lineY = 30, canvas_height-100
    pygame.draw.rect(canvas, color, [0,0,canvas_width,canvas_height])
    pygame.draw.line(canvas, white, [lineX, lineY] , [canvas_width - lineX, lineY], 2)

def object(color):
    x = int(canvas_width / 2)
    pygame.draw.circle(canvas, color, (x, y), radius, 2)

while True:
    background(blue)
    object(white)

    if y <= 0 + radius:
        speed *= -1
    if y > canvas_height-100 - radius:
        speed *= -1

    y -= speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            if event.key == pygame.K_SPACE:
                speed *= -1

    fps.tick(60)
    pygame.display.update()
