from pyglet.window import key
import pyglet 
from boundary import Boundary
from particles import Particles
import random

class Space:
    def __init__(self):
        self.window = pyglet.window.Window(fullscreen=True)
        self.batch = pyglet.graphics.Batch()
        self.window.push_handlers(on_draw=self.on_draw, on_key_press=self.on_key_press,
                                  on_mouse_motion=self.on_mouse_motion)
        self.mouse_x = 600
        self.mouse_y = 110
        self.lines = []
        
        self.particles = Particles(self.window.width, self.window.height)
        
        pyglet.clock.schedule_interval(self.update, 1 / 20.0)  # Update 20 times per second        
        # pyglet.clock.schedule_interval(self.setup, 1 / 10.0)  # Update 20 times per second        

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.setup(22)
            
    def setup(self,dt=12):
        self.lines = []
        for i in range(4):
            x1 = random.randint(0,self.window.width)
            x2 = random.randint(0,self.window.height)            
            x3 = random.randint(0,self.window.width)
            x4 = random.randint(0,self.window.height)            

            self.lines.append(Boundary(x1, x2, x3, x4))

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y

    def update(self, dt):
        self.batch = pyglet.graphics.Batch()
        self.particles.update(self.lines, (self.mouse_x, self.mouse_y))
    
    def call_draw(self):
        for line in self.lines:
            line.draw()
        self.particles.show(self.batch)
        
    def on_draw(self):
        self.window.clear()
        self.call_draw()
    
    def run(self):
        pyglet.app.run()

if __name__ == "__main__":
    space = Space()
    space.run()
