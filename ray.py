import math
from pyglet.gl import *
from pyglet.graphics import OrderedGroup

class Ray:
    def __init__(self, pos, angle_radian):
        self.pos = pos
        self.angle = angle_radian
        self.dir = (math.cos(angle_radian), math.sin(angle_radian))
        self.line = None        
        self.x2 = pos[0] + self.dir[0] * 3
        self.y2 = pos[1] + self.dir[1] * 3
        self.group = OrderedGroup(0)

    def update_direction(self):
        self.dir = (math.cos(self.angle), math.sin(self.angle))
        self.x2 = self.pos[0] + self.dir[0] * 3
        self.y2 = self.pos[1] + self.dir[1] * 3

    def lookAt(self, x, y):
        x = x - self.pos[0]
        y = y - self.pos[1]
        self.dir = self.normalize_vector_2d(x, y)

    def normalize_vector_2d(self, x, y):
        magnitude = math.sqrt(x ** 2 + y ** 2)
        if magnitude == 0:
            return (0, 0)  # Avoid division by zero
        return (x / magnitude, y / magnitude)
    
    def cast(self, wall):
        x1, y1 = wall.a
        x2, y2 = wall.b
        x3, y3 = self.pos
        x4, y4 = self.x2, self.y2
                
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return None  # Lines are parallel or coincident
        
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = ((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
        
        if 0 <= t <= 1 and u <= 0:
            intersection_x = x1 + t * (x2 - x1)
            intersection_y = y1 + t * (y2 - y1)
            return (intersection_x, intersection_y)
        else:
            return None  # No valid intersection

    def show(self, batch):
        vertices = [self.pos[0], self.pos[1], self.x2, self.y2]
        colors = (255, 255, 255) * 2  # Each vertex needs a color
        # Set the line width
        glLineWidth(1.0)  # Set the line width to 5 pixels

        # Begin drawing lines
        glBegin(GL_LINES)
        # Set line color
        glColor3f(255, 255, 255)  # Black color
        # Define line vertices
        glVertex2f(vertices[0], vertices[1])
        glVertex2f(vertices[2], vertices[3])
        glEnd()
