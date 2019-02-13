#Travis Walker and Shawn White
import os
import time
import ogre.renderer.OGRE as ogre
import pygame

class GfxMgr:

    def __init__(self,engine):
        self.engine = engine
        self.entityMgr = engine.entityMgr
        self.config = ""
        self.plugins = os.path.join(self.config,"plugins.cfg")
        self.resources = os.path.join(self.config, "resources.cfg")
        self.renderWindow = None

    def init(self):
        self.clock = 0
        self.root = ogre.Root(self.plugins)
        self.defineResources()
        self.setupRenderSystem()
        self.createRenderWindow()
        self.initializeResourceGroups()
        self.setupScene()
        self.startTime = time.time()
        self.endTime = self.startTime + 8
        self.scoreVal = 0
        self.showHUD()
        self.overlay()


    def defineResources(self):
        cf = ogre.ConfigFile()
        cf.load(self.resources)
        seci = cf.getSectionIterator()
        while seci.hasMoreElements():
            secName = seci.peekNextKey()
            settings = seci.getNext()
            
            for item in settings:
                typeName = item.key
                archName = item.value
                ogre.ResourceGroupManager.getSingleton().addResourceLocation(archName, typeName, secName)

    def setupRenderSystem(self):
        if not self.root.restoreConfig() and not self.root.showConfigDialog():
            raise Exception("User canceled the config dialog -> Application.setupRenderSystem()")


    def createRenderWindow(self):
        self.root.initialise(True, "Tutorial Render Window")
        self.renderWindow = self.root.getAutoCreatedWindow()
 

    def initializeResourceGroups(self):
        ogre.TextureManager.getSingleton().setDefaultNumMipmaps(5)
        ogre.ResourceGroupManager.getSingleton().initialiseAllResourceGroups()
 

    def setupScene(self):

        self.sceneManager = self.root.createSceneManager(ogre.ST_GENERIC, "Default SceneManager")
        self.createCameras()
        viewPort1 = self.root.getAutoCreatedWindow().addViewport(self.camera1,0,0,0,.5,1)
	viewPort2 = self.root.getAutoCreatedWindow().addViewport(self.camera2,1,.5,0,.5,1)
        self.createScene()
        print "\n\n setupScene \n\n"
        
    def createCameras(self):
            self.camera1 = self.sceneManager.createCamera('camera1')
            self.camera1.nearClipDistance = 10
            self.camYawNode1 = self.sceneManager.getRootSceneNode().createChildSceneNode("CamNode1", (-2000, 3200, -2500))
            self.camYawNode1.yaw(ogre.Degree(0))
            self.camPitchNode1 = self.camYawNode1.createChildSceneNode("PitchNode1")
            self.camPitchNode1.attachObject(self.camera1)
            self.camPitchNode1.pitch(ogre.Degree(-90))
            self.camera1.lookAt = (0, 0, 0)


            self.camera2 = self.sceneManager.createCamera('camera2')
            self.camera2.nearClipDistance = 10
            self.camYawNode2 = self.sceneManager.getRootSceneNode().createChildSceneNode("CamNode2", (2000,3200, 2500))
            self.camYawNode2.yaw(ogre.Degree(0))
            self.camPitchNode2 = self.camYawNode2.createChildSceneNode("PitchNode2")
            self.camPitchNode2.attachObject(self.camera2)
            self.camPitchNode2.pitch(ogre.Degree(-90))
            self.camera2.lookAt = (0, 0, 0)

    def createScene(self):
        sceneManager = self.sceneManager
        sceneManager.ambientLight = 1, 1, 1
 

        plane = ogre.Plane ((0, 1, 0), 0)
        meshManager = ogre.MeshManager.getSingleton ()
        meshManager.createPlane ('Ground', 'General', plane,
                                     10000, 10000, 20, 20, True, 1, 5, 5, (0, 0, 1))
        
        ent = sceneManager.createEntity('GroundEntity', 'Ground')
        sceneManager.getRootSceneNode().createChildSceneNode ().attachObject (ent)
        ent.setMaterialName ('Examples/Rockwall')
        ent.castShadows = False

        # draw HUD
        # Menu
        self.overlayManager = ogre.OverlayManager.getSingleton() 

        # HUD
        self.weapons = self.overlayManager.getByName("GUI/Weapons")
        self.frame = self.overlayManager.getByName("GUI/myFrame")

        self.selectedWeaponIndex = 0
        self.weaponArr = []
        self.weaponArr.append(self.overlayManager.getOverlayElement("GUI/Weapons/gun"))

    def showHUD(self):
        self.weapons.hide()
        self.frame.show()

    def overlay(self):
       self.overlayManager = ogre.OverlayManager.getSingleton() 
       self.shipInfoOverlay = self.overlayManager.getByName("Example/DynTexOverlay")
       self.shipInfoOverlay.show()

       self.overlayContainer = self.overlayManager.createOverlayElement("Panel", "ECSLENT/ShipInfoPanel")
       self.overlayContainer.setMetricsMode(ogre.GMM_PIXELS)
       self.overlayContainer.setPosition(10, 10)
       self.overlayContainer.setDimensions(500, 100)
    
       self.scoreText  = self.overlayManager.createOverlayElement("TextArea", "Score")
       self.scoreText.setMetricsMode(ogre.GMM_PIXELS)
       self.scoreText.setCaption("P1: ")
       self.scoreText.setPosition(5, 5)
       self.scoreText.setDimensions(500, 20)
       self.scoreText.setFontName("BlueHighway")
       self.scoreText.setCharHeight(20)
       self.scoreText.setColourTop((1.0, 1.0, 0.7))
       self.scoreText.setColourBottom((1.0, 1.0, 0.7))

       self.scoreValText  = self.overlayManager.createOverlayElement("TextArea", "ScoreVal")
       self.scoreValText.setMetricsMode(ogre.GMM_PIXELS)
       self.scoreValText.setCaption(str(0))
       self.scoreValText.setPosition(55, 5)
       self.scoreValText.setDimensions(500, 20)
       self.scoreValText.setFontName("BlueHighway")
       self.scoreValText.setCharHeight(20)
       self.scoreValText.setColourTop((1.0, 0.7, 0.7))
       self.scoreValText.setColourBottom((1.0, 1.0, 0.7))

       self.scoreTwoText  = self.overlayManager.createOverlayElement("TextArea", "ScoreTwo")
       self.scoreTwoText.setMetricsMode(ogre.GMM_PIXELS)
       self.scoreTwoText.setCaption("P2: ")
       self.scoreTwoText.setPosition(115, 5)
       self.scoreTwoText.setDimensions(500, 20)
       self.scoreTwoText.setFontName("BlueHighway")
       self.scoreTwoText.setCharHeight(20)
       self.scoreTwoText.setColourTop((1.0, 1.0, 0.7))
       self.scoreTwoText.setColourBottom((1.0, 1.0, 0.7))

       self.scoreTwoValText  = self.overlayManager.createOverlayElement("TextArea", "ScoreTwoVal")
       self.scoreTwoValText.setMetricsMode(ogre.GMM_PIXELS)
       self.scoreTwoValText.setCaption(str(0))
       self.scoreTwoValText.setPosition(165, 5)
       self.scoreTwoValText.setDimensions(500, 20)
       self.scoreTwoValText.setFontName("BlueHighway")
       self.scoreTwoValText.setCharHeight(20)
       self.scoreTwoValText.setColourTop((1.0, 0.7, 0.7))
       self.scoreTwoValText.setColourBottom((1.0, 1.0, 0.7))

       self.timerText  = self.overlayManager.createOverlayElement("TextArea", "Time")
       self.timerText.setMetricsMode(ogre.GMM_PIXELS)
       self.timerText.setCaption("Time: ")
       self.timerText.setPosition(5, 35)
       self.timerText.setDimensions(500, 20)
       self.timerText.setFontName("BlueHighway")
       self.timerText.setCharHeight(20)
       self.timerText.setColourTop((1.0, 1.0, 0.7))
       self.timerText.setColourBottom((1.0, 1.0, 0.7))

       self.clockText  = self.overlayManager.createOverlayElement("TextArea", "Clock")
       self.clockText.setMetricsMode(ogre.GMM_PIXELS)
       self.clockText.setCaption(str(self.clock))
       self.clockText.setPosition(55, 35)
       self.clockText.setDimensions(500, 20)
       self.clockText.setFontName("BlueHighway")
       self.clockText.setCharHeight(20)
       self.clockText.setColourTop((1.0, 0.7, 0.7))
       self.clockText.setColourBottom((1.0, 1.0, 0.7))

       self.overlayContainer.addChild(self.scoreText)
       self.overlayContainer.addChild(self.timerText)
       self.overlayContainer.addChild(self.clockText)
       self.overlayContainer.addChild(self.scoreValText)
       self.overlayContainer.addChild(self.scoreTwoValText)
       self.overlayContainer.addChild(self.scoreTwoText)
       self.scoreValText.show()
       self.scoreText.show()
       self.scoreTwoText.show()
       self.scoreTwoValText.show()
       self.timerText.show()
       self.clockText.show()
       self.shipInfoOverlay.add2D(self.overlayContainer)
       self.overlayContainer.show()


    def updateTime(self):
        self.clock = int(self.endTime - time.time())
        self.clockText.hide()
        self.clockText.setCaption(str(self.clock))
        self.clockText.show()

    def updateScore(self):
        self.scoreValText.hide()
        self.scoreValText.setCaption(str(self.engine.entityMgr.entities[0].score))
        self.scoreValText.show()

        self.scoreTwoValText.hide()
        self.scoreTwoValText.setCaption(str(self.engine.entityMgr.entities[1].score))
        self.scoreTwoValText.show()

    def tick(self, dtime):
        self.root.renderOneFrame()
        self.updateTime()
        self.updateScore()
        if self.clock <= 0:
            print "player 1 score: " + str(self.engine.entityMgr.entities[0].score)
            print "player 2 score: " + str(self.engine.entityMgr.entities[1].score)
            if self.engine.entityMgr.entities[0].score > self.engine.entityMgr.entities[1].score:
                print "Player 1 wins"
                self.engine.stop(1)
            else:
                print "Player 2 wins"
                self.engine.stop(2)
            #self.engine.stop()


    def stop(self):
        pass
    
