import pygame
from pygame import Vector2

class Wall:

    '''
    Wall class: walls that can be placed on the screen.
    '''

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def show(self, screen):
        '''
        Display the wall on the screen.
        
        :param screen: pygame screen
        :type screen: pygame.Surface
        '''
        pygame.draw.line(screen, (0,0,0), self.start, self.end, 3)
