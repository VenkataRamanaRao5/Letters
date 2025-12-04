## What is this?
This repository contains python code to draw letters using pygame. I know we can just print text onto the screen, but I want the effect of drawing them point by point. This is done in two parts: first, I wrote the `Chainable` class to be able to chian multiple different update functions easily and then the `Letter` class to first build basic strokes of line, semi-ellipse and parabola and use the `Chainable` class to put together each letter.

The ability to chain update functions is imperative. I'll explain what I precisely mean by chaining update functions. 
- When you are drawing a letter, it consists of multiple strokes. For instance, you need to draw a line and then a circle to draw the letter 'b'. Point number 1.
- Pygame works with an game loop. You typically have three parts to the game loop: 
  1. event handling
  2. logic handling and updates
  3. rendering
  The co-ordinate updates are usually done per frame, the entire loop runs for each frame and render part renders it. When you are drawing something, you need to update the co-ordinates in each iteration. You cannot have a single function that performs this atomically. Perhaps you can, but you need to have the clock update and rendering logic inside each update function. 

- Either have rendering inside the function or return the co-ordinates as a list, concatenate the list and iterate over the big list. That's the only straightforward way to logically separate the different update parts. Unless you're willing to build an if-else ladder at the update part. Point number 3.

## Chainable class
To solve this issue, I wrote the `Chainable` class which provides you an `update` and `then` method. `then` method takes another `Chainable` instance as an argument and returns a new `Chainable` instance. You create a subclass for your required stroke or chain of strokes and implement the update function. 

Consider drawing a line. 
```python
class Line(Chainable):
    def __init__(self, ...):
        pass
    def update(self, iteration_counter):
        ...
        if condition:
            self.done = True
        return x, y 
```

Now, you can create a bunch of lines like below 
```python
chain = Line(...).then(Line(...)).then(Line(...))...
```

Inside the game loop
```python
while not done:
    # event loop
    x, y = chain.update()
    # rendering
```

As simple as that. If not, it calls its update method. If yes, it sets `self.done` to `True`. In this case, we first call the first line's update method until it's done; then we call second's line's update and so on. This chaining is accomplished by the `then` method. Inside `then`, we build and return a new `Chainable` instance `result`. We first define a function with `self` and `other` as arguments. It first checks first line has set `done` to `True`. If not, it calls its update method. If yes, it checks if other has set `done` to `True`. We attach this function as bounded method to result.update and we return result as the new instance.

## How is this useful? 
1. We can define primitive strokes and reuse them extremely easily in letters like below
```python
class Line(Chainable):
    ...
class SemiEllipse(Chainable):
    ...
class LetterB(Chainable):
    def update(...):
        # configuration of radii and lengths
        return Line(...).then(SemiEllipse(...)).then(SemiEllipse(...))
```
    Just like that. It takes a lot of configuration of radii, heights ad co-ordiantes but that's the only part you need to worry about. You need not handle the drawing multiple times. Write line once, semi ellipse once and just chain them!

2. When you want to write multiple letters - and all this is pretty useless if you don't - you can chain letters like below
```python
h = LetterA(...)
o = LetterO(...)
w = LetterW(...)
d = LetterD(...)
y = LetterY(...)

howdy = h.then(o).then(w).then(d).then(y)

while not done:
    # event loop
    x, y = howdy.update()
    # rendering
```
    That's it! You needn't bother about transferring the control from one letter to another. One instance, one update call, you are done.

3. All letters are implemented (or will be, in the future), so you can write any word or any combination of letters you want. All letters are written in such a way that you only need to provide the configuration of length once and all the letters will follow it. In each individual letter, you only need to provide the top-left corner co-ordinates. Details will be provided in a separate documentation for the letters.

4. Since `chainable.then` return another `Chainable` instance, it is associative. For instance, `c1.then(c2).then(c3)` is equivalent to `c1.then(c2.then(c3))`

Here's a demo video of all the letters implemented so far in a single chain. This is recording of the pygame window of `main.py`

[demo.mp4](output2.mp4)