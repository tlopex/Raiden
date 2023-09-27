from FlyingObjects import Enemy, bullet, Supply, Boss
from random import randint
from Collide import collide_check

def enemygenerator(Es, Ebo, screensize):
    upper_bound = 10
    if len(Es) <= upper_bound:
        while True:
            x, y = randint(50, screensize.width - 50), randint(0, screensize.height//3)
            newenemy = Enemy("Image/战斗机2.png", [x, y], screensize)
            if collide_check(Es, newenemy) == False and collide_check(Ebo, newenemy) == False:
                break

        Es.append(newenemy)

def bossgenerator(Es, Ebo, screensize):
    while True:
        x, y = randint(50, screensize.width - 50), randint(0, screensize.height//5)
        newboss=Boss("Image/boss.png",[x,y],screensize)
        if(collide_check(Ebo, newboss) == False and collide_check(Es, newboss) == False):
            break
    Ebo.append(newboss)
    #print(1)


def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def bulletgenerator(buls, x, screensize, bullettype = 0, double = False):
    if double == False:
        newbullet = bullet([x.position[0], x.position[1] + int(sgn(x.bullet_direction)*x.rect.height // 2)], x.bullet_direction, screensize, type = bullettype)
        buls.append(newbullet)
    elif double == True:
        newbullet = bullet([x.position[0] - x.rect.width // 6, x.position[1] + int(sgn(x.bullet_direction)*x.rect.height // 2)], x.bullet_direction, screensize, type = bullettype)
        buls.append(newbullet)
        newbullet = bullet([x.position[0] + x.rect.width // 6, x.position[1] + int(sgn(x.bullet_direction)*x.rect.height // 2)], x.bullet_direction, screensize, type = bullettype)
        buls.append(newbullet)



def giftgenerator(Eg, screensize):
    if len(Eg) >= 1: 
        return False
        
    x, y = randint(50, screensize.width - 50), randint(0, 50)
    newGift = Supply([x, y], screensize)
    Eg.append(newGift)
    return True