import pygame.font
from pygame.sprite import Group

class Scoreboard():
    """class that creates a scoreboard"""
    
    def __init__(self,fp_settings,screen):
        """initialises scoreboard"""
        self.fp_settings = fp_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.score_msg = str(fp_settings.score)
        
        #font settings
        self.text_colour = (0,0,0)
        self.font = pygame.font.SysFont(None, 48)
        
        self.prep_score()
        
    def prep_score(self):
        """Turn score into a rendered image"""
        
        self.score_msg = str(self.fp_settings.score)
        self.score_image = self.font.render(self.score_msg, True, 
            self.text_colour,self.fp_settings.bg_colour)
            
        #display score at top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = self.screen_rect.top
        
    def show_score(self):
        """Display score on screen"""
        self.screen.blit(self.score_image, self.score_rect)
