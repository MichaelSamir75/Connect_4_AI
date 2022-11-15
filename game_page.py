import pygame
import time
from settings import *
from sprites import *
from button import Button
from text_box import input_box
from MinimaxBruning import mimimax_bruning_algorithm
from Minimax import mimimax_algorithm
from heuristic import heuristic
class Game():

    def __init__(self,screen):
        self.screen = screen
        self.screen.fill(BGCOLOUR)
        self.current = False
        self.font = pygame.font.Font(None,30)

        self.button_new = Button('New game',self.font,button_width,button_height,(10*100/WIDTH,HEIGHT-20/100*HEIGHT),5,self.new)
        self.button_depth = Button('Update depth',self.font,button_width*1.3,button_height,(10*100/WIDTH,HEIGHT-20/100*HEIGHT+1.2*button_height),5,self.new)
        self.input_depth = input_box(self.font,(button_width*2),button_height*1.1,(10*100/WIDTH + 1.4*button_width,HEIGHT-20/100*HEIGHT+1.1*button_height))
        
        self.depth = 4

        self.score1 = 0
        self.score2 = 0
        self.show_time = 0

        self.algorithm = mimimax_bruning_algorithm()
        self.new()


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
                            if(self.make_move(row,col)):
                                self.player = False
                                self.score1 = heuristic().getScore(self.game_grid,2)
                                self.draw_cells()
                                self.all_sprites.update()
                                self.all_sprites.draw(self.screen)
        self.button_new.check_click()
        self.button_depth.check_click()

    def solve(self):
        self.game_grid = self.algorithm.solve(self.game_grid,self.depth)

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.game_grid = self.create_game()
        self.player = True
        self.input_depth.set_text(str(self.depth))
        self.draw_cells()
    
    def make_move(self,row, col):
        for i in range(ROWS-1,row-1, -1):
            if(self.game_grid[i][col] == 0):
                self.game_grid[i][col] = 2
                return True
        return False

    def update(self):
        self.all_sprites.update()
        self.draw()
        if(not self.player):
            self.show_time = time.time()
            print(self.show_time )
            self.solve()
            self.player = True
        if((time.time()-self.show_time) >= 0.5):
            self.draw_cells()
            self.score2 = heuristic().getScore(self.game_grid,1)
            self.all_sprites.update()
            self.show_time = time.time()

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
            UIElement(2/100*WIDTH, 15/100*HEIGHT, "Player", RED).draw(self.screen)
            UIElement(87/100*WIDTH, 15/100*HEIGHT, "Robot", BLACK).draw(self.screen)
        else:
            UIElement(2/100*WIDTH, 15/100*HEIGHT, "Player", BLACK).draw(self.screen)
            UIElement(87/100*WIDTH, 15/100*HEIGHT, "Robot", RED).draw(self.screen)
        UIElement(7/100*WIDTH, 19/100*HEIGHT, str(self.score1), BLACK).draw(self.screen)
        UIElement(92/100*WIDTH, 19/100*HEIGHT, str(self.score2), BLACK).draw(self.screen)
        pygame.draw.circle(self.screen, PLAYER1, (4/100*WIDTH, 20/100*HEIGHT), cell_size/5)
        pygame.draw.circle(self.screen, PLAYER2, (89/100*WIDTH, 20/100*HEIGHT), cell_size/5)
    
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