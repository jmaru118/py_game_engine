import pygame
from pygame.locals import *

class sound:
    def __init__(self, engine):
        self.engine = engine

    def bgm(self):
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.load("bass.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1.0)

    def init(self):
        pygame.init()
        self.shot = pygame.mixer.Sound("shot.wav")
        self.footStep = pygame.mixer.Sound("step.wav")
        self.bump = pygame.mixer.Sound("bump.wav")
        self.intro = pygame.mixer.Sound("intro.wav")
        self.enemyDeath = pygame.mixer.Sound("endeath.wav")
        self.playerDeath = pygame.mixer.Sound("pdeath.wav")

    def playIntro(self):
        self.intro.play()
        
    def playBump(self):
        #if not pygame.mixer.get_busy():
            self.bump.play()

    def playShot(self):
        self.shot.play()

    def playFootStep(self):
        if not pygame.mixer.get_busy():
            self.footStep.play()

    def playEnemyDeath(self):
        self.enemyDeath.play()

    def playPlayerDeath(self):
        self.playerDeath.play()

    def tick(self, dtime):
        pass


# add this into the engine.py init()
   #     import soundMgr
    #    self.soundMgr = soundMgr.sound(self)
     #   self.soundMgr.init()
      #  self.soundMgr.bgm()
