from typing import *

"""
This class is meant to provide functionality to chain updates 
to event loops using a `then` method. 
First, create a subclass and implement the `update` method.
Then, create an instance of the subclass and call `update` on it
when needed. If you need to chain multiple updates based on some
done condition, say, a.update() for 10 iterations and b.update()
for 10 iterations, you can create a Chainable ch = a.then(b) and 
then call ch.update(). This is infinitely chainable, meaning you
can write a1.then(a2).then(a3).... Set done inside `update` to
indicate the control should flow to next Chainable instance.
"""
class Chainable:
    done = False

    """
    Executes one iteration of updation while inside the loop. Does
    not return anything, so implement the subclass to perform side
    effects as needed.

    Parameters
    ----------
    i : integer
      an integer that can optionally be passed to hold the 
      iteration counter variable

    Returns
    -------
    None
    """
    def update(self, i: Optional[int]) -> None:
        done = True

    """
    Return a Chainable instance on which when update is
    called, conditionally calls self.update first if 
    self.done is False, otherwise calls other.update
    if other.done is False. If both are True, sets its
    done as True. This takes in an Chainable and returns 
    a Chainable, so it can composed infinitely in any order.

    Parameters
    ----------
    other : Chainable
        the Chainable instance whose update should be 
        executed after self has marked as done

    Returns
    -------
    out: Chainable
        the chainable instance whose update method 
        conditionally calls update on self and other.
    """
    def then(self, other: 'Chainable') -> 'Chainable':
        def function(this, i: Optional[int]) -> None:
            if not self.done:
                self.update(i)
            elif not other.done:
                other.update(i)
            else:
                this.done = True
        
        chainedChain = Chainable()
        chainedChain.update = function.__get__(chainedChain)
        return chainedChain

        