from ursina import *
from ursina import Ursina, Entity, color, EditorCamera, held_keys, time
from ursina.shaders import lit_with_shadows_shader
from ursina.lights import AmbientLight, DirectionalLight
from ursina.audio import Audio
from ursina.prefabs.sky import Sky
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina(
    # borderless=False, 
    # fullscreen=True, 
    # show_ursina_splash=True
    ) 

sun = Entity(
    rotation_x=45,
    rotation_y= 45,
)
DirectionalLight(parent=sun, y=2, z=3, shadows=True)
Sky()

ground = Entity(
    model="plane",
    texture="grass",
    scale=(200, 5, 200),
    shader=lit_with_shadows_shader,
    collider="box"
)

player = Entity(
    model="models/gato.obj",
    texture="models/textures/cat_low_Cat_BaseColor.png",
    shader=lit_with_shadows_shader,
    scale=2,
)

ambientSound = Audio('audio/ambient-music.mp3', loop=True, autoplay=False)
ambientSound.volume = .3

def move(e):
    e.x += held_keys['d'] * time.dt * 8
    e.x -= held_keys['a'] * time.dt * 8
    e.z += held_keys['w'] * time.dt * 8
    e.z -= held_keys['s'] * time.dt * 8

def update():
    move(player)

EditorCamera()
# ambientSound.play()
app.run()
