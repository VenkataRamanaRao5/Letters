from Chainable import Chainable

class SemiEllipse(Chainable):
    def __init__(self, centerx, centery, radiusx, radiusy, dx = 1, isTop = True, starti = 0, stepi = 1, endi = None):
        super().__init__()
        if dx not in [1, -1]:
            raise ValueError("parameter dx of SemiEllipse object must be eiterh +1 or -1")
        self.centerx = centerx
        self.centery = centery
        self.radiusx = radiusx
        self.radiusy = radiusy
        self.dx = dx * stepi
        self.isTop = isTop
        self.starti = starti
        self.endi = endi or 2 * self.radiusx
        self.stepi = stepi
        self.dy = -1 if isTop else 1

        self.x = self.centerx - dx * (radiusx + dx * (2 * starti / self.endi) * radiusx) - self.dx
        self.i = starti

    def update(self, i = None):
        if not self.done:
            self.x += self.dx
            self.y = self.dy * self.radiusy * (1 - ((self.x - self.centerx) / self.radiusx) ** 2) ** 0.5 + self.centery
            self.i += self.stepi
        if self.i > self.endi - self.stepi:
            self.done = True
        return self.x, self.y
    
class Circle(Chainable):
    def __new__(cls, centerx, centery, radius, dx = 1, fromTop = True, starti = 0, stepi = 1, endi = None):
        first = SemiEllipse(centerx, centery, radius, radius, dx, fromTop, starti, stepi, endi)
        second = SemiEllipse(centerx, centery, radius, radius, -dx, not fromTop, starti, stepi, endi)

        return first.then(second)

class Line(Chainable):
    def __init__(self, startx, starty, endx, endy, nsteps=100):
        super().__init__()
        self.nsteps = nsteps
        self.done = False
        self.i = 0

        self.dx = (endx - startx) / nsteps
        self.dy = (endy - starty) / nsteps

        self.x = startx - self.dx
        self.y = starty - self.dy

    def update(self, i = None):
        if not self.done:
            self.x += self.dx
            self.y += self.dy
            self.i += 1
        if self.i > self.nsteps:
            self.done = True
        return self.x, self.y
        
class Parabola(Chainable):
    def __init__(self, root1, root2, y, height, startx, dx, endi, stepi=1.0):
        super().__init__()
        if dx not in [1, -1]:
            raise ValueError("parameter dx of Parabola object must be eiterh +1 or -1")
        self.done = False
        self.i = 0
        self.root1 = root1
        self.root2 = root2
        self.y1 = y
        self.height = height
        self.endi = endi
        self.stepi = stepi

        self.dx = dx * stepi
        self.x = startx - self.dx
        self.centerx = (root2 - root1) / 2

    def update(self, i = None):
        if not self.done: 
            self.x += self.dx
            self.y = - (self.height / (self.centerx ** 2)) * (self.x - self.root1) * (self.x - self.root2) + self.y1
            self.i += self.stepi
        if self.i > self.endi:
            self.done = True
        return self.x, self.y