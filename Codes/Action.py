import pygame
def Action(event, Player):
    if event.key == pygame.K_s:
        Player.GoDown()
    if event.key == pygame.K_w:
        Player.GoUp()
    if event.key == pygame.K_a:
        Player.GoLeft()
    if event.key == pygame.K_d:
        Player.GoRight()
    if event.key == pygame.K_SPACE:
        Player.Shoot()
    if event.key == pygame.K_b:
        Player.BigBoom()  #use bombs to clean up all the enemies, bombs can be collected from parachutes
  

if __name__ == "__main__":
    Action()

