
import time
import sys
import pygame
from random import randint 

#initialize pygame
pygame.init()

#create the screen and set caption
WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("CS term 3 first project")

#color
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
RED=(255, 0, 0)
BLUE=(0, 0, 255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
CYAN=(0,255,255)
ORANGE=(255,165,0)
PURPLE=(128,0,128)

clock=pygame.time.Clock() #control the FPS
font=pygame.font.Font(None, 30)
big_font=pygame.font.Font(None, 50)

running=True

kris = pygame.image.load("assets/kris.png").convert()
susie = pygame.image.load("assets/susie.png").convert()


while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running=False
    screen.fill(WHITE) #fill the background with white color
    screen.blit(kris,(0,0))

    

















    pygame.display.update()
pygame.quit()


 