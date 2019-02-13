#Travis Walker and Shawn White
import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
from gamepad import GamePad

class InputMgr(OIS.KeyListener, OIS.MouseListener, OIS.JoyStickListener):

    def __init__(self, engine):
        self.engine = engine
        OIS.KeyListener.__init__(self)
        OIS.MouseListener.__init__(self)
        self.sceneManager = engine.gfxMgr.sceneManager
        self.transVector = ogre.Vector3(0, 0, 0)
        self.camVector = ogre.Vector3(0, 0, 0)
        self.toggle = 0.1
        self.rotate = 0.005
        self.yaw = 0.0
        self.pitch = 0.0
        self.move = 500
        self.entites = engine.entityMgr.entities
        self.bToggle= True
        print " InputMgr init"
        
    def init(self):
        import soundMgr
        self.soundMgr = soundMgr.sound(self)
        self.soundMgr.init()
        self.soundMgr.playIntro()
        print " InputMgr2 init"
        windowHandle = 0
        
        renderWindow = self.engine.gfxMgr.root.getAutoCreatedWindow()
        print " InputMgr3 init"
        windowHandle = renderWindow.getCustomAttributeUnsignedLong("WINDOW")
        print " InputMgr3 init"
        paramList = [("WINDOW", str(windowHandle))]
        self.inputManager = OIS.createPythonInputSystem(paramList)
        self.keyboard = None
        self.mouse = None
	self.gamepad = None
        print " InputMgr4 init"

        try:
           
           self.keyboard = self.inputManager.createInputObjectKeyboard(OIS.OISKeyboard, False)
           self.mouse = self.inputManager.createInputObjectMouse(OIS.OISMouse, False)
	  # self.gamepad = self.inputManager.createInputObjectJoyStick(OIS.OISJoyStick, False)

        except Exception, e:
            raise e
	#self.gamepad.setEventCallback(self) 
        self.mouse.setEventCallback(self)
        self.keyboard.setEventCallback(self) 

        self.camYawNode1 = self.engine.gfxMgr.camYawNode1
        self.camPitchNode1 = self.engine.gfxMgr.camPitchNode1
        self.camera1 = self.engine.gfxMgr.camera1

       	self.camYawNode2 = self.engine.gfxMgr.camYawNode2
        self.camPitchNode2 = self.engine.gfxMgr.camPitchNode2
        self.camera2 = self.engine.gfxMgr.camera2
        print " InputMgr still working?"
    def initP(self):
        self.player1 = self.engine.gameMgr.player1
	self.player2 = self.engine.gameMgr.player2
        self.player1node=self.player1.node
	self.player2node=self.player2.node

    def tick(self, dtime):
        self.keyboard.capture() 
        self.mouse.capture()
        if not self.checkCollisionP1():
            self.keyPressed(dtime)

        self.currMouse = self.mouse.getMouseState()


        self.camYawNode1.yaw(ogre.Radian(-self.yaw))
        self.camPitchNode1.pitch(ogre.Radian(self.pitch))

            

        
        # Translate the camera based on time.
        self.player1node.translate(self.player1node.orientation
                              * self.transVector
                              * dtime )
        self.player1.pos += (self.player1node.orientation
                              * self.transVector
                              * dtime )
        self.camYawNode1.translate(self.camYawNode1.orientation
                              * self.camVector
                              * dtime )
        
        if self.checkCollisionP1():
            self.player1node.translate(self.player1node.orientation
                              * -self.transVector*1.2
                              * dtime )
            self.player1.pos += (self.player1node.orientation
                              * -self.transVector*1.2
                              * dtime )
            
            self.camYawNode1.translate(self.camYawNode1.orientation
                              * -self.camVector*1.2
                              * dtime )
        


        self.player2node.translate(self.player2node.orientation
                              * -self.transVector
                              * dtime )
        self.player2.pos += (self.player2node.orientation
                              * -self.transVector
                              * dtime )

        self.camYawNode2.translate(self.camYawNode1.orientation
                              * -self.camVector
                             * dtime )
                
        if self.checkCollisionP2():
            self.player2node.translate(self.player2node.orientation
                              * self.transVector*1.2
                              * dtime )
            self.player2.pos += (self.player2node.orientation
                              * self.transVector*1.2
                              * dtime )
            
            self.camYawNode2.translate(self.camYawNode1.orientation
                              * self.camVector*1.2
                              * dtime )
            

        

    def keyPressed(self, frameEvent):
        #print "in keypressed funtion"

        # Move the camera using keyboard input.
        self.transVector = ogre.Vector3(0, 0, 0)
        self.camVector = ogre.Vector3(0, 0, 0)
        # Move Forward.
        if self.keyboard.isKeyDown(OIS.KC_W):
            self.transVector.z -= self.move
            self.camVector.z -= self.move
            self.soundMgr.playFootStep()
        # Move Backward.
        if self.keyboard.isKeyDown(OIS.KC_S):
            self.transVector.z += self.move
            self.camVector.z += self.move
            self.soundMgr.playFootStep()
        # Strafe Left.
        if self.keyboard.isKeyDown(OIS.KC_A):
            self.transVector.x -= self.move
            self.camVector.x -= self.move
            self.soundMgr.playFootStep()
        # Strafe Right.
        if self.keyboard.isKeyDown(OIS.KC_D):
            self.transVector.x += self.move
            self.camVector.x += self.move
            self.soundMgr.playFootStep()

       #	if self.keyboard.isKeyDown(OIS.KC_Q):
        #    self.yaw = -self.rotate
 
        #elif self.keyboard.isKeyDown(OIS.KC_E):
         #   self.yaw = self.rotate
        #else:
          #  self.yaw = 0
            
        #if self.keyboard.isKeyDown(OIS.KC_Z):
       #     self.pitch = self.rotate
        #elif self.keyboard.isKeyDown(OIS.KC_X):
         #   self.pitch = -self.rotate 
        #else:
         #   self.pitch = 0
         
        # Move Up.        
        if self.keyboard.isKeyDown(OIS.KC_PGUP):
            self.camVector.y += self.move
        # Move Down.
        if self.keyboard.isKeyDown(OIS.KC_PGDOWN):
            self.camVector.y -= self.move

        if self.keyboard.isKeyDown(OIS.KC_SPACE) and self.bToggle:
            self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[1], pos = self.player1.pos+ogre.Vector3(150, 0, 0))
            self.soundMgr.playShot()
            self.bToggle= False
            
        if not self.keyboard.isKeyDown(OIS.KC_SPACE):
            self.bToggle= True

        if self.keyboard.isKeyDown(OIS.KC_ESCAPE):
            print "escape key pressed"
            self.engine.stop()
        
        return not self.keyboard.isKeyDown(OIS.KC_ESCAPE)

    def keyReleased(self, frameEvent):
        return True

    def mouseMoved(self, frameEvent):
        return True
 
    def mousePressed(self, frameEvent, id):
        if id == OIS.MB_Left:
            self.mouseSelectEntity()
        return True
 
    def mouseReleased(self, frameEvent, id):
        return True


    def stop(self):
        pass

    
    def mouseSelectEntity(self):
        self.mouse.capture()
        self.currMouse = self.mouse.getMouseState()

        if not self.shiftKeyDown:
            for ent in self.engine.entityMgr.selectedEntities:
                ent.node.showBoundingBox(False)
                self.engine.entityMgr.selectedEntities = []
        
        pos, ents = self.castRay(self.currMouse)

        for ent in ents:
            self.engine.entityMgr.selectedEntities.append(ent)
            ent.node.showBoundingBox(True)


    def castRay(self, currMouse):
        currMouse.width = self.engine.gfxMgr.renderWindow.getWidth()
        currMouse.height = self.engine.gfxMgr.renderWindow.getHeight()
        mouseRay = self.engine.gfxMgr.camera.getCameraToViewportRay(currMouse.X.abs/float(currMouse.width), 
                                                                    currMouse.Y.abs/float(currMouse.height))
        result  =  mouseRay.intersects(self.engine.gfxMgr.waterPlane)        

        if result.first:
            pos =  mouseRay.getPoint(result.second)
            return self.checkForEntsInRadius(pos, 23000)


    def checkForEntsInRadius(self, pos, radiusSquared):
        entities = []
        #for name, ent in self.engine.entityMgr.entities.iteritems():
        for ent in self.engine.entityMgr.entities.values():
            dist = ent.pos.squaredDistance(pos)
            if dist < radiusSquared:
                entities.append(ent)
        return (pos, entities)

    
    def checkCollisionP1(self):
        for Entity in self.entites:
            if self.entites[Entity].uiname is not self.player1.uiname:
                if self.player1.box.intersects(self.entites[Entity].box):
                    self.soundMgr.playBump()
                    print "collision"
                    return True

        return False

    def checkCollisionP2(self):
        for Entity in self.entites:
            if self.entites[Entity].uiname is not self.player2.uiname:
                if self.player2.box.intersects(self.entites[Entity].box):
                    self.soundMgr.playBump()
                    return True

        return False

        
