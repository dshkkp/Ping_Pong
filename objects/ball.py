import random
from .base import MovingObject


class Ball(MovingObject):
    def __init__(self, x, y, size, speed, field_width, field_height):
        super().__init__(x, y, size, size, speed)
        self.size = size
        self.field_width = field_width
        self.field_height = field_height
        self.reset(direction=random.choice([-1, 1]))

    def reset(self, direction: int = 1):
        # центр
        self.x = (self.field_width - self.size) / 2
        self.y = (self.field_height - self.size) / 2

        # направление
        self.vx = direction
        self.vy = random.choice([-0.7, -0.4, 0.4, 0.7])

    def update(self, dt: float):
        self.move(dt)
