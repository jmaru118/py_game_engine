import ogre.renderer.OGRE as ogre

class Renderer:
    def __init__(self, ent):
        self.ent = ent
        self.entOgre = self.ent.engine.gfxMgr.sceneManager.createEntity(self.ent.uiname + str(self.ent.engine.entityMgr.nEnts), self.ent.mesh)
        self.node = self.ent.engine.gfxMgr.sceneManager.getRootSceneNode().createChildSceneNode(self.ent.uiname+'node', self.ent.pos)
        self.node.attachObject(self.entOgre)
        self.ent.node = self.node
        self.bound=self.entOgre.getWorldBoundingBox(True)
        
        #check for wall
        if self.ent.uiname == 'wall' + str(self.ent.id):
            self.entOgre.setMaterialName ('Examples/EnvMappedRustySteel')

        if self.ent.uiname == 'player':
            print" scale player"
            self.node.scale((50, 50, 50))
        
        if self.ent.uiname == 'enemy' + str(self.ent.id):
            print" scale enemy"
            self.node.scale((3, 3, 3))
        if self.ent.uiname == 'bullet' + str(self.ent.id):
            self.node.scale((.45, .45, .45))
            self.entOgre.setMaterialName('Examples/Chrome')


    def tick(self, dtime):
        if self.ent.uiname == 'player'+str(self.ent.id):
            self.bound = self.entOgre.getWorldBoundingBox(True)
            self.node.showBoundingBox(False)
        else:
            if self.ent.uiname == 'bullet'+str(self.ent.id):
                self.bound = self.entOgre.getWorldBoundingBox(True)
            if self.ent.uiname == 'enemy'+str(self.ent.id):
                self.bound = self.entOgre.getWorldBoundingBox(True)
                
            self.ent.node.setPosition(self.ent.pos)
        
            errorRange = 0.05
            x = abs(self.ent.desiredHeading - self.ent.heading)

            if x < errorRange:
                self.ent.node.yaw(ogre.Degree(0))

            if x > errorRange:
                amountTurned = self.ent.turningRate * dtime

                if self.ent.heading < self.ent.desiredHeading:
                    self.ent.node.yaw(ogre.Degree(amountTurned))
                elif self.ent.heading > self.ent.desiredHeading:
                    self.ent.node.yaw(ogre.Degree(-amountTurned))
            self.node.showBoundingBox(False)

            
