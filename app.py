import time
import random
from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.lights import DirectionalLight
from ursina.audio import Audio
from ursina.prefabs.sky import Sky
from ursina.collider import MeshCollider
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina(
    # borderless=False, fullscreen=True, show_ursina_splash=True
)

def setup_scene():
    global sun, ground, ambientSound
    sun = Entity(rotation_x=45, rotation_y=45)
    ground = Entity(
        model="plane",
        texture="grass",
        scale=(200, 5, 200),
        shader=lit_with_shadows_shader,
        collider="box"
    )
    ambientSound = Audio('audio/ambient-music.mp3', loop=True, autoplay=False)
    ambientSound.volume = .3
    # ambientSound.play()

def setup_lights():
    DirectionalLight(parent=sun, y=2, z=3, shadows=True)
    Sky()

def create_enemies(number):
    return [Enemy() for _ in range(number)]
        
class Player(FirstPersonController):
    def __init__(self):
        super().__init__()
        self.model = "models/gato.obj"
        self.texture = "models/textures/cat_low_Cat_BaseColor.png"
        self.shader = lit_with_shadows_shader
        self.scale = 2
        self.collider = MeshCollider(self)
        camera.z = -7
        self.speed = 15
        self.hitSound = Audio('audio/hit-sound.mp3', loop=False, autoplay=False)
        self.hitSound.volume = 0.6
        self.cooldown_duration = 2
        self.last_attack_time = 0
        self.hit = False
        self.hitbox = None

    def input(self, key):
        if key == "left mouse down":
            current_time = time.time()
            if current_time - self.last_attack_time >= self.cooldown_duration:
                self.hitSound.play()
                self.last_attack_time = current_time
                self.hit = True
                self.create_hitbox()
                self.hit = False
            else:
                print(f"Cooldown active! Wait {round(self.cooldown_duration - (current_time - self.last_attack_time), 1)} seconds")

    def create_hitbox(self):
        if not self.hitbox:
            self.hitbox = Entity(
                model="cube",
                scale=(1, 3, 3),
                color=color.red,
            )
            self.hitbox.position = self.position + self.forward * 2
            self.hitbox.rotation = self.rotation
            print(f"Hitbox created at {self.hitbox.position}")
            invoke(destroy, self.hitbox, delay=0.2)  # Adjust delay if needed
            self.hitbox = None

class Enemy(Entity):
    def __init__(self):
        super().__init__()
        self.model = "models/gato.obj"
        self.texture = "models/textures/cat_low_Cat_BaseColor.png"
        self.shader = lit_with_shadows_shader
        self.scale = 5
        self.collider = MeshCollider(self)
        self.position = (
            random.uniform(-ground.scale_x / 2, ground.scale_x / 2),
            0,
            random.uniform(-ground.scale_z / 2, ground.scale_z / 2)
        )
        print(f"Enemy created at {self.position}")

setup_scene()
setup_lights()

enemies = create_enemies(2)  # Create multiple enemies
player1 = Player()

def update():
    if player1.hitbox:
        for enemy in enemies:
            if player1.hitbox.intersects(enemy):
                print(f"Hit detected between player hitbox at {player1.hitbox.position} and enemy at {enemy.position}")
                destroy(enemy)
                enemies.remove(enemy)
                print("Enemy destroyed")

app.run()
