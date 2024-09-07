import math 
from ray import Ray

class Particles:
    def __init__(self, width, height):
        self.pos = (width // 2, height // 2)
        self.rays = []
        for a in range(0, 360, 1):
            angle_radian = -math.radians(a)
            self.rays.append(Ray(self.pos, angle_radian))

    def show(self, batch):
        for ray in self.rays:
            ray.show(batch)

    def cast(self, walls):

        for ray in self.rays:
            ray.pos = self.pos  # Update ray position to match particle position
            ray.update_direction()  # Ensure ray direction is updated

            closest = None
            min_dist = float('inf')
            for wall in walls:
                cast = ray.cast(wall)
                if cast:
                    dist = math.sqrt((cast[0] - ray.pos[0]) ** 2 + (cast[1] - ray.pos[1]) ** 2)
                    if dist < min_dist:
                        min_dist = dist
                        closest = cast

            if closest:
                ray.x2 = closest[0]
                ray.y2 = closest[1]
            else:
                ray.x2 = self.pos[0] + math.cos(ray.angle) * 1000  # Extend ray if no collision
                ray.y2 = self.pos[1] + math.sin(ray.angle) * 1000
        
    def update(self, walls, m_pos):
        self.pos = m_pos
        self.cast(walls)  # Ensure the cast method is called to update ray positions
