import pygame
import numpy as np
from settings import *
from sprites import *
from button import Button
from text_box import input_box

class Game():

    def __init__(self,screen):
        self.screen = screen
        self.screen.fill(BGCOLOUR)
        self.current = False
        self.font = pygame.font.Font(None,30)

        self.new()
        self.button_new = Button('New game',self.font,button_width,button_height,(10*100/WIDTH,HEIGHT-20/100*HEIGHT),5,self.new)
        self.button_depth = Button('Update depth',self.font,button_width*1.3,button_height,(10*100/WIDTH,HEIGHT-20/100*HEIGHT+1.2*button_height),5,self.new)
        self.input_depth = input_box(self.font,(button_width*2),button_height*1.1,(10*100/WIDTH + 1.4*button_width,HEIGHT-20/100*HEIGHT+1.1*button_height))

        self.depth = 7

        self.score1 = 0
        self.score2 = 0

    def checkUpdate(self):
        return self.current

    def set_next_page(self, page):
        self.page = page

    def events(self):
        for event in pygame.event.get():
            self.input_depth.check_event(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_SPACE):
                    self.page.current = True
                    self.current = False
                
            if event.type == pygame.MOUSEBUTTONDOWN and self.player:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for row, cells in enumerate(self.cells):
                    for col, cell in enumerate(cells):
                        if cell.click(mouse_x, mouse_y):
                            print("a7aaaaaaa")
                            self.player = not self.make_move(row,col)
                            self.draw_cells()

        self.button_new.check_click()
        self.button_depth.check_click()
    
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.game_grid = self.create_game()
        self.player = True
        self.draw_cells()
    
    def make_move(self,row, col):
        for i in range(ROWS-1,row-1, -1):
            print(i)
            if(self.game_grid[i][col] == 0):
                print(i, col)
                self.game_grid[i][col] = 1
                return True
        return False

    def update(self):
        self.all_sprites.update()
    
    def create_game(self):
        grid = [[0 for i in range(COLUMNS)] for j in range(ROWS)]
        return grid
    
    #write title
    def create_text(self):
        color = "#475F77"
        self.rect_title = pygame.Rect((0,50,WIDTH,20))
        font = pygame.font.Font("assets/Arcade.ttf", 75)
        text_title = font.render("CONNECT 4", True, color)
        text_rect = text_title.get_rect(center=self.rect_title.center)
        self.screen.blit(text_title,text_rect)
    
    def draw_grid(self):
        color = ("#475F77")
        for col in range(-1, (ROWS+1) * cell_size, cell_size):
            pygame.draw.line(self.screen, color, (col+15/100*WIDTH, 15/100*HEIGHT), (col+15/100*WIDTH, ROWS * cell_size+15/100*HEIGHT), 4)
        for row in range(0, COLUMNS * cell_size, cell_size):
            pygame.draw.line(self.screen, color, (15/100*WIDTH, row+15/100*HEIGHT), (COLUMNS * cell_size+ 15/100*WIDTH, row+15/100*HEIGHT), 4)

    def draw_cells(self):
        self.cells=[]
        grid = self.game_grid
        for row, x in enumerate(grid):
            self.cells.append([])
            for col, val in enumerate(x):
                self.cells[row].append(Cell(self, col, row, val))

    def draw_score(self):
        if(self.player):
            UIElement(2/100*WIDTH, 15/100*HEIGHT, "Player", GREEN).draw(self.screen)
            UIElement(87/100*WIDTH, 15/100*HEIGHT, "Robot", BLACK).draw(self.screen)
        else:
            UIElement(2/100*WIDTH, 15/100*HEIGHT, "Player", BLACK).draw(self.screen)
            UIElement(87/100*WIDTH, 15/100*HEIGHT, "Robot", GREEN).draw(self.screen)
        UIElement(2/100*WIDTH, 20/100*HEIGHT, str(self.score1), BLACK).draw(self.screen)
        UIElement(87/100*WIDTH, 20/100*HEIGHT, str(self.score2), BLACK).draw(self.screen)

    
    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.create_text()
        self.button_new.draw(self.screen)
        self.button_depth.draw(self.screen)
        self.input_depth.draw(self.screen)

        self.all_sprites.draw(self.screen)
        self.draw_grid()
        self.draw_score()
        pygame.display.flip()