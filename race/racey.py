import pygame                                                                           # import the pygame module
import time                                                                             # import time module
import random                                                                           # import random module
pygame.init()                                                                           # initiates the module

fps_menu = 60
fps_game = 60

# screen resolution
display_width  = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

# RGB Red, Green, Blue
Black	    = (0,0,0)
White	    = (255,255,255)
Red	        = (255,0,0)
Lime	    = (0,255,0)
Blue	    = (0,0,255)
Yellow	    = (255,255,0)
Cyan        = (0,255,255)
Magenta     = (255,0,255)
Silver	    = (192,192,192)
Gray	    = (128,128,128)
Maroon	    = (128,0,0)
Olive	    = (128,128,0)
Green	    = (0,128,0)
brightGreen = (0,158,0)
Purple	    = (128,0,128)
Teal	    = (0,128,128)
Navy	    = (0,0,128)
Gold        = (255,215,0)
DarkGolden  = (184,134,11)


ScoreColor = Black
textObjectsColor = Green
smallTextObjectsColor = DarkGolden
backgroundMenu = Silver
backgroundGame = White


pygame.display.set_caption("A Bit Racey")                                               # set the name of the display
clock = pygame.time.Clock()                                                             # set the internal clock of the program

carImg = pygame.image.load("RaceCar.png")                                               # this will load our image of a car
pause = False

# key bindins
GamePause     = pygame.K_ESCAPE
carAccelerate = pygame.K_w
carReverse    = pygame.K_s
carLeft       = pygame.K_a
carRight      = pygame.K_d


def things_dodged(count):
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: " + str(count), True, ScoreColor)
    gameDisplay.blit(text, (0, 0))

def things(thingx, thingy, thingw, thingh, color):                                      # define the function to create an object
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])              # pygame draw a rectangle

def car(x,y):                                                                           # define function
    gameDisplay.blit(carImg,(x,y))                                                      # function that will let us choose the image location

def smallText_objects(text, font):                                                      # define function to display a message if crash equals True
    smallText_objects = font.render(text, True, smallTextObjectsColor)                  # text parameters
    return smallText_objects, smallText_objects.get_rect()

def text_objects(text, font):                                                           # define function to display a message if crash equals True
    textSurface = font.render(text, True, textObjectsColor)                             # text parameters
    return textSurface, textSurface.get_rect()                                          # return the message in a rectangle

def message_display(text):                                                              # fuction create text
    largeText = pygame.font.Font("freesansbold.ttf", 45)                                # define text font and size
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))                            # show the message in the center of the display
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()                                                             # update so the message is shown
    time.sleep(2)                                                                       # duration of the message
    game_loop()                                                                         # game_loop() restart the game

def crash():                                                                            # define crash function
    message_display("You Crashed!")                                                     # if crash = True show message

def quitgame():
    pygame.quit()
    quit()

def button(msg, x, y, w, h, InactiveColor, ActiveColor, action=None):
    mouse = pygame.mouse.get_pos()
    #print("/// Mouse Pos: x = {0}. y = {1}".format(mouse[0], mouse[1]))
    click = pygame.mouse.get_pressed()
    print(click)

    # if mouse within button boundaries
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ActiveColor, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, InactiveColor, (x, y, w, h))

    # button text
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = smallText_objects(msg, smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def unpause():
    global pause
    pause = False

def paused():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            if event.type == pygame.KEYDOWN:                                              # if key was released
                if event.key == pygame.K_ESCAPE:
                    unpause()

        gameDisplay.fill(backgroundMenu)
        largeText = pygame.font.Font("freesansbold.ttf", 45)
        TextSurf, TextRect = text_objects(("Paused"), largeText)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)

        button("CONTINUE", 100, 235, 120, 45, Green, brightGreen, unpause)
        #button("CONFIG", 100, 335, 120, 45, Green, brightGreen, "CONFIG")
        button("QUIT  ", 100, 435, 120, 45, Green, brightGreen, quitgame)


        pygame.display.update()
        clock.tick(fps_menu)


