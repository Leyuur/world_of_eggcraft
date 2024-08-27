from ursina import *
from ursina.shaders import *
from ursina.collider import *
from enemies import *
from world import *

class Melee(Entity):
    def __init__(self, parent):
        # Melee features
        super().__init__()
        self.scale = 5
        self.position = parent.position + parent.forward
        self.rotation = parent.rotation
        self.collider = "box"
        self.hitSound = Audio('audio/hit-sound.mp3', loop=False, autoplay=True)
        self.hitSound.volume = 0.6
    def update(self):
        if isinstance(self.intersects().entity, Enemy):
            die = Audio('audio/died.mp3', loop=False, autoplay=True)
            die.volume = 0.3
            destroy(self.intersects().entity)
            
class Caster(Entity):
    def __init__(self, position, parent):
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
        self.parent = parent
        self.direction = self.parent.forward.normalized()
    def update(self):
        self.position += self.direction * time.dt * self.speed
        
        if self.y > 100:
            destroy(self)
        if isinstance(self.intersects().entity, Enemy):
            die = Audio('audio/died.mp3', loop=False, autoplay=True)
            die.volume = 0.3
            destroy(self.intersects().entity)
            destroy(self)
    
def move(self):
    def rotate_with_mouse(self):
        self.rotation_y += mouse.velocity[0] * self.sense
        self.camera_pivot.rotation_x -= mouse.velocity[1] * self.sense
        self.camera_pivot.rotation_x = clamp(self.camera_pivot.rotation_x, -10, 80)
    rotate_with_mouse(self)
    if held_keys['w']:
        self.position += self.forward * time.dt * self.speed
    if held_keys['s']:
        self.position -= self.forward * time.dt * self.speed
    if held_keys['a']:
        self.position -= self.right * time.dt * self.speed
    if held_keys['d']:
        self.position += self.right * time.dt * self.speed
        
def gravity(self):
     # player gravity
    self.velocity_y -= self.gravity * time.dt
    self.y += self.velocity_y
    
    # verify collision
    if self.y <= self.scale[1] / 2:
        self.y = self.scale[1] / 2
        self.velocity_y = 0
        self.is_jumping = False
        
def jump(self, key, keyValue):
    if key == keyValue and not self.is_jumping:
            self.velocity_y = self.jump_height
            self.is_jumping = True
            
def attack(self, key, keyValue):
    from player import Mage, Warrior
    if key == keyValue:
        if self.thisClass == Warrior:
            invoke(destroy, Melee(self), delay = 0.1)
        if self.thisClass == Mage:
            Caster(self.position, self)