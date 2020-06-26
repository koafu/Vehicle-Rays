import pygame
from pygame import Vector2
from math import degrees, atan2

class Ray:

    '''
    Ray class: rays used on the vehicle that detect obstacles and return
    the intersection point.
    '''

    def __init__(self, pos, angle, length):
        self.pos = pos
        self.angle = angle
        self.dir = pos.rotate(self.angle)

        self.length = length # length of the ray
        self.detect = False # bool for when a obstacle is detected

    def update(self, vel):
        '''
        Update the orientation of the ray based on the velocity vector
        of the vehicule.

        :param vel: velocity vector of the vehicule
        :type vel: pygame.math.Vector2
        '''

        if vel.magnitude() == 0:
            return

        self.dir = vel.rotate(self.angle).normalize()

    def cast(self, walls):
        '''
        Cast the ray and return intersection point between the ray 
        and the obstacle if detected.

        :param walls: list of all the walls on the screen
        :type walls: list
        '''

        walls_detected = 0

        for wall in walls:
            x1 = wall.start.x
            y1 = wall.start.y
            x2 = wall.end.x
            y2 = wall.end.y
            x3 = self.pos.x
            y3 = self.pos.y
            x4 = self.pos.x + self.dir.x * self.length
            y4 = self.pos.y + self.dir.y * self.length

            denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if denominator == 0:
                continue

            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
            u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator

            if t > 0 and t < 1 and u > 0 and u < 1:
                pt = Vector2(x1 + t * (x2 - x1), y1 + t * (y2 - y1)) # intersection point
                self.detect = True
                walls_detected += 1
                break

        if walls_detected == 0:
            self.detect = False

    def show(self, screen):
        '''
        Display the ray on the screen according to its direction.
        
        :param screen: pygame screen
        :type screen: pygame.Surface
        '''

        if self.detect:
            pygame.draw.line(screen, (255,0,0), self.pos,
                    (self.pos.x + self.dir.x * self.length,
                    self.pos.y + self.dir.y * self.length), 2)
        else:
            pygame.draw.line(screen, (140,160,185), self.pos,
                    (self.pos.x + self.dir.x * self.length,
                    self.pos.y + self.dir.y * self.length), 2)
