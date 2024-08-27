from random import randint
from ursina import *
from ursina.shaders import *
from ursina.collider import *

class Enemy(Entity):
    def __init__(self, player):
        super().__init__(player)
        self.collider = "mesh"
        self.shader = lit_with_shadows_shader
        self.speed = 6
        self.target = player
        self.attackCoolDown = 0
        self.attackRate = 3
 
    def update(self):
        if self.attackCoolDown > 0:
            self.attackCoolDown -= time.dt
            
        dist = distance_xz(self.target.position, self.position)
        if dist > 100:
            return
        
        self.look_at_2d(self.target.position, 'y')
        
        if dist > 7:
            self.position += self.forward * time.dt * self.speed

        if dist <= 12 and self.attackCoolDown <= 0:
            # add enemy attack
            self.attackCoolDown = self.attackRate
            
class Cocodrilo(Enemy):
    def __init__(self, player):
        super().__init__(player)
        self.model = "models/cocodrilo.obj"
        self.texture = "models/textures/texture-cocodrilo.png"
        self.scale = 5
        self.position = (randint(0, 1990), self.scale[1] / 2, randint(0, 1990))
        self.speed = 2
        self.target = player
  

def enemySpawner(player, q=int):
    for _ in range(q):
        Cocodrilo(player)
