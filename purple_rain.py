from random import randint
import sys
import pygame
# initialize pygame functions
pygame.init()

light_purple = (247, 230, 255)
purple = (159, 99, 187)

# set resolution
canvas_width,canvas_height = 640,480
# create window
canvas = pygame.display.set_mode((canvas_width,canvas_height))
# set window name
pygame.display.set_caption("Purple Rain")
# define fps constant
fps = pygame.time.Clock()
framesPerSecond = 60
# Min and Max drop speeds
min_speed,max_speed = 1,5
gravity = 0.8

x_list = [] # store x values of the rain
y_list = [] # store y values of the rain

while True:
    # draw background filling the whole window
    pygame.draw.rect(canvas,light_purple,[0,0, canvas_width,canvas_height])
    # get random speed between Min and Max values
    rain_speed = 10
    # density of raindrops
    for i in range(1): # increase range to add raindrops
        # random x raindrop start position
        rain_xPos = randint(0,canvas_width)
        # start raining upside the window in a random value
        rain_yPos = randint(-canvas_height,-20)
        x_list.append(rain_xPos)
        y_list.append(rain_yPos)

    # move the drops down considering their Y position
    for w in range(len(x_list)):
        # increase the rain speed adding the gravity factor to it
        #rain_speed += gravity

        # change the Y value to make it goes down
        y_list[w]+= rain_speed
        # draw the line (drop)
        pygame.draw.line(canvas,purple,(x_list[w],y_list[w]),(x_list[w],y_list[w]+10),2)


    # if drop is below the canvas border reset it to a new X and Y position
    if rain_yPos>canvas_height:
        rain_yPos  = randint(-canvas_height,-20)
        rain_xPos  = randint(0,canvas_width)

    # Check for ESC key pressed or pygame window closed to quit
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

       # if key pressed is ESC
       elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             pygame.quit()
             sys.exit()

    fps.tick(framesPerSecond)
    pygame.display.flip()
