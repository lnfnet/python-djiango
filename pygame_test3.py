#! /usr/bin/env python3

import pygame
from pygame.locals import *
from pygame.event import *
import time
import sys

pygame.init()

ScreenSize=(1000,700)
GameScreen=pygame.display.set_mode(ScreenSize)

black=0,0,0
white=255,255,255
blue=0,0,255
red=255,0,0
green=0,255,0
RazPiRed=210,40,82

DefaultFont = None
GameFont=pygame.font.Font(DefaultFont,60)
GameText="I love my Raspberry Pi"
GameTextGraphic=GameFont.render(GameText,True,white)

GameScreen.fill(RazPiRed)
GameScreen.blit(GameTextGraphic,(100,100))
pygame.display.update()


#time.sleep(10)

#GameImage="C:\\Users\\lnf\\Pictures\\1.jpg"
#GameImageGraphic=pygame.image.load(GameImage).convert()
#GameImageLocation=GameImageGraphic.get_rect()
#############################################
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
        else:
            print("Game coming....")
