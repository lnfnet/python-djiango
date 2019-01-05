#!\usr\bin\env python3
import pygame
import random
import sys

from pygame.locals import *

pygame.init()


#Delete a Raspberry
def deleteRaspberry (RaspberryDict,RNumber):
    key1='RasLoc'+ str(RNumber)
    key2='RasOff'+ str(RNumber)

    NewRaspberry = dict(RaspberryDict)

    del NewRaspberry[key1]
    del NewRaspberry[key2]

    return NewRaspberry

#set up the game Screen

ScreenSize=ScreenWidth,ScreenHeight=1000,700
GameScreen=pygame.display.set_mode(ScreenSize)

blue=0,0,255

#set up the game image graphics

GameImage="1.jpg"
GameImageGrahic=pygame.image.load(GameImage).convert_alpha()
GameImageGrahic=pygame.transform.scale(GameImageGrahic,(75,75))
GameImageLocation=GameImageGrahic.get_rect()

#Starting speed
ImageOffset=[5,5]

#Buid the Raspberry Dictionary

RAmount =17 #Number of Raspberries on screen
Raspberry={} #初始化字典

for RNumber in range(RAmount):
    Position_x=(ImageOffset[0]+RNumber)*random.randint(9,29)
    Position_y=(ImageOffset[1]+RNumber)*random.randint(8,18)
    RasKey='RasLoc'+str(RNumber)
    Location=GameImageLocation.move(Position_x,Position_y)
    Raspberry[RasKey]=Location
    RasKey='RasOff'+str(RNumber)
    Raspberry[RasKey]=ImageOffset

#Setup Game Sound

# ClickSound=pygame.mixer.Sound()

#Play the Game

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for RNumber in range(RAmount):
                RasLoc = 'RasLoc'+str(RNumber)
                RasImageLoction=Raspberry[RasLoc]
                if RasImageLocation.collidepoint(pygame.mouse.get_pos()):
                    deleteRaspberry(Raspberry,RNumber)
                    RAmount=RAmount-1
                    #ClickSound.play()
                    pygame.time.delay(200)
                    if RAmount==0:
                        sys.exit()
    #Redraw the Screen Background
        GameScreen.fill(blue)

        #Move the Raspberries around the screen
        for RNumber in range(RAmount):
            RasLoc='RasLoc'+str(RNumber)
            RasImageLocation=Raspberry[RasLoc]
            RasOff='RasOff'+str(RNumber)
            RasImageOffset=Raspberry[RasOff]

            NewLocation=RasImageLocation.move(RasImageOffset)

            Raspberry[RasLoc] = NewLocation

    #Keep Raspberries on screen
        if NewLocation.left<0 or NewLocation.right>ScreenWidth:
            NewOffset = -RasImageOffset[0]
            if NewOffset<0:
                NewOffset=NewOffset-1
            else:
                NewOffset=NewOffset+1

            RasImageOffset=[NewOffset,RasImageOffset[1]]
            Raspberry[RasOff]=RasImageOffset #Update offset

        if NewLocation.top<0 or NewLocation.bottom>ScreenHeight:
            NewOffset=-RasImageOffset[1]
            if NewOffset<0:
                NewOffset=NewOffset-1
            else:
                NewOffset=NewOffset+1
                
            RasImageOffset=[NewOffset,RasImageOffset[1]]
            Raspberry[RasOff]=RasImageOffset #Update offset

        GameScreen.blit(GameImageGrahic,NewLocation)
        pygame.display.update()
