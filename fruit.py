import pygame, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self, screen, cell_number, cell_size, apple):
        self.screen = screen
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.apple = apple
        
        self.x = random.randint(0, self.cell_number - 1)
        self.y = random.randint(0, self.cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * self.cell_size), int(self.pos.y * self.cell_size), self.cell_size, self.cell_size)
        self.screen.blit(self.apple, fruit_rect)
        #pygame.draw.rect(screen, pygame.Color('red'), fruit_rect)
        
    def randomize(self):
        self.x = random.randint(0, self.cell_number - 1)
        self.y = random.randint(0, self.cell_number - 1)
        self.pos = Vector2(self.x, self.y)
