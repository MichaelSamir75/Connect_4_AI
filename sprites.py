import pygame
from settings import *

pygame.font.init()


class Cell(pygame.sprite.Sprite):
    def __init__(self, game, x, y, cell, isSelected = False):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((cell_size, cell_size))
        self.x, self.y = x, y
        self.cell = cell
        self.isSelected = isSelected
        self.rect = pygame.draw.circle(self.image, BGCOLOUR, (cell_size/2, cell_size/2), cell_size/2.2)

        if(self.isSelected):
            self.image.fill(GREY)
        else:
            self.image.fill(LIGHTGREY)

        if(self.cell == 0):
            self.rect = pygame.draw.circle(self.image, BGCOLOUR, (cell_size/2, cell_size/2), cell_size/2.2)

        elif self.cell == 1:
            self.rect = pygame.draw.circle(self.image, PLAYER1, (cell_size/2, cell_size/2), cell_size/2.2)

        elif self.cell == 2:
            self.rect = pygame.draw.circle(self.image, PLAYER2, (cell_size/2, cell_size/2), cell_size/2.2)


    def update(self):
        self.rect.x = self.x * cell_size + WIDTH*15/100
        self.rect.y = self.y * cell_size + HEIGHT*15/100

    def select(self, mouse_x, mouse_y):
        if(self.rect.collidepoint(mouse_x,mouse_y)):
            self.image.fill(GREY)
            self.rect = pygame.draw.circle(self.image, PLAYER1, (cell_size/2, cell_size/2), cell_size/2.2)

    def click(self, mouse_x, mouse_y):
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.bottom


class UIElement:
    def __init__(self, x, y, text, color):
        self.x, self.y = x, y
        self.text = text
        self.color = color

    def set_color(self, color):
        self.color = color

    def draw(self, screen):
        font = pygame.font.Font("assets/FerroRosso.ttf", 26)
        text = font.render(self.text, True, self.color)
        screen.blit(text, (self.x, self.y))
