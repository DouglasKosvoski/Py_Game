import pygame
pygame.init()

black = (0,0,0)
white = (255,255,255)
gray  = (128,128,128)
canvas = pygame.display.set_mode((300, 200))
canvas.fill(black)

color, buttom_xpos,buttom_ypos, buttom_radius, buttom_thickness = gray,70,91,8,0
color, slider_x, slider_y, slider_width, slider_height = white,70, 90, 170, 3


while True:
    for event in pygame.event.get():
        click = pygame.mouse.get_pressed()

    if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    pygame.draw.rect(canvas,black,(0,0,400,400))
    pygame.draw.rect(canvas,white,(slider_x,slider_y,slider_width,slider_height))

    mouse = pygame.mouse.get_pos()

    insBX = buttom_xpos-buttom_radius < mouse[0] < buttom_xpos+buttom_radius
    insBY = buttom_ypos-buttom_radius < mouse[1] < buttom_ypos+buttom_radius
    if click[0]==1:
        if insBX and insBY:
            buttom_xpos = mouse[0]
            if buttom_xpos > 170+70:
                buttom_xpos = 170+70
            if buttom_xpos < 170-90-3:
                buttom_xpos = 170-90-3

    pygame.draw.circle(canvas, gray, (buttom_xpos,buttom_ypos), buttom_radius, buttom_thickness)
    click = pygame.mouse.get_pressed()
    pygame.display.update()
