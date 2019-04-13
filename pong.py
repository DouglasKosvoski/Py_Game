import sys, pygame
pygame.init()

print('''
PLAYER1 = W, S
PLAYER2 = UPARROW, DOWNARROW
SPACE   = THROW THE BALL
''')


black = (0,0,0)
gray = (128,128,128)
blue = (102,102,255)
green = (0,255,0)#(102,255,179)
white = (255,255,255)
white = (255,255,255)

canvas_width, canvas_height = 640,480
canvas = pygame.display.set_mode((canvas_width,canvas_height))
pygame.key.set_repeat(1,1)
pygame.display.set_caption("Pong")
fps = pygame.time.Clock()

def background(color,startX,startY,endX,endY):
    pygame.draw.rect(canvas,color,[startX,startY,endX,endY])

def midlle_line(color,startX,startY,endX,endY,line_tickness):
    for i in range(10):
        pygame.draw.line(canvas,color,[startX,(i*startY)+10],[endX,i*endY+20],line_tickness)

def pipe(pipeX,startY,pipe_tickness,endY):
    pygame.draw.rect(canvas,green,[pipeX,startY,pipe_tickness,endY])

def ball(color,ballX,ballY,ball_rad):
    pygame.draw.circle(canvas,color,(ballX,ballY),ball_rad)

def game_loop():

    # left pipe
    pipeXL = canvas_width/10
    startYL = 165
    endYL = 150

    # right pipe
    pipeXR = canvas_width-64
    startYR = 165
    endYR = 150
    pipe_tickness = 15
    pipe_change = 15
    ball_rad = 12
    ballX = int(pipeXL+ball_rad+pipe_tickness+1)
    ballY = int(canvas_height/2)
    ball_Xspeed = 0
    ball_Yspeed = 0

    ended = False
    while not ended:
        background(blue,0,0,canvas_width,canvas_height)
        midlle_line(green,canvas_width/2,50,canvas_width/2,50,5)
        pipe(pipeXR,startYR,pipe_tickness,endYR)
        pipe(pipeXL,startYL,pipe_tickness,endYL)

        # ball movement
        ballX += int(ball_Xspeed)
        ballY += int(ball_Yspeed)
        ball(green,ballX,ballY,ball_rad)

        # if ball hits right pipe
        if ballX >= pipeXR-ball_rad and startYR < ballY <= startYR+endYR:
            ball_Xspeed *= -1

        # if ball hits left
        if ballX <= pipeXL+ball_rad+pipe_tickness and startYL < ballY <= startYL+endYL:
            ball_Xspeed *= -1


        # if ball hits the border of the screen
        # # width
        if ballX <= 0:
            ballX = int(pipeXL+ball_rad+pipe_tickness+1)
            ballY = int(startYL+(startYL/2))
            ball_Xspeed = 0
            ball_Yspeed = 0

        elif ballX >= canvas_width:
            ballX = int(pipeXL+ball_rad+pipe_tickness+1)
            ballY = int(startYL+(startYL/2))
            ball_Xspeed = 0
            ball_Yspeed = 0

        # height
        if ballY <= 0 or ballY >= canvas_height:
            ball_Yspeed *= -1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_SPACE:
                    ball_Xspeed = 10
                    ball_Yspeed = 5


                # PLAYER 1
                elif event.key == pygame.K_w:
                    startYL -= pipe_change
                    pipe(pipeXL,startYL,pipe_tickness,endYL)
                    if startYL <= 0:
                        startYL = 0

                elif event.key == pygame.K_s:
                    startYL += pipe_change
                    pipe(pipeXL,startYL,pipe_tickness,endYL)
                    if startYL+150 >= canvas_height:
                        startYL = canvas_height-150

                # PLAYER 2
                elif event.key == pygame.K_UP:
                    startYR -= pipe_change
                    pipe(pipeXR,startYR,pipe_tickness,endYR)
                    if startYR <= 0:
                        startYR = 0

                elif event.key == pygame.K_DOWN:
                    startYR += pipe_change
                    pipe(pipeXR,startYR,pipe_tickness,endYR)
                    if startYR+150 >= canvas_height:
                        startYR = canvas_height-150


        fps.tick(60)
        pygame.display.update()

game_loop()
