import pygame
from Bricks import *
from Scenes import *
from Shared import *
import Ball
import Pad
import Highscore
import Assests
from Shared import GameConstants
from Level import Level
class Breakout:

    def __init__(self):
        self.__lives = 5
        self.__score = 0
        self.__level = Level()

    def start(self):
        pass

    def changeScenes(self, scene):
        pass

    def getLevel(self):
        pass

    def getScore(self):
        pass

    def IncreaseScore(self, score):
        pass

    def getLives(self):
        pass

    def getBalls(self):
        pass

    def getPad(self):
        pass 
 
    def playSound(self, soundClip):
        pass

    def reduceLives(self):
        pass
    
    def increaseLives(self):
        pass

    def reset(self):
        pass

Breakout().start()

