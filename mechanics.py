from ursina import *
from ursina.shaders import *
from ursina.collider import *
from enemies import *

class Melee(Entity):
    def __init__(self, position):
        # Melee features
        super().__init__()
        self.model = "cube"
        self.scale = (10, 5, 10)
        self.position = position
        self.collider = "box"
        self.hitSound = Audio('audio/hit-sound.mp3', loop=False, autoplay=True)
        self.hitSound.volume = 0.6
    def update(self):
        if isinstance(self.intersects().entity, Enemy):
            die = Audio('audio/died.mp3', loop=False, autoplay=True)
            die.volume = 0.3
            destroy(self.intersects().entity)
            
class Caster(Entity):
    def __init__(self, position):
        # Caster features
        super().__init__()
        self.model = "sphere"
        self.scale = 1
        self.color = color.orange
        self.position = position
        self.collider = "sphere"
        self.castSound = Audio('audio/cast-sound.mp3', loop=False, autoplay=True)
        self.castSound.volume = 0.6
        self.speed = 50
    def update(self):
        self.z += time.dt * self.speed
        
        if self.y > 100:
            destroy(self)
        if isinstance(self.intersects().entity, Enemy):
            die = Audio('audio/died.mp3', loop=False, autoplay=True)
            die.volume = 0.3
            destroy(self.intersects().entity)
            destroy(self)
     