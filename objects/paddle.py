from .base import MovingObject


class Paddle(MovingObject):
    def __init__(self, x, y, width, height, speed, field_height):
        super().__init__(x, y, width, height, speed)
        self.field_height = field_height

    def move_up(self):
        self.vy = -1.0

    def move_down(self):
        self.vy = 1.0

    def stop(self):
        self.vy = 0.0

    def update(self, dt: float):
        self.move(dt)
        # ограничение по полю
        if self.y < 0:
            self.y = 0
        if self.y + self.height > self.field_height:
            self.y = self.field_height - self.height
