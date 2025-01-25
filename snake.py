import pygame
from pygame.math import Vector2

class SNAKE:
    def __init__(self, screen, cell_size):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False
        self.crunc_sound = pygame.mixer.Sound('Sounds/crunch.wav')
        self.screen = screen
        self.cell_size = cell_size
    
    def draw_snakes(self):
        for block in self.body:
            x_pos = int(block.x * self.cell_size)
            y_pos = int(block.y * self.cell_size)
            snake_rect = pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, pygame.Color('blue'), snake_rect)
        
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
        
    def add_block(self):
        self.new_block = True
        
    def play_crunch_sound(self):
        self.crunc_sound.play()
        
    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)# -*- coding: utf-8 -*-

