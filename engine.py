# 381 main engine

class Engine(object):
    '''
    The root of the global manager tree
    '''

    def __init__(self):
        pass

    def init(self):
        import entityMgr
        self.entityMgr = entityMgr.EntityMgr(self)
        self.entityMgr.init()
        self.keepRunning = True;

        import gfxMgr
        self.gfxMgr = gfxMgr.GfxMgr(self)
        self.gfxMgr.init()

        import netMgr
        self.netMgr = netMgr.NetMgr(self)
        self.netMgr.init()

        import inputMgr
        self.inputMgr = inputMgr.InputMgr(self)
        self.inputMgr.init()

       # import selectionMgr
        #self.selectionMgr = selectionMgr.SelectionMgr(self)
        #self.selectionMgr.init()

        #import controlMgr
       # self.controlMgr = controlMgr.ControlMgr(self)
       # self.controlMgr.init()


        import gameMgr
        self.gameMgr = gameMgr.GameMgr(self)
        self.gameMgr.init()
        self.inputMgr.initP()

        import soundMgr
        self.soundMgr = soundMgr.sound(self)
        self.soundMgr.init()
        self.soundMgr.bgm()

        import collisionMgr
        self.collisionMgr = collisionMgr.collisionMgr(self)
        self.collisionMgr.init()


    def stop(self, winner):
        self.winner = winner
        self.gfxMgr.stop()
        self.inputMgr.stop()
        #self.selectionMgr.stop()
        self.gameMgr.stop()
       # self.controlMgr.stop()
        self.netMgr.stop()
        self.collisionMgr.stop()
        self.endScreen(0)
        self.keepRunning = False
        self.endScreen(winner)

    def run(self):
        import time
        import ogre.renderer.OGRE as ogre
        weu = ogre.WindowEventUtilities() # Needed for linux/mac
        weu.messagePump()                 # Needed for linux/mac

        self.oldTime = time.time()        
        self.runTime = 0
        while (self.keepRunning):
            now = time.time() # Change to time.clock() for windows
            dtime = now - self.oldTime
            self.oldTime = now

            self.entityMgr.tick(dtime)
            self.gfxMgr.tick(dtime)
            self.netMgr.tick(dtime)
            self.inputMgr.tick(dtime)
           # self.selectionMgr.tick(dtime)
           # self.controlMgr.tick(dtime)
            self.gameMgr.tick(dtime)
            self.collisionMgr.tick(dtime)
            
            self.runTime += dtime
        
            weu.messagePump()             # Needed for linux/mac
            time.sleep(0.001)

        print "381 Engine exiting..."

    def endScreen(self, winner):
        import pygame
        pygame.init()
        print(winner)

        if winner == 1:
            self.screen = pygame.display.set_mode()
            pygame.display.set_caption("118 Studios")
            self.img=pygame.image.load("p1win.jpg") 
            self.screen.blit(self.img,(0,0))
            pygame.display.update()
            pygame.display.flip()
            pygame.time.wait(7000)
        elif winner == 2:
            screen = pygame.display.set_mode()
            pygame.display.set_caption("118 Studios")
            img=pygame.image.load("p2win.jpg") 
            screen.blit(img,(0,0))
            pygame.display.update()
            pygame.display.flip()
            pygame.time.wait(7000)
        elif winner == 0:
            pass



        pygame.quit()