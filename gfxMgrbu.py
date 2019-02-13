#Travis Walker and Shawn White
import os

import ogre.renderer.OGRE as ogre

class GfxMgr:

    def __init__(self,engine):
        self.engine = engine
        self.entityMgr = engine.entityMgr
        self.config = ""
        self.plugins = os.path.join(self.config,"plugins.cfg")
        self.resources = os.path.join(self.config, "resources.cfg")
        self.renderWindow = None

    def init(self):
        self.root = ogre.Root(self.plugins)
        self.defineResources()
        self.setupRenderSystem()
        self.createRenderWindow()
        self.initializeResourceGroups()
        self.setupScene()
        self.showHUD()

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
            self.camYawNode1 = self.sceneManager.getRootSceneNode().createChildSceneNode("CamNode1", (-2000, 5000, -2500))
            self.camYawNode1.yaw(ogre.Degree(0))
            self.camPitchNode1 = self.camYawNode1.createChildSceneNode("PitchNode1")
            self.camPitchNode1.attachObject(self.camera1)
            self.camPitchNode1.pitch(ogre.Degree(-90))
            self.camera1.lookAt = (0, 0, 0)


            self.camera2 = self.sceneManager.createCamera('camera2')
            self.camera2.nearClipDistance = 10
            self.camYawNode2 = self.sceneManager.getRootSceneNode().createChildSceneNode("CamNode2", (2000, 5000, 2500))
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
        self.life = self.overlayManager.getByName("GUI/Lifebar")
        self.weapons = self.overlayManager.getByName("GUI/Weapons")
        self.frame = self.overlayManager.getByName("GUI/myFrame")

        self.selectedWeaponIndex = 0
        self.weaponArr = []
        self.weaponArr.append(self.overlayManager.getOverlayElement("GUI/Weapons/gun"))

    def showHUD(self):
        self.life.show()
        self.weapons.show()
        self.frame.show()

    def tick(self, dtime):
        self.root.renderOneFrame()

    def stop(self):
        pass
    
