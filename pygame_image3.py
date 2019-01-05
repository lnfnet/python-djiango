#! /usr/bin/env python3

import pygame
import sys

from pygame.locals import *

ScreenSize=(1000,700)
GameScreen=pygame.display.set_mode(ScreenSize)

blue=0,0,255

GameImage="C:\\Users\\lnf\\Pictures\\1.jpg"
GameImageGraphic=pygame.image.load(GameImage).convert_alpha()

GameImageLocation=GameImageGraphic.get_rect()

GameScreen.fill(blue)
GameScreen.blit(GameImageGraphic,GameImageLocation)
    #update game screen
pygame.display.update()

ImageOffset=[10,10]

# ClickSound=pygame.mixer.sound("")


while True:
    for event in pygame.event.get():
        if event.type in (QUIT,MOUSEBUTTONDOWN):
            #clickSound.play()
            pygame.time.delay(300)
            sys.exit()
    #Move game image
    GameImageLocation=GameImageLocation.move(ImageOffset)
    #Draw screen images
    GameScreen.fill(blue)
    GameScreen.blit(GameImageGraphic,GameImageLocation)
    #update game screen
    pygame.display.update()
    pygame.time.delay(200) 
