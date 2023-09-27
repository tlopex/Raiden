import pygame
from Output import ranklist
import sys
from Record_MyScore import record_myscore

red =(255, 0, 0)
green =(20, 255, 20)
black =(0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

screen = pygame.display.set_mode((650, 517))

def rect (title, x, y, w, h, color):
    font = pygame.font.Font(None, 22)
    pygame.draw.rect(screen, color, [x,y,w,h])
    namelen = len(title)//2+7
    screen.blit(font.render(title, True, (255, 255, 255)), ((2*x+w)/2-namelen,(2
    *y+h)/2-namelen))

def paused (My):
    pause = True
    while pause:
        rect("Menu", 50, 50, 550, 450,black)
        rect("Go On", 150, 400, 100, 50, green)
        rect("Quit",400, 400, 100, 50, red)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 150 < mouse[0] < 250 and 400 < mouse[1] < 450:
            if click[0]:
                pause = False
        if 400 < mouse[0] < 500 and 400 < mouse[1] < 450:
            if click[0]:
                record_myscore(My)
                pygame.quit()
                sys.exit()
        pygame.display.update()

def rank() :
    rank = True
    while rank:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        rect("", 50, 50, 550, 450, white)
        bg = pygame.image.load("Image/highest.png")
        screen.blit(bg, (100, 70))
        rect("menu", 275, 420, 100, 50, green)
        b = ranklist()
        for pos, a in enumerate(b[:8]):
            font = pygame.font.Font(None, 22)
            screen.blit(font.render("name" + "               " + "score" + "               " + "HP", True, (0, 0, 0)), (200, 175))
            screen.blit(font.render(a[0] + "                " + str(a[1]) + "            " + a[2], True, (0, 0, 0)), (200, pos * 27 + 200))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 275 < mouse[0] < 375 and 420 < mouse[1] < 470:
            if click[0]:
                rank = False
        pygame.display.update()

def teach() :
    teach = True
    while teach:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        rect("", 50, 50, 550, 450, white)
        rect("menu", 275, 420, 100, 50, green)
        font = pygame.font.Font(None, 18)
        screen.blit(font.render("go up --------------> w", True, (0, 0, 0)), (250,100))
        screen.blit(font.render("go left ------------> a", True, (0, 0, 0)), (250,150))
        screen.blit(font.render("go right -----------> d", True, (0, 0, 0)), (250,200))
        screen.blit(font.render("go down ------------> s", True, (0, 0, 0)), (250,250))
        screen.blit(font.render("double bullets -----> l", True, (0, 0, 0)), (250,300))
        screen.blit(font.render("enemy slow down ----> k", True, (0, 0, 0)), (250,350))
        screen.blit(font.render("menu ---------------> Esc", True, (0, 0, 0)), (250,400))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 275 < mouse[0] < 375 and 420 < mouse[1] < 470:
            if click[0]:
                teach = False
        pygame.display.update()

def start() :
    stop = True
    while stop:
        bg = pygame.image.load("Image/menu.jpg")
        screen.blit(bg, (0, 0))
        ti = pygame.image.load("Image/name.png")
        screen.blit(ti, (250, 300))
        rect("Start", 275, 370, 100, 50, green)
        rect("Record",550, 400, 100, 50, blue)
        rect("Help",0, 400, 100, 50, blue)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 275 < mouse[0] < 375 and 370 < mouse[1] < 420:
            if click[0]:
                stop = False
        if 550 < mouse[0] < 650 and 400 < mouse[1] < 450:
            if click[0]:
                rank()
        if 0 < mouse[0] < 100 and 400 < mouse[1] < 450:
            if click[0]:
                teach()
        pygame.display.update()

def failed (My):
    failed = True
    while failed:
        bgfailed = pygame.image.load("Image/GameOver.png")
        screen.blit(bgfailed, (0, 0))
        rect("Quit",150, 400, 100, 50, red)
        rect("Rank",400, 400, 100, 50, blue)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 150 < mouse[0] < 250 and 400 < mouse[1] < 450:
            if click[0]:
                record_myscore(My)
                pygame.quit()
                sys.exit()
        if 400 < mouse[0] < 500 and 400 < mouse[1] < 450:
            if click[0]:
                rank()
        pygame.display.update()

def win (My):
    win = True
    while failed:
        bgwin = pygame.image.load("Image/win.jpg")
        screen.blit(bgwin, (0, 0))
        rect("Quit",100, 450, 100, 50, red)
        rect("Rank",450, 450, 100, 50, blue)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 100 < mouse[0] < 200 and 450 < mouse[1] < 500:
            if click[0]:
                record_myscore(My)
                pygame.quit()
                sys.exit()
        if 450 < mouse[0] < 550 and 450 < mouse[1] < 500:
            if click[0]:
                rank()
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    start()
    paused()
    failed()
    rank()
    teach()