from pyglet.gl import *


class Boundary:
    def __init__(self, x1, y1, x2, y2):
        self.a = (x1,y1)
        self.b = (x2,y2)
        
    def draw(self):
        vertices = [self.a[0], self.a[1], self.b[0], self.b[1]]

        # Set the line width
        glLineWidth(5.0)  # Set the line width to 5 pixels

        # Begin drawing lines
        glBegin(GL_LINES)
        # Set line color
        glColor3f(255, 255, 255)  # Black color
        # Define line vertices
        glVertex2f(vertices[0], vertices[1])
        glVertex2f(vertices[2], vertices[3])
        glEnd()


'''
2                : The number of vertices in the line (two endpoints).
GL_LINES         : Specifies the type of primitive to render, which in this case is a line.
self.group       : An instance of pyglet.graphics.OrderedGroup to manage rendering order.
('v2f', vertices): A tuple that defines the format of vertex coordinates. 'v2f' indicates that the vertices are in 2D float format.
('c3B', colors)  : A tuple that defines the format of colors. 'c3B' indicates that the colors are in RGB format with 3 bytes per color.

'''
