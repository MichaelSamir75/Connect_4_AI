import pygame, sys

class Button:
	def __init__(self,text,font,width,height,pos,elevation,function):
        #declare some variables
		self.enabled = True
		self.font = font
		self.function = function
		self.click_sound = pygame.mixer.Sound("assets/blipshort1.wav")
        
		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.elevation_enable = elevation
		self.elevation_disable = 2
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#475F77'

		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#354B5E'
		#text
		self.text = text
		self.text_surf = self.font.render(text,True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def change_text(self, newtext):
		self.text_surf = self.font.render(newtext, True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def draw(self,screen):
		self.screen = screen
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos) and self.enabled:
			self.top_color = '#D74B4B'
            
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
				self.change_text(f"{self.text}")
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					self.function()
					self.click_sound.play()
					self.pressed = False
					self.change_text(self.text)
		elif(self.enabled):
			self.dynamic_elecation = self.elevation
			self.top_color = '#475F77'

	def enable(self):
		self.enabled = True
		self.top_color = '#475F77'
		self.elevation = self.elevation_enable

	def disable(self):
		self.enabled = False
		self.top_color = '#203243'
		self.elevation = self.elevation_disable

	def press(self):
		self.enabled = False
		self.top_color = (200,0,0)
		self.elevation = self.elevation_disable

pygame.init()

