import pygame
import math

from Chainable import Chainable

class Circle(Chainable):
    def __init__(self, x, y, r, omega, x1 = 0):
        self.x0 = x
        self.centery = y
        self.radius = r
        self.omega = omega
        self.originx = 0
        self.origin = 0
        self.dt = 1 / 100
        self.t = 0
        self.x1 = x1
        self.done = False

    def update(self, i = 0):
        if not self.done:
            self.t += 1
            term = (self.x0 + self.x1) / 2 + (self.x1 - self.x0) * math.sin(2 * math.pi * self.t * self.dt)
            self.x = math.cos(self.omega * self.t * self.dt) * self.radius + term
            self.y = math.sin(self.omega * self.t * self.dt) * self.radius + self.centery
            #print(self.x0, math.pi * self.t * self.dt, math.sin(math.pi * self.t * self.dt), (self.x1 - self.x0) * math.sin(math.pi * self.t * self.dt))
            print(self.x1, self.x0, (self.x - self.x0)**2, (self.x - self.x1)**2)
        if self.t > 500:
            self.done = True
        return self.x, self.y
    
class Center(Chainable):
    def __init__(self, x0, y, x1):
        self.x0 = x0
        self.x1 = x1
        self.y = y 
        self.dt = 1 / 100
        self.t = 0
        self.done = False

    def update(self, i = 0):
        if not self.done:
            self.t += 1
            self.x = (self.x0 + self.x1) / 2 + (self.x1 - self.x0) * math.sin(2 * math.pi * self.t * self.dt)
        if self.t > 100:
            self.done = True
        return self.x, self.y
     

class FourPointCurve(Chainable):
    def __init__(self,  a, b, c, no_steps = 100, center = (500, 300), upper_limit = 2 * math.pi):
        self.x0 = center[0]
        self.y0 = center[1]
        self.a = a
        self.b = b
        self.c = c
        self.no_steps = no_steps
        self.upper_limit = upper_limit
        self.done = False
        self.t = 0
        self.step = upper_limit / no_steps

    def update(self, i = None):
        if not self.done:
            theta = self.t - self.c * math.sin(4 * self.t)
            r = ((math.cos(4 * self.t) + 1) * 0.5) ** 1.2 * (self.b - self.a) + self.a
            point = r * math.e ** (1j * -theta)
            self.x = point.real + self.x0
            self.y = point.imag + self.y0
            self.t += self.step
        if self.t > self.upper_limit:
            self.done = True
        return self.x, self.y
    
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

c = Circle(250, 300, 100, 2 * math.pi, 500)
t = Center(250, 300, 500)
curve = FourPointCurve(40, 100, 0.4, 200, upper_limit = 6.28)
curve = Rangoli([
    [0.1, -15],
    [0.2, -11],
    [0.25, -7],
    [-0.05, -3],
    [1.05, 1],
    [0.8, 5],
    [-0.25, 9]
], 100, 1500, upper_limit = 2 * math.pi)

chain = curve#.then(t)

pygame.init()
width, height = 1000, 600
Display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chainable")
clock=pygame.time.Clock()
x, y = 0, 0

try:
    Display.fill('grey')
    done = False
    while not done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = True
                break
        if not chain.done:
            coord = chain.update()
            if coord:
                print(coord)
                pygame.draw.circle(Display, "#732f14", coord, 2)
            pygame.display.flip()

        # out.write(frame)
        clock.tick(90)

finally:
    # out.release()
    pygame.quit()