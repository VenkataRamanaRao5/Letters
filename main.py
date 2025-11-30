from Letters.Chainable import Chainable

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