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
from Letters import SemiEllipse, Line, Parabola

pygame.init()
width, height = 1000, 600
Display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chainable")
clock=pygame.time.Clock()
x, y = 0, 0

first = SemiEllipse(200, 200, 30, 30, -1, isTop=True)
second = SemiEllipse(200, 200, 30, 30, 1, isTop=False)
third = SemiEllipse(260, 200, 30, 30, 1, isTop=True)
fourth = SemiEllipse(260, 200, 30, 30, -1, isTop=False)

circle = first.then(second).then(third).then(fourth)

left = Line(300, 330, 300, 270, 30)
right = Line(360, 270, 360, 330, 30)
top = Line(300, 270, 360, 270, 30)
bottom = Line(360, 330, 300, 330, 30)
backslash = Line(300, 330, 360, 270, 60)

square = left.then(top).then(right).then(bottom).then(backslash)

openUp = Parabola(200, 260, 360, 60, 200, 1, 60, 0.5)
openDown = Parabola(200, 260, 360, -30, 260, -1, 30, 1)

chain = circle.then(square).then(openUp).then(openDown)

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
            pygame.draw.circle(Display, "#732f14", coord, 8)
        pygame.display.flip()
        clock.tick(60)

finally:
    pygame.quit()