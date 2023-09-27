from os import execve
import pygame
import sys


pygame.init()

size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("AliveText Demo")

bg = (0, 0, 0)

font = pygame.font.Font(None, 20)
screen.fill(bg)


def live_text_test():
    Player_Image_Path = "plane_white.png"
    Myimage = pygame.image.load(Player_Image_Path)
    Myimagesize = Myimage.get_rect()[2:]
    My = Player(Myimagesize, size)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    My.damage()

            screen.fill(bg)
            screen.blit(font.render(str(My.life), True, (0, 255, 0)), (580, 0))


        pygame.display.flip()

if __name__ == '__main__':
    live_text_test()
