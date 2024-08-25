from ursina import *
from ursina.shaders import *
from ursina.collider import *
from ursina.prefabs.sky import *
from ursina.lights import *
from world import World
from player import *

game = Ursina(fullscreen = True, show_ursina_splash=True)

World()


player = Warrior()
cocodrilos = enemySpawner(5)
# EditorCamera()

game.run()