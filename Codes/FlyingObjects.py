import pygame
from Action import Action
import random as r
from random import randint
from math import ceil

class FlyingObjects:
    def __init__(self, sizescreen):
        self.screensize = sizescreen

    def GoDown(self):
        if self.position[1] + self.speed[1] <= self.screensize.height - self.rect.height:
            self.position[1] += self.speed[1]

    def GoUp(self):
        if self.position[1] - self.speed[1] >= 0:
            self.position[1] -= self.speed[1] 

    def GoRight(self):
        if self.position[0] + self.speed[0] <= self.screensize.width - self.rect.width:
            self.position[0] += self.speed[0]

    def GoLeft(self):
        if self.position[0] - self.speed[0] >= 0:
            self.position[0] -= self.speed[0]
    def damage(self):
        self.life -= 1

class Player(FlyingObjects):
    sensitivity = 5
    interval = 10

    def __init__(self, myrect, screensize, sx = 10, sy = 10):
        FlyingObjects.__init__(self, screensize)
        self.rect = myrect
        self.position = [screensize.width//2 - self.rect.width//2, screensize.height-self.rect.height]
        self.speed = sx, sy
        self.life = 20
        self.score = 0
        self.bullet_direction = -self.speed[1]

class Enemy(FlyingObjects):
    def __init__(self, E_image, position, screensize):
        FlyingObjects.__init__(self, screensize)
        self.position = position[:]
        self.size = [50, 50]
        self.life = 1
        self.speed =  [0, 10]
        self.bullet_direction = self.speed[1] // 2
        self.image = pygame.image.load(E_image)
        self.image = pygame.transform.rotate(self.image, 180)
        delta = r.randint(2,20)
        self.image =pygame.transform.scale(self.image,(50 + delta, 50 + delta))
        self.rect = self.image.get_rect()
        self.value = 100 + delta
        self.speed[1] = ceil(self.speed[1] / delta)

class Boss(FlyingObjects):
    def __init__(self , B_image ,position , screensize):
        FlyingObjects.__init__(self,screensize)
        self.position = position[:]
        # Once Enemy was shot by player's bullet, it will die
        self.size = [50,50]
        self.life = 5
        self.speed =  [0, 1]
        self.bullet_direction = 10 // 2
        self.image = pygame.image.load(B_image)
        self.value = 1000
        self.rect = self.image.get_rect()


class bullet(FlyingObjects):
    def __init__(self, position, forward, screensize, type = 0):
        FlyingObjects.__init__(self, screensize)
        self.position = position[:]
        self.life = 1
        self.speed =  [0, forward]
        
        self.image = pygame.image.load('Image/Bul.png')
        if type == 0: 
            pass
        if type == 1:
            self.image = pygame.image.load('Image/Bluebullet.png')

        if forward < 0:
            self.image = pygame.transform.rotate(self.image, 360 - 45)
        elif forward > 0:
            self.image = pygame.transform.rotate(self.image, 360 - 45 - 180)
            
        self.image =pygame.transform.scale(self.image, (20 , 20))
        self.rect = self.image.get_rect()
        
class Supply(FlyingObjects):
    def __init__(self, position, screensize):
        self.image = pygame.transform.scale(pygame.image.load('Image/gift.png'), (50, 50))
        FlyingObjects.__init__(self, screensize)
        self.position = position[:]
        self.speed = [0,1]
        self.rect = self.image.get_rect()


def Class_test():
    clock = pygame.time.Clock()
    Player_Image_Path = "Image/Plane_W.png"

    bg=pygame.image.load("Image/backgroundstar.jpg")
    Myimage = pygame.image.load(Player_Image_Path)
    Myimagesize = Myimage.get_rect()[2:]

    screensize = bg.get_rect()[2], bg.get_rect()[2]
    screen = pygame.display.set_mode(screensize)

    My = Player(Myimage.get_rect(), Myimagesize, screensize)
    print(Myimage.get_rect().width)
    running = True
    while running:
        # Load background image
        screen.blit(bg,(0, 0))

        # Allow User to move the plane countinuously by holding the key
        pygame.key.set_repeat(My.sensitivity, My.interval)

        # Get action from the KeyBooard
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                Action(event, My)
            
        # Load User plane
        screen.blit(Myimage, My.position)

        # Display
        pygame.display.flip()

        # FPS = 200
        # clock.tick(200)



if __name__ == '__main__':
    Class_test()