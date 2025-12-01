from Chainable import Chainable
from typing import *

class Config:
    def __init__(self, 
                 master_dimension: Optional[int] = 60, 
                 radiusx: Optional[int] = 30,
                 radiusy: Optional[int] = 30,
                 height: Optional[int] = 120):
        self.master_dimension = master_dimension
        self.radiusx = radiusx or self.master_dimension / 2
        self.radiusy = radiusy or self.master_dimension / 2
        self.height = height or self.master_dimension * 2

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

        self.x = self.centerx - dx * (radiusx + dx * (2 * starti / endi) * radiusx) - self.dx
        self.i = starti

    def update(self, i = None):
        if not self.done:
            self.x += self.dx
            self.y = self.dy * self.radiusy * (1 - ((self.x - self.centerx) / self.radiusx) ** 2) ** 0.5 + self.centery
            self.i += self.stepi
        if self.i > self.endi - self.stepi:
            self.done = True
        return self.x, self.y

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
    def __init__(self, root1, root2, y, height, startx, dx, endi, stepi=1):
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
    
class Letter:
    def __init__(self, config):
        self.radiusx = config.radiusx
        self.radiusy = config.radiusy
        self.height = config.height

    def a(self, cornerx, cornery, radiusx=None, radiusy=None, nsteps=None):
        radiusx = radiusx or self.radiusx
        radiusy = radiusy or self.radiusy
        nsteps = nsteps or 2 * self.radiusx
        centerx = cornerx + radiusx
        centery = cornery + radiusy
        endi = 2 * radiusx
        stepi = endi / nsteps
        first = SemiEllipse(centerx, centery, radiusx, radiusy, -1, True, 0, stepi, endi)
        second = SemiEllipse(centerx, centery, radiusx, radiusy, 1, False, 0, stepi, endi)
        curve = SemiEllipse(centerx + radiusx + radiusx / 3, centery, radiusx / 3, radiusy, 1, False, 0, 1, radiusx / 3)

        return first.then(second).then(curve)
    
    def b(self, cornerx, cornery, radiusx=None, radiusy=None, height=None, nstepsHeight=None, nstepsCircle=None):
        radiusx = radiusx or self.radiusx
        radiusy = radiusy or self.radiusy
        height = height or self.height
        nstepsHeight = nstepsHeight or self.height / 2
        nstepsCircle = nstepsCircle or 2 * self.radiusx
        centerx = cornerx + radiusx
        centery = cornery + radiusy
        endi = 2 * radiusx
        stepi = endi / nstepsCircle

        stick = Line(cornerx, cornery + 2 * radiusy - height, cornerx, cornery + 2 * radiusy, nstepsHeight)
        first = SemiEllipse(centerx, centery, radiusx, radiusy, 1, True, 0, stepi, endi)
        second = SemiEllipse(centerx, centery, radiusx, radiusy, -1, False, 0, stepi, endi)
        
        return stick.then(first).then(second)
    
    def c(self, cornerx, cornery, radiusx=None, radiusy=None, nsteps=None):
        radiusx = radiusx or self.radiusx * 0.8
        radiusy = radiusy or self.radiusy
        centerx = cornerx + radiusx
        centery = cornery + radiusy
        endi = 2 * radiusx
        nsteps = nsteps or 2 * self.radiusx
        stepi = endi / nsteps
        proportion = 0.9

        first = SemiEllipse(centerx, centery, radiusx, radiusy, -1, True, endi * (1 - proportion), stepi, endi)
        second = SemiEllipse(centerx, centery, radiusx, radiusy, 1, False, 0, stepi, endi * proportion)
        
        return first.then(second)
    
    def d(self, cornerx, cornery, radiusx=None, radiusy=None, height=None, nstepsHeight=None, nstepsCircle=None):
        radiusx = radiusx or self.radiusx
        radiusy = radiusy or self.radiusy
        height = height or self.height
        nstepsHeight = nstepsHeight or self.height / 2
        nstepsCircle = nstepsCircle or 2 * self.radiusx
        centerx = cornerx + radiusx
        centery = cornery + radiusy
        endi = 2 * radiusx
        stepi = endi / nstepsCircle

        first = SemiEllipse(centerx, centery, radiusx, radiusy, -1, True, 0, stepi, endi)
        second = SemiEllipse(centerx, centery, radiusx, radiusy, 1, False, 0, stepi, endi)
        stick = Line(cornerx + 2 * radiusx, cornery + 2 * radiusy - height, cornerx + 2 * radiusx, cornery + 2 * radiusy, nstepsHeight)
        
        return first.then(second).then(stick)
    
