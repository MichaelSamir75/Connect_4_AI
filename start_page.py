import pygame
from settings import *
from button import Button

#class responsible for start page
class Start():
    def __init__(self,screen):
        self.screen = screen
        self.screen.fill(BGCOLOUR)
        self.font = pygame.font.Font(None,30)
        self.button_next = Button('Play',self.font,button_width,button_height,(WIDTH/2-button_width/2,HEIGHT-10/100*HEIGHT),5,self.change_state)
        self.current = True

    def checkUpdate(self):
        pass
        return self.current

    def set_next_page(self, page):
        self.page = page

    def change_state(self):
        self.page.current = True
        self.current = False
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_SPACE):
                    self.page.current = True
                    self.current = False
            
        self.button_next.check_click()

    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.button_next.draw(self.screen)
        self.create_text()
        self.show_us()
        self.show_rules()


    def show_us(self):
        font_powered = pygame.font.Font("assets/FerroRosso.ttf", 30)
        font_names = pygame.font.Font("assets/arial_narrow_7.ttf", 20)
        names = "1-Mohamed Salama\n\
2-Mohamed Aiad\n\
3-Ahmed Abdallah\n\
4-Michael Samir\n"
        text_powered = font_powered.render("Powered by:", True, "#475F77")
        self.screen.blit(text_powered,(WIDTH/1.4,HEIGHT/1.2,WIDTH,50))
        self.blit_text(self.screen, names, (WIDTH/1.4,HEIGHT/1.15), font_names, (0,0,0))

    def show_rules(self):
        font_rules = pygame.font.Font("assets/FerroRosso.ttf", 40)
        font_text = pygame.font.Font("assets/times new roman.ttf", 25)

        text = "Connect 4 is a two-player game in which the players first choose a color and then take turnsdropping their colored discs from the top into a grid.\n\
The pieces fall straight down, occupyingthe next available space within the column.\n\
The objective of the game is to connect-four ofone’s own discs of the same color next to each other vertically, horizontally, or diagonally.\n\
The two players keep playinguntil the board is full. The winner is the player having greater number of connected-fours."

        #show example image
        puzzle_image = pygame.image.load("assets/c4.png")
        puzzle_image = pygame.transform.scale(puzzle_image, (puzzle_image.get_width()*0.5, puzzle_image.get_height()*0.5))
        imagerect = puzzle_image.get_rect()
        puzzle_image.convert()
        self.screen.blit(puzzle_image, (WIDTH/2-puzzle_image.get_width()/2,HEIGHT-puzzle_image.get_height()-150))


        text_rules = font_rules.render("Rules:", True,  "#475F77")
        self.screen.blit(text_rules,(10,HEIGHT/7,WIDTH,50))
        self.blit_text(self.screen, text, (10,HEIGHT/7+50), font_text, (0,0,0))

    
    def blit_text(self, surface, text, pos, font, color=pygame.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
    
    #write welcome message
    def create_text(self):
        color = "#475F77"
        self.rect_title = pygame.Rect((0,50,WIDTH,20))
        font = pygame.font.Font("assets/Arcade.ttf", 75)
        text_title = font.render("CONNECT 4", True, color)
        text_rect = text_title.get_rect(center=self.rect_title.center)
        self.screen.blit(text_title,text_rect)