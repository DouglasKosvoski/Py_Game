import pygame, time
from datetime import datetime

pygame.init()
(resolution) = canvas_width, canvas_height = 500, 450
canvas = pygame.display.set_mode(resolution)
active = (0,255,0)
inactive = (70,70,70)


def background(cor=(50,50,50)):
    pygame.draw.rect(canvas, cor, [0,0,resolution[0],resolution[1]])

def a_left(ligado=False):
    pos = (75,40)
    size = (100,20)
    if ligado == True:
        pygame.draw.rect(canvas, active, [pos[0], pos[1], size[0], size[1]])
    else:
        pygame.draw.rect(canvas, inactive, [pos[0], pos[1], size[0], size[1]])
def b_left(ligado=False):
    size = (20,100)
    pos = (225-30,75)
    if ligado == True:
        pygame.draw.rect(canvas, active, [pos[0], pos[1], size[0], size[1]])
    else:
        pygame.draw.rect(canvas, inactive, [pos[0], pos[1], size[0], size[1]])
def c_left(ligado=False):
    size = (20,100)
    pos = (225-30,235)
    if ligado == True:
        pygame.draw.rect(canvas, active, [pos[0], pos[1], size[0], size[1]])
    else:
        pygame.draw.rect(canvas, inactive, [pos[0], pos[1], size[0], size[1]])
def d_left(ligado=False):
    pos = (75,355)
    size = (100,20)
    if ligado == True:
        pygame.draw.rect(canvas, active, [pos[0], pos[1], size[0], size[1]])
    else:
        pygame.draw.rect(canvas, inactive, [pos[0], pos[1], size[0], size[1]])
def e_left(ligado=False):
    size = (20,100)
    pos = (35,235)
    if ligado == True:
        pygame.draw.rect(canvas, active, [pos[0], pos[1], size[0], size[1]])
    else:
        pygame.draw.rect(canvas, inactive, [pos[0], pos[1], size[0], size[1]])
def f_left(ligado=False):
    size = (20,100)
    pos = (35,75)
    if ligado == True:
        pygame.draw.rect(canvas, active, [pos[0], pos[1], size[0], size[1]])
    else:
        pygame.draw.rect(canvas, inactive, [pos[0], pos[1], size[0], size[1]])
def g_left(ligado=False):
    pos = (75,195)
    size = (100,20)
    if ligado == True:
        pygame.draw.rect(canvas, active, [pos[0], pos[1], size[0], size[1]])
    else:
        pygame.draw.rect(canvas, inactive, [pos[0], pos[1], size[0], size[1]])

def a_right(ligado=False):
    pos = (75+250,40)
    size = (100,20)
    if ligado == True:
        pygame.draw.rect(canvas, active, [pos[0], pos[1], size[0], size[1]])
    else:
        pygame.draw.rect(canvas, inactive, [pos[0], pos[1], size[0], size[1]])
def b_right(ligado=False):
    size = (20,100)
    pos = (225-30+250,75)
    if ligado == True:
        pygame.draw.rect(canvas, active, [pos[0], pos[1], size[0], size[1]])
    else:
        pygame.draw.rect(canvas, inactive, [pos[0], pos[1], size[0], size[1]])
def c_right(ligado=False):
    size = (20,100)
    pos = (225-30+250,235)
    if ligado == True:
        pygame.draw.rect(canvas, active, [pos[0], pos[1], size[0], size[1]])
    else:
        pygame.draw.rect(canvas, inactive, [pos[0], pos[1], size[0], size[1]])
def d_right(ligado=False):
    pos = (75+250,355)
    size = (100,20)
    if ligado == True:
        pygame.draw.rect(canvas, active, [pos[0], pos[1], size[0], size[1]])
    else:
        pygame.draw.rect(canvas, inactive, [pos[0], pos[1], size[0], size[1]])
def e_right(ligado=False):
    size = (20,100)
    pos = (35+250,235)
    if ligado == True:
        pygame.draw.rect(canvas, active, [pos[0], pos[1], size[0], size[1]])
    else:
        pygame.draw.rect(canvas, inactive, [pos[0], pos[1], size[0], size[1]])
def f_right(ligado=False):
    size = (20,100)
    pos = (35+250,75)
    if ligado == True:
        pygame.draw.rect(canvas, active, [pos[0], pos[1], size[0], size[1]])
    else:
        pygame.draw.rect(canvas, inactive, [pos[0], pos[1], size[0], size[1]])
def g_right(ligado=False):
    pos = (75+250,195)
    size = (100,20)
    if ligado == True:
        pygame.draw.rect(canvas, active, [pos[0], pos[1], size[0], size[1]])
    else:
        pygame.draw.rect(canvas, inactive, [pos[0], pos[1], size[0], size[1]])

def draw_segs(aa,bb,cc,dd,ee,ff,gg, w):
    if w == "left":
        a_left(aa)
        b_left(bb)
        c_left(cc)
        d_left(dd)
        e_left(ee)
        f_left(ff)
        g_left(gg)
    if w == "right":
        a_right(aa)
        b_right(bb)
        c_right(cc)
        d_right(dd)
        e_right(ee)
        f_right(ff)
        g_right(gg)
def draw_display():
    temp = datetime.now().second

    tempo_R = int(str(temp)[-1])
    if len(str(temp)) > 1:
        tempo_L = int(str(temp)[-2])
    else:
        tempo_L = -999

    if tempo_R != -999:
        if tempo_R == 0:
            draw_segs(True,True,True,True,True,True,False, "right")
        elif tempo_R == 1:
            draw_segs(False,True,True,False,False,False,False, "right")
        elif tempo_R == 2:
            draw_segs(True,True,False,True,True,False,True, "right")
        elif tempo_R == 3:
            draw_segs(True, True,True,True,False,False,True, "right")
        elif tempo_R == 4:
            draw_segs(False, True,True,False,False,True,True, "right")
        elif tempo_R == 5:
            draw_segs(True,False,True,True,False,True,True, "right")
        elif tempo_R == 6:
            draw_segs(True,False,True,True,True,True,True, "right")
        elif tempo_R == 7:
            draw_segs(True, True,True,False,False,False,False, "right")
        elif tempo_R == 8:
            draw_segs(True, True,True,True,True,True,True, "right")
        elif tempo_R == 9:
            draw_segs(True, True,True,True,False,True,True, "right")
    if tempo_L != -999:
        if tempo_L == 0:
            draw_segs(True,True,True,True,True,True,False, "left")
        elif tempo_L == 1:
            draw_segs(False,True,True,False,False,False,False, "left")
        elif tempo_L == 2:
            draw_segs(True,True,False,True,True,False,True, "left")
        elif tempo_L == 3:
            draw_segs(True, True,True,True,False,False,True, "left")
        elif tempo_L == 4:
            draw_segs(False, True,True,False,False,True,True, "left")
        elif tempo_L == 5:
            draw_segs(True,False,True,True,False,True,True, "left")
        elif tempo_L == 6:
            draw_segs(True,False,True,True,True,True,True, "left")
        elif tempo_L == 7:
            draw_segs(True, True,True,False,False,False,False, "left")
        elif tempo_L == 8:
            draw_segs(True, True,True,True,True,True,True, "left")
        elif tempo_L == 9:
            draw_segs(True, True,True,True,False,True,True, "left")
    else:
        draw_segs(False, False,False,False,False,False,False, "left")

while True:
    background()
    draw_display()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit
                quit()

    pygame.display.update()