# start the intro
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(backgroundMenu)
        largeText = pygame.font.Font("freesansbold.ttf", 35)
        TextSurf, TextRect = text_objects(("A Bit Racey! - Created by Douglas Kosvoski"), largeText)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)

        button("START ", 100, 235, 120, 45, Green, brightGreen, game_loop)
        #button("CONFIG", 100, 335, 120, 45, Green, brightGreen, "CONFIG")
        button("QUIT  ", 100, 435, 120, 45, Green, brightGreen, quitgame)


        pygame.display.update()
        clock.tick(fps_menu)

# run the game
def game_loop():
    global pause

    thing_width = 30                                                                    # width of the object (box)
    thing_height = 30                                                                   # height of the object (box)
    thing_startx = random.randrange(0, display_width - thing_width)                     # object start on a random x location
    thing_starty = -600                                                                 # object start y location, since is -600
    thing_speed = 7                                                                    # object speed (change location per loop)

    x = (display_width / 2) - (thing_width/2)                                           # define x position of the image
    y = display_height * 0.6
    x_change = 0                                                                        # initialy car is on x axis = 0
    y_change = 0                                                                        # initialy car is on y axis = 0
    car_width = 132                                                                     # image width
    car_height = 228                                                                    # image height


    dodged = 0                                                                          # how many times the object respawn (if it respawn means you avoided it)
    gameExit = False                                                                    # set that you are not crashed
    while not gameExit:                                                                 # while you're not crashed run the loop function
        for event in pygame.event.get():                                                # for each event in the event
            if event.type == pygame.QUIT:                                               # if the event was quit
                pygame.quit()                                                           # exit pygame
                quit()                                                                  # exit python
            print("Events: ", event)                                                    # for each event print it on console
            # key pressed
            if event.type == pygame.KEYDOWN:                                            # if any key was pressed
                if event.key == carLeft:                                                # if the key pressed was left arrow
                    x_change = -10                                                      # subtract 10 from x axis (object goes left)
                if event.key == carRight:                                               # if the key pressed was right arrow
                    x_change = 10                                                       # add 10 to x axis (object goes right)
                if event.key == carAccelerate:                                          # if the key pressed was up arrow
                    y_change = -10                                                      # subtract 10 to y axis (object goes up)
                if event.key == carReverse:                                             # if the key pressed was down arrow
                    y_change = 10                                                       # add 10 to y axis (object goes down)
                if event.key == GamePause:
                    pause = True
                    paused()


            # key release
            if event.type == pygame.KEYUP:                                              # if key was released
                # if the key either right or left arrow was released
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

            if event.type == pygame.KEYUP:                                              # if key was released
                # if the key either up or down arrow was released
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0



        x += x_change                                                                   # change value to show new object position on the x axis
        y += y_change                                                                   # change value to show new object position on the y axis

        gameDisplay.fill(backgroundGame)                                                         # set background color

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, Teal)
        thing_starty += thing_speed                                                     # increase y position of the box by its speed

        car(x,y)                                                                        # set the position of the car as the same of the image (this will sync both)
        things_dodged(dodged)

        # set boundaries
        if x > display_width - car_width or x < 0:                                      # if object out of x axis
            crash()                                                                     # breaks the loop
        if y > display_height - car_height or y < 0:                                    # if object out of y axis
            crash()                                                                     # breaks the loop

        if thing_starty > display_height:                                               # if the box will spawn out of the display height
            thing_starty = 0 - thing_height                                             # spawn the box minus its height (to be sure that the box will not be seen as soon as spawns)
            thing_startx = random.randrange(0, display_width - thing_width)             # define a random x location spawn
            dodged += 1
            thing_speed += 0.33


        if y < thing_starty + thing_height:
            print("y crossover")

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print("x crossover")
                crash()


        pygame.display.update()                                                         # refresh the display for each loop
        clock.tick(fps_game)                                                            # set frames per second

game_intro()
game_loop()
pygame.quit()                                                                           # if the loop was breaked unitialize the pygame module
quit()                                                                                  # built-in python function to quit
