import pygame
from pygame.locals import *
from game_page import Game
from settings import *
from start_page import Start

pygame.init()

class main():
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

    def main(self):
        run = True
        clock = pygame.time.Clock()
        game_page = Game(self.screen)
        start_page = Start(self.screen)
        start_page.set_next_page(game_page)
        game_page.set_next_page(start_page)

        while run:
            clock.tick(FPS)
            if(start_page.checkUpdate()):
                start_page.events()
                start_page.draw()
            
            if(game_page.checkUpdate()):
                game_page.update()
                game_page.events()
                game_page.draw()
            
            pygame.display.update()

if __name__ == "__main__":
    main = main()
    main.main()
    pygame.quit()