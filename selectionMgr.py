#Travis Walker and Shawn White
import ogre.io.OIS as OIS

class SelectionMgr:
    def __init__(self, engine):
        self.engine = engine
        self.entityMgr = engine.entityMgr
        self.selectedEntities = []
        self.numSelected = 0;
        print " selectionMgr init"
		
    def init(self):
        self.keyboard = self.engine.inputMgr.keyboard
        self.toggle = .1

    def tick(self, dt):
        if self.toggle >= 0:
           self.toggle -= dt
	    
        if  self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_TAB):
            self.toggle = .5
            if self.keyboard.isKeyDown(OIS.KC_LSHIFT):
               self.appendNextEnt()
            else:
               self.selectNextEnt()

			
  

    def stop(self):
        pass
