from ursina import *

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.model = "cube"
        self.color = color.azure
        self.scale = (1, 2, 1)
        self.position = (0, 1, 0)
        self.speed = 5
        self.rotation_speed = 100

    def update(self):
        self.move()
        self.rotate_camera()

    def move(self):
        if held_keys['w']:
            self.position += self.forward * time.dt * self.speed
        if held_keys['s']:
            self.position -= self.forward * time.dt * self.speed
        if held_keys['a']:
            self.position -= self.right * time.dt * self.speed
        if held_keys['d']:
            self.position += self.right * time.dt * self.speed

    def rotate_camera(self):
        # Rotaciona o jogador (e a câmera junto) ao pressionar as setas para os lados
        if held_keys['left arrow']:
            self.rotation_y += self.rotation_speed * time.dt
        if held_keys['right arrow']:
            self.rotation_y -= self.rotation_speed * time.dt

        # Posiciona a câmera atrás do jogador
        camera.position = self.position + (-self.forward * 10) + (Vec3(0, 5, 0))
        camera.look_at(self.position + Vec3(0, 2, 0))  # Ajuste o valor Y para olhar mais alto ou mais baixo no personagem

app = Ursina()
player = Player()
app.run()
