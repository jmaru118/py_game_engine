#Travis Walker and Shawn White
import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import pygame.joystick as JoyStick
import pygame
import math
from pygame.locals import *

class InputMgr(OIS.KeyListener, OIS.MouseListener, OIS.JoyStickListener):

    def __init__(self, engine):
        self.engine = engine
        OIS.KeyListener.__init__(self)
        OIS.MouseListener.__init__(self)
        self.sceneManager = engine.gfxMgr.sceneManager
        self.transVector1 = ogre.Vector3(0, 0, 0)
        self.camVector1 = ogre.Vector3(0, 0, 0)
        self.transVector2 = ogre.Vector3(0, 0, 0)
        self.camVector2 = ogre.Vector3(0, 0, 0)
        self.toggle = 0.1
        self.rotate = 0.005
        self.yaw = 0.0
        self.pitch = 0.0
        self.move = 800
        self.entites = engine.entityMgr.entities
        self.bToggle1 = True
        self.bToggle2 = True
        self.p1bulletcount =0
        self.p2bulletcount =0
	self.p1checked = False
	self.p2checked = False
        self.p1stuckcheck = 0
        self.p2stuckcheck = 0

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
	JoyStick.init()
	self.joysticks = [JoyStick.Joystick(x) for x in range(JoyStick.get_count())]
	self.joysticks[0].init();
	self.joysticks[1].init();
        try:
           
           self.keyboard = self.inputManager.createInputObjectKeyboard(OIS.OISKeyboard, False)
           self.mouse = self.inputManager.createInputObjectMouse(OIS.OISMouse, False)

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
	self.bulletp1 = self.engine.gameMgr.bulletP1
	self.bulletp2 = self.engine.gameMgr.bulletP2

    def tick(self, dtime):
	#print "numbuttons :" + str(self.joysticks[0].get_numbuttons())


    





        if  not self.checkCollisionP1():
            
            self.transVector1 = ogre.Vector3(0, 0, 0)
            self.camVector1 = ogre.Vector3(0, 0, 0)

            self.movePlayer1()
        if not self.checkCollisionP2():

            self.transVector2 = ogre.Vector3(0, 0, 0)
            self.camVector2 = ogre.Vector3(0, 0, 0)
            self.movePlayer2()
        self.p2checked = True
        self.p1checked = True
        self.keyboard.capture() 
        self.camYawNode1.yaw(ogre.Radian(-self.yaw))
        self.camPitchNode1.pitch(ogre.Radian(self.pitch))


        pygame.event.get()
        
        self.keyPressed(dtime)

        self.player1node.translate(
                               self.transVector1
                              * dtime )
        self.player1.pos += (
                               self.transVector1
                              * dtime )
        self.camYawNode1.translate(
                               self.camVector1
                              * dtime )
        
        if self.checkCollisionP1():
            self.soundMgr.playBump()
            if self.transVector1 == ogre.Vector3(0,0,0):
                self.player1.kill()
            self.player1node.translate(
                               -self.transVector1*2
                              * dtime )
            self.player1.pos += (
                               -self.transVector1*2
                              * dtime )
            
            self.camYawNode1.translate(
                               -self.camVector1*2
                              * dtime )
        


        self.player2node.translate(
                               self.transVector2
                              * dtime )
        self.player2.pos += (
                              self.transVector2
                              * dtime )

        self.camYawNode2.translate(
                               self.camVector2
                             * dtime )
                
        if self.checkCollisionP2():
            self.soundMgr.playBump()
            if self.transVector2 == ogre.Vector3(0,0,0):
                self.player2.kill()
            self.player2node.translate(
                               -self.transVector2*2
                              * dtime )
            self.player2.pos += (
                               -self.transVector2*2
                              * dtime )
            
            self.camYawNode2.translate(
                               -self.camVector2*2
                              * dtime )
        self.p1checked = False
        self.p2checked = False
            

    def movePlayer1(self):
        ax0 = self.joysticks[0].get_axis(0)
        ax1 = self.joysticks[0].get_axis(1)
        ax3 = self.joysticks[0].get_axis(3)
        ax4 = self.joysticks[0].get_axis(4)
        ax5 = self.joysticks[0].get_axis(5)
        if ax0 > .16 or ax0 < -.16:
            self.transVector1.x += self.move * ax0
            self.camVector1.x += self.move * ax0
         # M ove Backward.
        if ax1 > .16 or ax1 < -.16:
            self.transVector1.z += self.move * ax1
            self.camVector1.z += self.move * ax1
        #print "ax3: " + str(ax3) + " ax4: " + str(ax4)


        angleDeadZone = .04
        if ax4 < -angleDeadZone and ax3 > angleDeadZone: # 4-,3+
            oppositeOverAdjacent = ax4 / ax3
            aimAngle = -math.atan(oppositeOverAdjacent) #radians
           # print "angle: " + str(aimAngle) + " degree: " + str(math.degrees(aimAngle))

        elif ax4 < -angleDeadZone and ax3 < -angleDeadZone:# 4-,3-
            oppositeOverAdjacent = ax4 / ax3
            aimAngle = (math.pi / 2) - math.atan(oppositeOverAdjacent)  #radians
            aimAngle += math.pi / 2
          #  print "angle: " + str(aimAngle) + " degree: " + str(math.degrees(aimAngle))

        elif ax4 > angleDeadZone and ax3 < -angleDeadZone:# 4+,3-
            oppositeOverAdjacent = ax4 / ax3
            aimAngle = (math.pi / 2) - math.atan(oppositeOverAdjacent)  #radians
            aimAngle += (math.pi / 2)
           # print "angle: " + str(aimAngle) + " degree: " + str(math.degrees(aimAngle))

        elif ax4 > angleDeadZone and ax3 > angleDeadZone:# 4+,3+
            oppositeOverAdjacent = ax4 / ax3
            aimAngle = (math.pi / 2) - math.atan(oppositeOverAdjacent)  #radians
            aimAngle += (3 * math.pi / 2)
           # print "angle: " + str(aimAngle) + " degree: " + str(math.degrees(aimAngle))



        elif (ax3 < angleDeadZone and ax3 > -angleDeadZone) and ax4 > angleDeadZone:
            aimAngle = (3 * math.pi) / 2
        elif (ax3 < angleDeadZone and ax3 > -angleDeadZone) and ax4 < -angleDeadZone:
            aimAngle = (math.pi / 2)
        elif (ax4 < angleDeadZone and ax4 > -angleDeadZone) and ax3 > angleDeadZone :
            aimAngle = 0
        elif (ax4 < angleDeadZone and ax4 > -angleDeadZone) and ax3 < -angleDeadZone: 
            aimAngle = math.pi
        
        else:
            aimAngle = 0
        #print "angle: " + str(aimAngle) + " degree: " + str(math.degrees(aimAngle))
        if ax5 > .45 and self.bToggle1:
            self.player1.shoot(self.bulletp1[self.p1bulletcount])
            self.p1bulletcount += 1
            if self.p1bulletcount is 10:
                self.p1bulletcount =0
            self.soundMgr.playShot()
            self.bToggle1= False
            
        elif ax5 < .45:
            self.bToggle1= True
            
        rad = ogre.Radian(aimAngle)
        quat = self.player1node.getOrientation()
        yaww = quat.getYaw()
        yaww = rad - yaww
        self.player1node.yaw(yaww)


    def movePlayer2(self):
        ax0 = self.joysticks[1].get_axis(0)
        ax1 = self.joysticks[1].get_axis(1)
        ax3 = self.joysticks[1].get_axis(3)
        ax4 = self.joysticks[1].get_axis(4)
        ax5 = self.joysticks[1].get_axis(5)
        if ax0 > .16 or ax0 < -.16:
            self.transVector2.x += self.move * ax0
            self.camVector2.x += self.move * ax0
         # M ove Backward.
        if ax1 > .16 or ax1 < -.16:
            self.transVector2.z += self.move * ax1
            self.camVector2.z += self.move * ax1
        

        angleDeadZone = .04
        if ax4 < -angleDeadZone and ax3 > angleDeadZone: # 4-,3+
            oppositeOverAdjacent = ax4 / ax3
            aimAngle = -math.atan(oppositeOverAdjacent) #radians
           # print "angle: " + str(aimAngle) + " degree: " + str(math.degrees(aimAngle))
            print "angle: " + str(aimAngle) + " degree: " + str(math.degrees(aimAngle))

        elif ax4 < -angleDeadZone and ax3 < -angleDeadZone:# 4-,3-
            oppositeOverAdjacent = ax4 / ax3
            aimAngle = (math.pi / 2) - math.atan(oppositeOverAdjacent)  #radians
            aimAngle += math.pi / 2
          #  print "angle: " + str(aimAngle) + " degree: " + str(math.degrees(aimAngle))

        elif ax4 > angleDeadZone and ax3 < -angleDeadZone:# 4+,3-
            oppositeOverAdjacent = ax4 / ax3
            aimAngle = (math.pi / 2) - math.atan(oppositeOverAdjacent)  #radians
            aimAngle += (math.pi / 2)
           # print "angle: " + str(aimAngle) + " degree: " + str(math.degrees(aimAngle))

        elif ax4 > angleDeadZone and ax3 > angleDeadZone:# 4+,3+
            oppositeOverAdjacent = ax4 / ax3
            aimAngle = (math.pi / 2) - math.atan(oppositeOverAdjacent)  #radians
            aimAngle += (3 * math.pi / 2)
           # print "angle: " + str(aimAngle) + " degree: " + str(math.degrees(aimAngle))



        elif (ax3 < angleDeadZone and ax3 > -angleDeadZone) and ax4 > angleDeadZone:
            aimAngle = (3 * math.pi) / 2
        elif (ax3 < angleDeadZone and ax3 > -angleDeadZone) and ax4 < -angleDeadZone:
            aimAngle = (math.pi / 2)
        elif (ax4 < angleDeadZone and ax4 > -angleDeadZone) and ax3 > angleDeadZone :
            aimAngle = 0
        elif (ax4 < angleDeadZone and ax4 > -angleDeadZone) and ax3 < -angleDeadZone: 
            aimAngle = math.pi
        
        else:
            aimAngle = 0
        #print "angle: " + str(aimAngle) + " degree: " + str(math.degrees(aimAngle))
        if ax5 > .45 and self.bToggle2:
            self.player2.shoot(self.bulletp2[self.p2bulletcount])
            self.p2bulletcount += 1
            if self.p2bulletcount is 10:
                self.p2bulletcount =0

            self.bToggle2= False
            self.soundMgr.playShot()
        elif ax5 < .45:
            self.bToggle2= True

        rad = ogre.Radian(aimAngle)
        quat = self.player2node.getOrientation()
        yaww = quat.getYaw()
        yaww = rad - yaww
        self.player2node.yaw(yaww)


    def keyPressed(self, frameEvent):
        #print "in keypressed funtion"

        # Move the camera using keyboard input.
        self.transVector = ogre.Vector3(0, 0, 0)
        self.camVector = ogre.Vector3(0, 0, 0)
        # Move Forward.
        if self.keyboard.isKeyDown(OIS.KC_W):
            self.transVector.z -= self.move
            self.camVector.z -= self.move
        # Move Backward.
        if self.keyboard.isKeyDown(OIS.KC_S):
            self.transVector.z += self.move
            self.camVector.z += self.move
        # Strafe Left.
        if self.keyboard.isKeyDown(OIS.KC_A):
            self.transVector.x -= self.move
            self.camVector.x -= self.move
        # Strafe Right.
        if self.keyboard.isKeyDown(OIS.KC_D):
            self.transVector.x += self.move
            self.camVector.x += self.move

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






        if self.keyboard.isKeyDown(OIS.KC_ESCAPE):
            print "escape key pressed"
            self.engine.stop()
        
        

