from Shared import *
from Shared.GameObject import GameObject
class Pad(GameObject):

    def __init(self, position, sprite):
        super(Pad, self).__init__(position, GameConstants.PAD_SIZE, sprite)