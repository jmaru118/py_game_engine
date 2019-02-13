#Travis Walker and Shawn White
from vector import MyVector
import ent

class EntityMgr:
    def __init__(self, engine):
        print "starting ent mgr"
        self.engine = engine
    
    def init(self):
        self.entities = {}
        self.nEnts = 0
	self.enemies = []
	self.enemyPositions = []
        self.selectedEnt = None
        self.selectedEntIndex = 0
        self.selectedEntities = []
        self.ent =0
	self.killed = 0
    


        self.entTypes = [ent.Player,ent.Bullet,ent.Wall,ent.Enemy]

    def createEnt(self, entType, pos = MyVector(0,0,0), yaw = 0):
        ent = entType(self.engine,self.nEnts, pos = pos, yaw = yaw)
        ent.init()
        self.entities[self.nEnts] = ent;
        self.selectedEnt = ent
        self.selectedEntIndex = self.nEnts;
        ent.box=ent.aspects[1].bound

        self.nEnts = self.nEnts + 1
        return ent

    def selectNextEnt(self):
        if self.selectedEntIndex >= self.nEnts - 1:
            self.selectedEntIndex = 0
        else:
            self.selectedEntIndex += 1
        self.selectedEnt = self.entities[self.selectedEntIndex]
        #print "EntMgr selected: ", str(self.selectedEnt)
        return self.selectedEnt

    def getSelected(self):
        return self.selectedEnt

    def tick(self, dtime):
        for eid, entity in self.entities.iteritems():
            entity.tick(dtime)
      
        





