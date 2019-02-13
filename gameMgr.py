#Travis Walker and Shawn White
from vector import Vector3


class GameMgr:
    def __init__(self, engine):
        self.engine = engine
        print "starting Game mgr"
        pass

    def init(self):
        self.loadLevel()


    def loadLevel(self):
        self.game1()
        

    def game1(self):
        x = 0
        #create player
        print "GameMgr Creating"
        self.bulletP1 = []
        self.bulletP2 = []
        self.player1 = self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[0], pos = Vector3(-2000, 0, -2500))
        self.player2 = self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[0], pos = Vector3(2000, 0, 2500))
        for i in range(10):
            self.bulletP1.append(self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[1], pos = Vector3(-2300, -200, -2500)))
        for i in range(10):
            self.bulletP2.append(self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[1], pos = Vector3(-2300, -200, -2500)))
        print "GameMgr Created: ", self.player1.uiname, self.player1.eid
        print "GameMgr Created: ", self.player2.uiname, self.player2.eid
	    #self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[2], pos = Vector3(200, 0, 200))
        # self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[2], pos = Vector3(-200, 0, -200))

        for i in range(60):
            #left boundary
            self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[2], pos = Vector3(-3000,0,-3000 + 100*i))
            #right boundary
            self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[2], pos = Vector3(-3000 + 100*i,0,-3000))
            #bottom boundary
            self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[2], pos = Vector3(3000 - 100*i,0,3000))
            #top boundary
            self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[2], pos = Vector3(3000,0,3000 - 100*i))
            if(i >= 10):
                self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[2], pos = Vector3(-3000 + 100*i,0,1400))
            if(i <= 50):
                self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[2], pos = Vector3(-3000 + 100*i,0,-1400))
        for i in range(28):
            if(i <= 11):
                self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[2], pos = Vector3(0,0,-1400+100*i))
            if(i >= 17):
                self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[2], pos = Vector3(0,0,-1400+100*i))
        
        self.engine.entityMgr.enemies.append(self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[3], pos = Vector3(0,0,0)))
	self.engine.entityMgr.enemies[0].index = 0
	self.engine.entityMgr.enemyPositions.append(Vector3(0,0,0))
        self.engine.entityMgr.enemies.append(self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[3], pos = Vector3(600,0,-1000)))
	self.engine.entityMgr.enemies[1].index = 1
	self.engine.entityMgr.enemyPositions.append(Vector3(600,0,-1000))
        self.engine.entityMgr.enemies.append(self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[3], pos = Vector3(2000,0,900)))
	self.engine.entityMgr.enemies[2].index = 2
	self.engine.entityMgr.enemyPositions.append(Vector3(2000,0,900))
        self.engine.entityMgr.enemies.append(self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[3], pos = Vector3(1700,0,-2600)))
	self.engine.entityMgr.enemies[3].index = 3
	self.engine.entityMgr.enemyPositions.append(Vector3(1700,0,-2600))
        self.engine.entityMgr.enemies.append( self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[3], pos = Vector3(500,0,-1700)))
	self.engine.entityMgr.enemies[4].index = 4
	self.engine.entityMgr.enemyPositions.append(Vector3(500,0,-1700))
        self.engine.entityMgr.enemies.append(self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[3], pos = Vector3(-600,0,1000)))
	self.engine.entityMgr.enemies[5].index = 5
	self.engine.entityMgr.enemyPositions.append(Vector3(-600,0,1000))
        self.engine.entityMgr.enemies.append(self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[3], pos = Vector3(-2000,0,-900)))
	self.engine.entityMgr.enemies[6].index = 6
	self.engine.entityMgr.enemyPositions.append(Vector3(-2000,0,-900))
        self.engine.entityMgr.enemies.append(self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[3], pos = Vector3(-1700,0,2600)))
	self.engine.entityMgr.enemies[7].index = 7
	self.engine.entityMgr.enemyPositions.append(Vector3(-1700,0,2600))
        self.engine.entityMgr.enemies.append(self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[3], pos = Vector3(-500,0,1700)))
	self.engine.entityMgr.enemies[8].index = 8
	self.engine.entityMgr.enemyPositions.append(Vector3(-500,0,1700))




    def tick(self, dt):
        pass

    def stop(self):
        pass
        

