from random import randint
from ursina import *
from ursina.shaders import *
from ursina.collider import *


class Enemy(Entity):
    def __init__(self):
        # enemy features
        super().__init__()
        self.model = "models/cocodrilo.obj"
        self.texture = "models/textures/texture-cocodrilo.png"
        self.scale = 5
        self.position = (randint(0, 1990), self.scale[1] / 2, randint(0, 1990))
        self.collider = "mesh"
        self.shader = lit_with_shadows_shader
            
def enemySpawner(q=int):
    for i in range(q):
        Enemy()
        