# -------------------
        #  if event.type == JOYAXISMOTION:
        #   if event.value > .1 or event.value < -.1:
         #   print "Axis: " + str(event.axis) + " Value: " + str(event.value)  
        	#print "Axis: " + str(self.axis)
        
            # Move Forward.
        


        
        return not self.keyboard.isKeyDown(OIS.KC_ESCAPE)   





# ---------------------

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
            if (self.entites[Entity].type is not "player") and (self.entites[Entity].type is not "bullet"):
                

                    
                if self.entites[Entity].type is "enemy":
                    if self.player1.box.intersects(self.entites[Entity].box) and not self.p1checked:
                        self.entites[Entity].kill(0)
                        self.player1.kill()
                        self.player1.score -= 2
                        return True
                elif self.player1.box.intersects(self.entites[Entity].box):
                    #self.p1stuckcheck+= 1
                    return True
        #if(self.p1stuckcheck >= 10):
            #self.player1.kill()
            #self.p1stuckcheck = 0

        return False

    def checkCollisionP2(self):
        for Entity in self.entites:
            if (self.entites[Entity].type is not "player") and (self.entites[Entity].type is not "bullet"):
 
                    
                if self.entites[Entity].type is "enemy":
                    if self.player2.box.intersects(self.entites[Entity].box) and not self.p2checked:
                        self.entites[Entity].kill(1)
                        self.player2.kill()
                        self.player2.score -= 2
                        return True
                elif self.player2.box.intersects(self.entites[Entity].box):
                    #self.p2stuckcheck+= 1
                    return True
        #if(self.p2stuckcheck >= 10):
            #self.player2.kill()
            #self.p2stuckcheck = 0

        return False

        
