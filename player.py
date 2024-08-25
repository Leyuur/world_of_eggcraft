from ursina import *
from ursina.shaders import *
from ursina.collider import *
from mechanics import *


class Warrior(Entity):
    def __init__(self):
        # player features
        super().__init__()
        self.model = "models/eggwin.obj"
        self.texture = "models/textures/texture-eggwin.png"
        self.scale = 5
        self.position = (0, self.scale[1] / 2, 0)
        self.collider = "box"
        self.shader = lit_with_shadows_shader
        self.speed = 10
        self.gravity = 1
        self.jump_height = 0.3
        self.jump_speed = 0.5
        self.velocity_y = 0 
        self.is_jumping = False
    
    def update(self):
        # player movimentation
        self.x += held_keys['d'] * time.dt * self.speed
        self.x -= held_keys['a'] * time.dt * self.speed
        self.z += held_keys['w'] * time.dt * self.speed
        self.z -= held_keys['s'] * time.dt * self.speed
        
        # player gravity
        self.velocity_y -= self.gravity * time.dt
        self.y += self.velocity_y
        
        # verify collision
        if self.y <= self.scale[1] / 2:
            self.y = self.scale[1] / 2
            self.velocity_y = 0
            self.is_jumping = False
        
        # player camera position
        camera.position = (self.position.x, self.scale[1] + 50, self.position.z - 100)
        camera.look_at(self)

    def input(self, key):
        if key == 'space' and not self.is_jumping:
            self.velocity_y = self.jump_height
            self.is_jumping = True
        if key == 'left mouse up':
            invoke(destroy, Melee(self.position), delay = 0.1)

class Mage(Entity):
    def __init__(self):
        # player features
        super().__init__()
        self.model = "models/hadeggar.obj"
        self.texture = "models/textures/texture-hadeggar.png"
        self.scale = 5
        self.position = (0, self.scale[1] / 2, 0)
        self.collider = "box"
        self.shader = lit_with_shadows_shader
        self.speed = 10
        self.gravity = 1
        self.jump_height = 0.3
        self.jump_speed = 0.5
        self.velocity_y = 0 
        self.is_jumping = False
    
    def update(self):
        # player movimentation
        self.x += held_keys['d'] * time.dt * self.speed
        self.x -= held_keys['a'] * time.dt * self.speed
        self.z += held_keys['w'] * time.dt * self.speed
        self.z -= held_keys['s'] * time.dt * self.speed
        
        # player gravity
        self.velocity_y -= self.gravity * time.dt
        self.y += self.velocity_y
        
        # verify collision
        if self.y <= self.scale[1] / 2:
            self.y = self.scale[1] / 2
            self.velocity_y = 0
            self.is_jumping = False
        
        # player camera position
        camera.position = (self.position.x, self.scale[1] + 50, self.position.z - 100)
        camera.look_at(self)

    def input(self, key):
        if key == 'space' and not self.is_jumping:
            self.velocity_y = self.jump_height
            self.is_jumping = True
        if key == 'left mouse up':
             Caster(self.position)
        