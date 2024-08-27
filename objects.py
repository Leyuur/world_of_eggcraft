from random import randint
from ursina import *
from ursina.shaders import *
from ursina.collider import *


class Tree(Entity):
    def __init__(self):
        # enemy features
        super().__init__()
        self.model = "models/tree.obj"
        self.texture = "models/textures/texture-tree.png"
        self.scale = 60
        self.position = (randint(0, 1990), self.scale[1] / 2 - 4, randint(0, 1990))
        self.collider = "mesh"
        self.shader = lit_with_shadows_shader
            
def treeSpawner(q=int):
    for i in range(q):
        Tree()
        