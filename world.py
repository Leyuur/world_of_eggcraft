from ursina import *
from ursina.shaders import *
from ursina.collider import *
from ursina.prefabs.sky import *
from ursina.lights import *

class World():
    def __init__(self):
        super().__init__()
        self.ground = Entity(
            model = "plane",
            texture = "grass",
            shader = lit_with_shadows_shader,
            collider = "box",
            scale = 2000
        )


        self.sky = Sky()
        self.sun = Entity(rotation_x=45, rotation_y=45)
        DirectionalLight(shadows=True, parent=self.sun, y=2, z=3)
        self.ambientSound = Audio('audio/ambient-sound.mp3', loop=True, autoplay=True)
        self.ambientSound.volume = .5

    