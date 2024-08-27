from ursina import *
from ursina.shaders import *
from ursina.collider import *
from ursina.prefabs.first_person_controller import FirstPersonController
from mechanics import *
from enemies import *


class Player(FirstPersonController):
    def __init__(self):
        # player features
        super().__init__()
        self.model = "models/eggwin.obj"
        self.texture = "models/textures/texture-eggwin.png"
        self.scale = 7
        self.position = (0, self.scale[1] / 2, 0)
        self.collider = BoxCollider(self)
        self.shader = lit_with_shadows_shader
        self.speed = 8
        self.sense = 100
        self.gravity = 1
        self.jump_height = 0.4
        self.jump_speed = 0.5
        self.velocity_y = 0 
        self.velocity_x = 0
        self.is_jumping = False
        self.attackCoolDown = 0
        self.attackRate = 0.5
        # self.move = True
        mouse.locked = True
    
    def update(self):
        # player movimentation
        # if self.move:
        move(self=self)
            
        if self.attackCoolDown > 0:
            self.attackCoolDown -= time.dt
        
        # player gravity
        gravity(self=self)
       
        # player camera position
        camera.z = -7
        
    def input(self, key):
        newKey = key
        jump(self=self, key=newKey ,keyValue="space")
        if self.attackCoolDown <= 0 and key == "left mouse up":
            attack(self=self, key=newKey,keyValue="left mouse up")
            self.attackCoolDown = self.attackRate
        

class Warrior(Player):
    def __init__(self):
        super().__init__()
        self.model = "models/eggwin.obj"
        self.texture = "models/textures/texture-eggwin.png"
        self.thisClass = Warrior

class Mage(Player):
    def __init__(self):
        super().__init__()
        self.model = "models/hadeggar.obj"
        self.texture = "models/textures/texture-hadeggar.png"
        self.thisClass = Mage
    
        