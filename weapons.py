from ursina import *
from ursina.shaders import *
from ursina.collider import *
from characters import *

class Hitbox(Entity):
    def __init__(self, position):
        # hitbox features
        super().__init__()
        self.model = "cube"
        self.scale = (10, 5, 10)
        self.position = position
        self.collider = "box"
        self.color = color.red
        self.shader = lit_with_shadows_shader
    def update(self):
        if isinstance(self.intersects().entity, Enemy):
            destroy(self.intersects().entity)
        
        