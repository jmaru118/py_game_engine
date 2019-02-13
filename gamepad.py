import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS

class GamePad(OIS.JoyStickListener):

    def __init__(self):
        OIS.JoyStickListener.__init__(self)

    def povMoved(self, Event, pov):
        pass
    def axisMoved(self, Event, axis):
        pass
    def sliderMoved(self, Event, sliderID):
        pass
    def buttonPressed(self, Event, button):
        pass
    def buttonReleased(self, Event, button):
        pass
