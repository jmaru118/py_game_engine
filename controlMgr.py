#Travis Walker and Shawn White
import ogre.io.OIS as OIS

class ControlMgr:
    def __init__(self, engine):
        self.engine = engine
        self.selectionMgr = engine.selectionMgr
        self.Keyboard = engine.inputMgr.keyboard
        

    def init(self):
        pass

    def tick(self, dt):
		#some code from Sushil assignment 4 solution
        #print str(self.selectedEntIndex), selectedEnt.id
        import utils
        selectedEnts = self.engine.entityMgr.selectedEntities
        # Speed Up
        if  self.Keyboard.isKeyDown(OIS.KC_UP):
            pass
        if  self.Keyboard.isKeyDown(OIS.KC_DOWN):
            pass

        # Turn Left.
        if  self.Keyboard.isKeyDown(OIS.KC_LEFT):
           pass
            
        # Turn Right.
        if  self.Keyboard.isKeyDown(OIS.KC_RIGHT):
            pass

        #print self.selectedEnt.uiname, selectedEnt.id, str(selectedEnt.vel)

    def stop(self):
        pass
