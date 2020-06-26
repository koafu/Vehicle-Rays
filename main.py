import pygame
from pygame import Vector2
from vehicle import Vehicle
from wall import Wall
from random import randint

class Main:

    '''
    Main class: acts as the gameloop.
    '''

    def __init__(self):
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ray Vehicles")
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.exit = False
        self.background = 88,88,95

    def run(self):
        '''
        Run project.
        '''

        vehicle = Vehicle(self.width / 2, self.height / 2)
        
        n_walls = 10
        # place random walls across the screen
        walls = [Wall(Vector2(randint(0, self.width), randint(0, self.height)), 
            Vector2(randint(0, self.width), randint(0, self.height))) for n in range(n_walls)]

        while not self.exit:

            self.screen.fill(self.background)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            mx, my = pygame.mouse.get_pos()
            vehicle.seek(Vector2(mx,my))
            vehicle.update(walls)
            vehicle.show(self.screen)

            for wall in walls:
                wall.show(self.screen)

            self.clock.tick(self.fps)
            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    sim = Main()
    sim.run()
