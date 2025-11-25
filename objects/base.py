import pygame


class GameObject:
    def __init__(self, x, y, width, height):
        self.x = float(x)
        self.y = float(y)
        self.width = width
        self.height = height

    def get_rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)

    def update(self, dt):
        pass

    def draw(self, surface):
        pass


class MovingObject(GameObject):
    def __init__(self, x, y, width, height, speed):
        GameObject.__init__(self, x, y, width, height)
        self.speed = speed
        self.vx = 0.0
        self.vy = 0.0

    def move(self, dt):
        self.x += self.vx * self.speed * dt
        self.y += self.vy * self.speed * dt
