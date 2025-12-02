from Chainable import Chainable

class Logger(Chainable):
    def __init__(self, end):
        self.end = end

    def update(self, i):
        print(f"Inside iteration {i}/{self.end}")
        if i >= self.end:
            self.done = True

ten = Logger(10)
twenty = Logger(20)

chain = ten.then(twenty)

for i in range(20):
    chain.update(i)

import pygame
from Letters import SemiEllipse, Line, Parabola, Config, Letter

pygame.init()
width, height = 1000, 600
Display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chainable")
clock=pygame.time.Clock()
x, y = 0, 0

config = Config(master_dimension=60, radiusx=30, radiusy=30, height=120)
letter = Letter(config)

a = letter.a(50, 80)
b = letter.b(150, 80)
c = letter.c(240, 80)
d = letter.d(320, 80)
h = letter.h(420, 80)
i = letter.i(500, 100, 5)
l = letter.l(540, 20)
m = letter.m(570, 80)
n = letter.n(690, 80)
o = letter.o(770, 80)
p = letter.p(860, 80)
q = letter.q(50, 230)
t = letter.t(150, 170)
u = letter.u(220, 230)
v = letter.v(310, 230)
w = letter.w(390, 230)
x = letter.x(490, 230)
y = letter.y(570, 230)
z = letter.z(660, 230)

chain = Chainable()

chain = a.then(b).then(c).then(d).then(h).then(i)
chain = chain.then(l).then(m).then(n).then(o).then(p)
chain = chain.then(q).then(t).then(u).then(v).then(w)
chain = chain.then(x).then(y).then(z)

try:
    Display.fill('grey')
    done = False
    while not done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = True
                break

        coord = chain.update()
        if coord:
            print(coord)
            pygame.draw.circle(Display, "#732f14", coord, 8)
        pygame.display.flip()
        clock.tick(600)

finally:
    pygame.quit()