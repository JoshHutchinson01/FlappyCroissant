import pygame.font
from pygame.sprite import Group

class HighScoreboard():
    """class that creates a high-score board"""
    
    def __init__(self,fp_settings,screen):
        """initialises a high score board"""
        self.fp_settings = fp_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.score_msg = "High score:" + str(fp_settings.high_score)
        
        #font settings
        self.text_colour = (0,0,0)
        self.font = pygame.font.SysFont(None, 48)
        
        self.prep_score()
        
    def prep_score(self):
        """Turn score into a rendered image"""
        
        #writes the new score message
        self.score_msg = "High score: " + str(self.fp_settings.high_score)
        
        #renders the image
        self.score_image = self.font.render(self.score_msg, True, 
            self.text_colour,self.fp_settings.bg_colour)
            
        #display score at top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.x = 50
        self.score_rect.top = self.screen_rect.top
        
    def show_score(self):
        """Display score on screen"""
        self.screen.blit(self.score_image, self.score_rect)
