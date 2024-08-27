from ursina import *
from ursina.shaders import *
from ursina.collider import *
from ursina.prefabs.sky import *
from ursina.lights import *
from world import World
from player import Warrior, Mage
from enemies import *
from objects import *
from mechanics import *

game = Ursina(
    development_mode=False,
    fullscreen = True, 
    # show_ursina_splash=True,
    title = "World of Eggcraft"
    )

World()

player = Warrior()

# cocodrilos = enemySpawner(150)

# trees = treeSpawner(200)

# EditorCamera()

game.run()