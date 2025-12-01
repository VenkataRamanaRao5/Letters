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

chain = a.then(b).then(c).then(d)

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
        clock.tick(200)

finally:
    pygame.quit()