import pygame
from pygame import Vector2
from math import atan2, degrees
from ray import Ray

class Vehicle:

    '''
    Vehicle class : handles the movement of the vehicle and
    the displaying of the vehicle on the screen.
    '''

    def __init__(self, x, y):
        self.pos = Vector2(x,y)
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)

        self.max_speed = 5
        self.max_force = 0.169
        self.r = 100 # length of the rays

        self.img = pygame.image.load("boid.png").convert()
        self.img = pygame.transform.scale(self.img, (40,20))
        self.img.set_colorkey((0,0,0))

        # the angle and the amount of rays can be changed by changing the range
        self.rays = [Ray(self.pos, angle, self.r) for angle in range(-135, 180, 45)]

    def update(self, walls):
        '''
        Update the position of the vehicle.

        :param walls: list of all the walls on the screen
        :type walls: list
        '''

        self.vel += self.acc
        self.limit_speed()
        self.pos += self.vel
        self.acc *= 0

        for ray in self.rays:
            ray.update(self.vel)
            ray.cast(walls)

    def limit_speed(self):
        '''
        Limits the speed of the vehicle.
        '''

        if self.vel.magnitude() > self.max_speed:
            self.vel.scale_to_length(self.max_speed)

    def limit_force(self, force):
        '''
        Limits the strength of a given force.

        :param force: force that acts upon the vehicle
        :type force: pygame.math.Vector2
        '''

        if force.magnitude() > self.max_force:
            force.scale_to_length(self.max_force)

    def seek(self, target):
        '''
        Seek a given target.

        :param target: position of the target
        :type target: pygame.math.Vector2
        '''

        desired = target - self.pos
        desired.scale_to_length(self.max_speed)
        steering = desired - self.vel
        self.limit_force(steering)
        self.acc += steering

    def show(self, screen):
        '''
        Rotates the image around its center according to the velocity vector
        and displays it on the screen.
        
        :param screen: pygame screen
        :type screen: pygame.Surface
        '''

        for ray in self.rays:
            ray.show(screen)

        angle = -degrees(atan2(self.vel.y, self.vel.x))
        img_copy = pygame.transform.rotate(self.img, angle)
        screen.blit(img_copy, (int(self.pos.x - img_copy.get_width() / 2),
            int(self.pos.y - img_copy.get_height() / 2)))