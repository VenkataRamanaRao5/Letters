import pygame
import math
from Chainable import Chainable
from Helpers import Circle
    
class Rangoli(Chainable):
    def __init__(self, parameters, scale = 1, no_steps = 100, center = (500, 300), upper_limit = 2 * math.pi):
        self.x0 = center[0]
        self.y0 = center[1]
        self.parameters = parameters
        self.scale = scale
        self.no_steps = no_steps
        self.upper_limit = upper_limit
        self.done = False
        self.t = 0
        self.step = upper_limit / no_steps

    def update(self, i = None):
        if not self.done:
            point = 0
            for parameter in self.parameters:
                point += self.scale * parameter[0] * math.e ** (1j * parameter[1] * -self.t)
            self.x = point.real + self.x0
            self.y = point.imag + self.y0
            self.t += self.step
        if self.t > self.upper_limit:
            self.done = True
        return self.x, self.y
    
    @staticmethod
    def with_default_config():
        return Rangoli([
            [0.1, -15],
            [0.2, -11],
            [0.2, -7],
            [-0.05, -3],
            [1.05, 1],
            [0.8, 5],
            [-0.25, 9]
        ], 100, 1500, upper_limit = 2 * math.pi)
    
dist = 64
dots = set()
last = {(0, 0)}
for i in range(3):
    news = set()
    for x, y in last:
        news.add((x + dist, y))
        news.add((x - dist, y))
        news.add((x, y + dist))
        news.add((x, y - dist))
    last = news
    dots = dots.union(last)

dots = sorted(dots)

dots_chain = Chainable().chain([Circle(x + 500, y + 300, 1) for x, y in dots])

whole_rangoli = dots_chain.then(Rangoli.with_default_config())
    
import main