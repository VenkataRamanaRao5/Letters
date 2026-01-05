from Chainable import Chainable
from typing import Optional
from Helpers import SemiEllipse, Parabola, Line

class Config:
    def __init__(self, 
                 master_dimension: Optional[int] = 60, 
                 radiusx: Optional[int] = 30,
                 radiusy: Optional[int] = 30,
                 height: Optional[int] = 120):
        self.master_dimension = master_dimension or 60
        self.radiusx = radiusx or self.master_dimension / 2
        self.radiusy = radiusy or self.master_dimension / 2
        self.height = height or self.master_dimension * 2
    
class Letter:
    def __init__(self, config):
        self.master_dimension = config.master_dimension
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
    
    def e(self, cornerx, cornery, radiusx=None, radiusy=None, nsteps=None):
        radiusx = radiusx or self.radiusx * 0.9
        radiusy = radiusy or self.radiusy
        centerx = cornerx + radiusx
        centery = cornery + radiusy
        endi = 2 * radiusx
        nsteps = nsteps or 2 * radiusx
        stepi = endi / nsteps
        proportion = 0.9

        line = Line(centerx - radiusx * proportion * 0.95, centery, centerx + radiusx * proportion * 0.95, centery, nsteps)

        first = SemiEllipse(centerx, centery, radiusx * proportion, radiusy, -1, True, stepi/2, stepi, endi * proportion + stepi)
        second = SemiEllipse(centerx, centery, radiusx, radiusy, 1, False, 0, stepi, endi * proportion)
        
        return line.then(first).then(second)

    def f(self, cornerx, cornery, radiusx=None, radiusy=None, height=None, width=None, nstepsHeight=None, nstepsCurve=None, nstepsDash=None):
        radiusx = radiusx or self.master_dimension / 2
        radiusy = radiusy or self.master_dimension / 2
        height = height or self.master_dimension * 3 / 2
        width = width or self.master_dimension * 0.6
        nstepsHeight = nstepsHeight or height / 2
        nstepsDash = nstepsDash or width / 2
        nstepsCurve = nstepsCurve or 2 * self.radiusx
        centerx = cornerx + radiusx
        centery = cornery + radiusy
        endi = radiusx
        stepi = endi / nstepsCurve

        lying_stick = Line(centerx + width * 0.2, cornery, centerx, cornery, nstepsDash)
        curve = SemiEllipse(centerx, centery, radiusx, radiusy, -1, True, endi, stepi, 2 * endi)
        stick = Line(cornerx, cornery + radiusy, cornerx, cornery + radiusy + height, nstepsHeight)
        dash = Line(cornerx + radiusx - width, cornery + radiusy * 1.5, cornerx + radiusx + width * 0.2, cornery + radiusy * 1.5, nstepsDash)

        return stick.then(curve).then(lying_stick).then(dash)
        
    def h(self, cornerx, cornery, radiusx=None, radiusy=None, height=None, nstepsHeight=None, nstepsCircle=None):
        radiusx = radiusx or self.radiusx
        radiusy = radiusy or self.radiusy * 2
        height = height or self.height
        nstepsHeight = nstepsHeight or self.height / 2
        nstepsCircle = nstepsCircle or 8 * self.radiusx
        centerx = cornerx + radiusx
        centery = cornery + radiusy
        endi = 2 * radiusx
        stepi = endi / nstepsCircle

        stick = Line(cornerx, cornery + radiusy - height, cornerx, cornery + radiusy, nstepsHeight)
        first = SemiEllipse(centerx, centery, radiusx, radiusy, 1, True, 0, stepi, endi)
        second = SemiEllipse(centerx, centery, radiusx, radiusy, -1, False, 0, stepi, 0.25)
        
        return stick.then(first).then(second)
    
    def i(self, cornerx, cornery, radius=None, height=None, nstepsHeight=None, nstepsCircle=None):
        radius = radius or self.master_dimension / 12
        height = height or self.height / 3
        nstepsHeight = nstepsHeight or self.height / 2
        nstepsCircle = nstepsCircle or 2 * self.radiusx
        centerx = cornerx + radius
        centery = cornery - 15 - 2 * radius
        endi = 2 * radius
        stepi = endi / nstepsCircle

        stick = Line(cornerx + radius, cornery, cornerx + radius, cornery + height, nstepsHeight)
        first = SemiEllipse(centerx, centery, radius, radius, 1, True, 0, stepi, endi)
        second = SemiEllipse(centerx, centery, radius, radius, -1, False, 0, stepi, endi)
        
        return stick.then(first).then(second)
    
    def l(self, cornerx, cornery, height=None, nsteps=None):
        height = height or self.height
        nsteps = nsteps or height / 2

        stick = Line(cornerx, cornery, cornerx, cornery + height, nsteps)
        
        return stick
   
    def m(self, cornerx, cornery, radiusx=None, radiusy=None, height=None, nstepsHeight=None, nstepsCurve=None):
        radiusx = radiusx or self.radiusx * 0.8
        radiusy = radiusy or self.radiusy
        height = height or 2 * self.radiusy
        nstepsHeight = nstepsHeight or self.height / 2
        nstepsCurve = nstepsCurve or 8 * self.radiusx
        centerx = cornerx + radiusx
        centery = cornery + radiusy
        endi = 2 * radiusx
        stepi = endi / nstepsCurve

        first = Line(cornerx, cornery, cornerx, cornery + height, nstepsHeight)
        curve1 = SemiEllipse(centerx, centery, radiusx, radiusy, 1, True, 0, stepi, endi)
        second = Line(cornerx + 2 * radiusx, cornery + radiusy * 0.98, cornerx + 2 * radiusx, cornery + height, nstepsHeight * (height - radiusy) / height)
        curve2 = SemiEllipse(centerx + 2 * radiusx, centery, radiusx, radiusy, 1, True, 0, stepi, endi)
        third = Line(cornerx + 3.96 * radiusx, cornery + radiusy * 0.98, cornerx + 3.96 * radiusx, cornery + height, nstepsHeight * (height - radiusy) / height)
        
        return first.then(curve1).then(second).then(curve2).then(third)
    
    def n(self, cornerx, cornery, radiusx=None, radiusy=None, height=None, nstepsHeight=None, nstepsCurve=None):
        radiusx = radiusx or self.radiusx * 0.8
        radiusy = radiusy or self.radiusy
        height = height or 2 * self.radiusy
        nstepsHeight = nstepsHeight or self.height / 2
        nstepsCurve = nstepsCurve or 8 * self.radiusx
        centerx = cornerx + radiusx
        centery = cornery + radiusy
        endi = 2 * radiusx
        stepi = endi / nstepsCurve

        first = Line(cornerx, cornery, cornerx, cornery + height, nstepsHeight)
        curve = SemiEllipse(centerx, centery, radiusx, radiusy, 1, True, 0, stepi, endi)
        second = Line(cornerx + 1.96 * radiusx, cornery + radiusy * 0.98, cornerx + 1.96 * radiusx, cornery + height, nstepsHeight * (height - radiusy) / height)
        
        return first.then(curve).then(second)

    def o(self, cornerx, cornery, radiusx=None, radiusy=None, nsteps=None):
        radiusx = radiusx or self.radiusx * 0.9
        radiusy = radiusy or self.radiusy
        nsteps = nsteps or 2 * self.radiusx
        centerx = cornerx + radiusx
        centery = cornery + radiusy
        endi = 2 * radiusx
        stepi = endi / nsteps
        first = SemiEllipse(centerx, centery, radiusx, radiusy, -1, True, 0, stepi, endi)
        second = SemiEllipse(centerx, centery, radiusx, radiusy, 1, False, 0, stepi, endi)
        
        return first.then(second)

    def p(self, cornerx, cornery, radiusx=None, radiusy=None, height=None, nstepsHeight=None, nstepsCircle=None):
        radiusx = radiusx or self.radiusx
        radiusy = radiusy or self.radiusy
        height = height or self.height
        nstepsHeight = nstepsHeight or self.height / 2
        nstepsCircle = nstepsCircle or 2 * self.radiusx
        centerx = cornerx + radiusx
        centery = cornery + radiusy
        endi = 2 * radiusx
        stepi = endi / nstepsCircle

        stick = Line(cornerx, cornery, cornerx, cornery + height, nstepsHeight)
        first = SemiEllipse(centerx, centery, radiusx, radiusy, 1, True, 0, stepi, endi)
        second = SemiEllipse(centerx, centery, radiusx, radiusy, -1, False, 0, stepi, endi)
        
        return stick.then(first).then(second)

    def q(self, cornerx, cornery, radiusx=None, radiusy=None, height=None, nstepsHeight=None, nstepsCircle=None):
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
        stick = Line(cornerx + 2 * radiusx, cornery, cornerx + 2 * radiusx, cornery + height, nstepsHeight)
        
        return first.then(second).then(stick)
   
    def t(self, cornerx, cornery, radiusx=None, radiusy=None, height=None, width=None, nstepsHeight=None, nstepsCurve=None, nstepsDash=None):
        radiusx = radiusx or self.master_dimension / 4
        radiusy = radiusy or self.master_dimension / 4
        height = height or self.master_dimension * 7 / 4
        width = width or self.master_dimension * 0.8
        nstepsHeight = nstepsHeight or height / 2
        nstepsDash = nstepsDash or width / 2
        nstepsCurve = nstepsCurve or 2 * self.radiusx
        centerx = cornerx + radiusx
        centery = cornery + height
        endi = radiusx
        stepi = endi / nstepsCurve

        stick = Line(cornerx, cornery, cornerx, cornery + height, nstepsHeight)
        curve = SemiEllipse(centerx, centery, radiusx, radiusy, 1, False, 0, stepi, endi)
        lying_stick = Line(centerx, centery + radiusy, centerx + width * 0.4, centery + radiusy, nstepsDash)
        dash = Line(cornerx + radiusx + width * 0.4 - width, cornery + height / 2, cornerx + radiusx + width * 0.4, cornery + height / 2, nstepsDash)

        return stick.then(curve).then(lying_stick).then(dash)
    
    def u(self, cornerx, cornery, radiusx=None, radiusy=None, height=None, nstepsHeight=None, nstepsCurve=None):
        radiusx = radiusx or self.radiusx * 0.8
        radiusy = radiusy or self.radiusy
        height = height or 2 * self.radiusy
        nstepsHeight = nstepsHeight or self.height / 2
        nstepsCurve = nstepsCurve or 8 * self.radiusx
        centerx = cornerx + radiusx
        centery = cornery + radiusy
        endi = 2 * radiusx
        stepi = endi / nstepsCurve

        first = Line(cornerx, cornery, cornerx, cornery + height - radiusy, nstepsHeight * (height - radiusy) / height)
        curve = SemiEllipse(centerx, centery, radiusx, radiusy, 1, False, 0, stepi, endi)
        second = Line(cornerx + 2 * radiusx, cornery, cornerx + 2 * radiusx, cornery + height - radiusy, nstepsHeight)
        tail = SemiEllipse(centerx + 1.5 * radiusx, centery, radiusx / 2, radiusy, 1, False, 0, stepi, endi / 4)
        
        return first.then(curve).then(second).then(tail)
    
    def v(self, cornerx, cornery, height=None, width=None, nsteps=None):
        height = height or self.master_dimension
        width = width or self.master_dimension * 0.75
        nsteps = nsteps or height
        
        first = Line(cornerx, cornery, cornerx + width / 2, cornery + height, nsteps)
        second = Line(cornerx + width / 2, cornery + height, cornerx + width, cornery, nsteps)
        
        return first.then(second)

    def w(self, cornerx, cornery, height=None, width=None, nsteps=None):
        height = height or self.master_dimension
        width = width or self.master_dimension * 7 / 6
        nsteps = nsteps or height
        
        first = Line(cornerx, cornery, cornerx + width * 0.25, cornery + height, nsteps)
        second = Line(cornerx + width * 0.25, cornery + height, cornerx + width * 0.5, cornery + height / 3, nsteps)
        third = Line(cornerx + width * 0.5, cornery + height / 3, cornerx + width * 0.75, cornery + height, nsteps)
        fourth = Line(cornerx + width * 0.75, cornery + height, cornerx + width, cornery, nsteps)
        
        return first.then(second).then(third).then(fourth)

    def x(self, cornerx, cornery, height=None, width=None, nsteps=None):
        height = height or self.master_dimension
        width = width or self.master_dimension * 0.75
        nsteps = nsteps or height
        
        first = Line(cornerx, cornery, cornerx + width, cornery + height, nsteps)
        second = Line(cornerx + width, cornery, cornerx, cornery + height, nsteps)
        
        return first.then(second)

    def y(self, cornerx, cornery, radiusx=None, radiusy=None, height=None, nstepsHeight=None, nstepsCurve=None, nstepsTail=None):
        radiusx = radiusx or self.radiusx
        radiusy = radiusy or self.radiusy * 2
        height = height or self.master_dimension * 2
        nstepsHeight = nstepsHeight or self.height / 2
        nstepsCurve = nstepsCurve or 8 * self.radiusx
        centerx = cornerx + radiusx
        centery = cornery
        endiCurve = 2 * radiusx
        stepiCurve = endiCurve / nstepsCurve
        nstepsTail = nstepsTail or height * 5 / 12
        stepiTail = 0.25

        curve = SemiEllipse(centerx, centery, radiusx, radiusy, 1, False, 0, stepiCurve, endiCurve)
        tail = Parabola(centerx + radiusx * 1.2, centerx - radiusx * 7 / 4, cornery - radiusx * 1.1, height + radiusx * 1.1, centerx + radiusx, -1, nstepsTail, stepiTail)
        
        return curve.then(tail)

    def z(self, cornerx, cornery, height=None, width=None, nsteps=None):
        height = height or self.master_dimension
        width = width or self.master_dimension * 0.75
        nsteps = nsteps or height
        
        first = Line(cornerx, cornery, cornerx + width, cornery, nsteps)
        second = Line(cornerx + width, cornery, cornerx, cornery + height, nsteps)
        third = Line(cornerx, cornery + height, cornerx + width, cornery + height, nsteps)
        
        return first.then(second).then(third)
