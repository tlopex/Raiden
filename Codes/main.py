from typing import Sized
import pygame
import time as systime
from Record_MyScore import record_myscore
# from gifts import gift
# from gifts import collide_gift
from Collide import collide

import sys

from pygame.constants import RESIZABLE
from Pause import paused
from Pause import start
from Pause import failed
from Pause import win
from FlyingObjects import Enemy,Player,bullet
from Pause import failed
from Action import Action
from random import randint
from Generator import enemygenerator, bulletgenerator, giftgenerator,bossgenerator

pygame.init()

# -------- Create ScreenSize
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
size = pygame.Rect(0, 0, width, height)
screen = pygame.display.set_mode((width, height))
# -------- Create ScreenSize


# -------- File Path

# Images:
bg = "Image/backgroundstar.jpg"
MyPlane_image = "Image/战斗机 (1).png"
Gift_image_path = 'Image/gift123.png'
Boss_image = "Image/boss.png"

# Audios:
bgm = 'Audio/travel.mp3'
# -------- File Path


# -------- Load Images and Audios
pygame.display.set_caption("Mini Raiden")
icon=pygame.image.load("Image/cat.png")
pygame.display.set_icon(icon)
bg=pygame.image.load(bg)
pygame.mixer.music.load(bgm)
pygame.mixer.music.play(-1)
# -------- Load Images and Audios

font = pygame.font.Font(None, 20)

