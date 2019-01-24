# Is possible to get stuck in the corners
# The upside object will always be generated in order
# to be in collision route with the downside object

import pygame, random
pygame.init()

canvas_width, canvas_height = 600, 400
canvas = pygame.display.set_mode((canvas_width, canvas_height))
fps = pygame.time.Clock()

gray = (120,120,120)
red  = (255,50,100)
blue = (80,120,200)

# OBJECT
obj_speed  = 2
obj_width  = 50
obj_height = 50
objX = (canvas_width/2) - (obj_width/2)
objY = random.randint(-100, -70)

gap = 20

# CAR
car_speed  = 2
car_width  = 50
car_height = 50
carX = (canvas_width/2) - (car_width/2)
carY = canvas_height - car_height - 20

range_detection = 100

direction = random.randint(-1,1)
while direction == 0:
    direction = random.randint(-1,1)

def background(color):
    pygame.draw.rect(canvas, color, [0,0,canvas_width,canvas_height])

def object(color):
    pygame.draw.rect(canvas, color, [objX, objY, obj_width, obj_height])

def car(color):
    pygame.draw.rect(canvas, color, [carX, carY, car_width, car_height])

while True:
    background(gray)
    object(red)
    car(blue)

    # MOVE
    objY += 1.5*obj_speed

    # RESTART OBJECT POS
    if objY >= canvas_height:
        objX = carX#random.randint(0,canvas_width - obj_width )
        objY = random.randint(-100, -70)

        direction = random.randint(-1,1)
        while direction == 0:
            direction = random.randint(-1,1)
        #print(direction)


    # IF CAR IN COLISION ROUTE
    if objY > range_detection:
        if carX <= objX + obj_width + gap and carX >= objX-car_width-gap:
            # BOUNDARIES
            if carX <= gap:
                carX = gap
            elif carX >= canvas_width - car_width - gap:
                carX = canvas_width - car_width - gap

            # DECISION
            if direction < 0:
                carX -= car_speed
            elif direction > 0:
                carX += car_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    fps.tick(60)
    pygame.display.update()
