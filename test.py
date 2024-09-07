import pyglet
from pyglet.gl import *

# Initialize a window
window = pyglet.window.Window(800, 600, "Thick Line Example")

@window.event
def on_draw():
    # Clear the window
    window.clear()
    
    # Set the line width
    glLineWidth(2.0)  # Set the line width to 5 pixels

    # Begin drawing lines
    glBegin(GL_LINES)
    # Set line color
    glColor3f(255, 255, 255)  # Black color
    # Define line vertices
    glVertex2f(100, 100)
    glVertex2f(700, 500)
    glEnd()

# Run the Pyglet application
pyglet.app.run()