def main():
    My_image = pygame.transform.scale(pygame.image.load(MyPlane_image), (50, 50))
    My = Player(My_image.get_rect(), size)
    # Gift_image = pygame.transform.scale(pygame.image.load(Gift_image_path), (50, 50))

    # Following Lists are used to store different Units
    Es = [] # Enemies
    buls = [] # bullets of players
    Eg = [] # Gifts 
    Eb = [] # Enemies's bullets
    Ebo = [] # Boss
    doublebullet = 0 #bullet
    slowdown = 0 #slowdown
    doublebullet_start_time = 0
    slowdown_start_time = 0
    dk = 1
    
    vis = False
    start()
    time = 0
    running = True
    while running:
        time += 1

        if doublebullet_start_time > 0:
            if systime.process_time() - doublebullet_start_time > 3:
                vis = False
                doublebullet_start_time = 0
        if slowdown_start_time > 0:
            if systime.process_time() - slowdown_start_time > 3:
                dk = 1
                slowdown_start_time = 0

        if time % int(50 / dk) == 0:
            enemygenerator(Es, Ebo, size)
        if time % 10 == 0:
            bulletgenerator(buls, My, size, double = vis)
        if time % int(50 / dk) == 0:
            for each in Es:
                bulletgenerator(Eb, each, size)
            for each in Ebo:
                bulletgenerator(Eb, each, size, 1)
                
        if time %200 == 0:
            bossgenerator(Es, Ebo, size)
        if randint(1, 200) == 1 and len(Eg) == 0:
            giftgenerator(Eg, size)

        screen.blit(bg,(0,0))
        for each in Es:
            each.position[1] += each.speed[1]*dk
            if each.position[1] - each.rect.height > size.height:
                Es.remove(each)

        for each in Eg:
            each.position[1] += each.speed[1]
            if each.position[1] - each.rect.height > size.height:
                Eg.remove(each)
        
        for each in Ebo:
            each.position[1] += each.speed[1]*dk
            if each.position[1] - each.rect.height > size.height:
                Ebo.remove(each)
        
        for each in buls:
            each.position[1] += each.speed[1]
        for each in Eb:
            each.position[1] += each.speed[1]*dk

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused(My)
                   # print("in paused")
                pygame.key.set_repeat(My.sensitivity, My.interval)
                Action(event, My)
                if event.key == pygame.K_l:
                    if doublebullet_start_time <= 0 and doublebullet > 0:
                        doublebullet -= 1
                        vis=True  
                        doublebullet_start_time = systime.process_time()
                if event.key == pygame.K_k:
                    if slowdown_start_time <= 0 and slowdown > 0:
                        slowdown -= 1
                        dk=0.5
                        slowdown_start_time = systime.process_time()


            #buls.append(bullet())

        screen.blit(My_image, [My.position[0] - My.rect.width//2, My.position[1] - My.rect.height // 2])

        for E in Es:
            screen.blit(E.image, [E.position[0] - E.rect.width//2, E.position[1] - E.rect.height // 2])
        for B in buls:
            screen.blit(B.image, [B.position[0] - B.rect.width//2, B.position[1] - B.rect.height // 2])
        for G in Eg:
            screen.blit(G.image, [G.position[0] - G.rect.width//2, G.position[1] - G.rect.height // 2])
        for B in Eb:
            screen.blit(B.image, [B.position[0] - B.rect.width//2, B.position[1] - B.rect.height // 2])
        for Q in Ebo:
            '''if Q.life == 5:
                hp5 = pygame.image.load("Image/HPBar-5.png")
                screen.blit(hp5,[Q.position[0] - Q.rect.width//2, Q.position[1] - Q.rect.height // 2-50])
            if Q.life == 4:
                hp4 = pygame.image.load("Image/HPBar-4.png")
                screen.blit(hp4,[Q.position[0] - Q.rect.width//2, Q.position[1] - Q.rect.height // 2-50])
            if Q.life == 3:
                hp3 = pygame.image.load("Image/HPBar-3.png")
                screen.blit(hp3,[Q.position[0] - Q.rect.width//2, Q.position[1] - Q.rect.height // 2-50])
            if Q.life == 2:
                hp2 = pygame.image.load("Image/HPBar-2.png")
                screen.blit(hp2,[Q.position[0] - Q.rect.width//2, Q.position[1] - Q.rect.height // 2-50])
            if Q.life == 1:
                hp1 = pygame.image.load("Image/HPBar-1.png")
                screen.blit(hp1,[Q.position[0] - Q.rect.width//2, Q.position[1] - Q.rect.height // 2-50])'''
            
          # hp1 = pygame.transform.scale(pygame.image.load("Image/HPBar-1.png"), (200, 50))
          #  screen.blit(hp1,[Q.position[0] - Q.rect.width//2, Q.position[1] - Q.rect.height // 2-50])
            screen.blit(Q.image, [Q.position[0] - Q.rect.width//2, Q.position[1] - Q.rect.height // 2])

        if collide(Es, My):
            My.life -= 1
        if collide(Ebo, My):
            My.life -= 1
        if collide(Eg, My):
            z=randint(1,3)
            if z==1:
                My.life += 1
            elif z==2:
                slowdown += 1
            else:
                doublebullet += 1

        if collide(Eb, My):
            My.life -= 1

        for each in Es:
            if collide(buls, each):
                My.score += each.value
                Es.remove(each)
                if len(Eg) >= 1:
                    continue
                Gift = Enemy(Gift_image_path, each.position, each.screensize)
                if randint(1, 20) == 1:
                    Eg.append(Gift)
        for each in Ebo:
            if collide(buls, each):
                My.score += each.value
                each.life -= 1
                if each.life == 0:
                    Ebo.remove(each)
                if len(Eg) >= 1:
                    continue
                Gift = Enemy(Gift_image_path, each.position, each.screensize)
                if randint(1, 20) == 1:
                    Eg.append(Gift)
    
        screen.blit(font.render("HP: " + str(My.life), True, (0, 255, 0)), (560, 0))
        screen.blit(font.render("Score:" + str(My.score) + " !", True, (255, 0, 0)), (560, 20))
        screen.blit(font.render("Slow Down Available: (K) " + str(slowdown), True, (255, 255, 255)), (460, 480))
        screen.blit(font.render("Double Bullet Available: (L) " + str(doublebullet) , True, (255, 255, 255)), (460, 500))
        if slowdown_start_time > 0:
            screen.blit(font.render("X 0.5", True, (0, 255, 0)), (0, 20))
        if doublebullet_start_time > 0:
            screen.blit(font.render("Double", True, (0, 255, 0)), (0, 50))
        pygame.display.update()
        
        if My.life <= 0:
           failed(My)
        if My.score >= 200000 :
            win(My)

        pygame.time.Clock().tick(60)

    if running == False:
        record_myscore(My)
        
if __name__ == "__main__":
    main()