
# import sys module
import pygame
  
pygame.init()

class input_box:
    def __init__(self,font,width,height,pos):
            #the text and font
            self.base_font = font
            self.user_text = ''

            # create rectangle
            self.input_rect = pygame.Rect(pos,(width,height))

            # color_active stores color(lightskyblue3) which
            # gets active when input box is clicked by user
            self.color_active = pygame.Color('lightskyblue3')

            # color_passive store color(chartreuse4) which is
            # color of input box.
            self.color_passive = pygame.Color('chartreuse4')
            self.color = self.color_passive
            self.active = False

    def get_text(self):
        return self.user_text
        
    def set_text(self, text):
        self.user_text = text

    def check_event(self,event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_rect.collidepoint(event.pos):
                    self.active = True
                else:
                    self.active = False
            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    self.user_text = self.user_text[:-1]

                # Unicode standard is used for string
                # formation
                else:
                    self.user_text += event.unicode

    def draw(self,screen):
        if self.active:
            color = self.color_active
        else:
            color = self.color_passive

        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(screen, color, self.input_rect, 0, 10)

        text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))

        # render at position stated in arguments
        screen.blit(text_surface, (self.input_rect.x+5, self.input_rect.y+5))

        # set width of textfield so that text cannot get
        # outside of user's text input
        self.input_rect.w = max(self.input_rect.w, text_surface.get_width()+10)

