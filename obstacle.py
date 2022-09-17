import pygame
from pygame.sprite import Sprite
import random

class LowerObstacle(Sprite):
    """Creates a lower obstacle class for the croissant to dodge"""
    
    def __init__(self,fp_settings,screen):
        """initialises the obstacle"""
        super().__init__()
        self.fp_settings = fp_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.obstacle_height = random.randint(50,300)
        
        #create an obstacle at (0,0) and move to bottom right
        self.rect = pygame.Rect(0,0,200,self.obstacle_height)
        self.rect.x = self.screen_rect.width 
        self.rect.y = self.screen_rect.height - self.obstacle_height
        
        #stores the x co-ordinate as a float
        self.xcoord = float(self.rect.x)
        
        #obstacle colour
        self.colour = fp_settings.obstacle_colour
        
    def update(self,fp_settings):
        """moves the obstacle along the screen"""
        self.xcoord -= fp_settings.obstacle_speed
        self.rect.x = self.xcoord
        
    def draw_obstacle(self):
        """Draws the obstacle to the screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)
        
class UpperObstacle(Sprite):
    """Creates a lower obstacle class for the croissant to dodge"""
    
    def __init__(self,fp_settings,screen,l_obst):
        """initialises the obstacle"""
        super().__init__()
        self.fp_settings = fp_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        #create an obstacle at (0,0) and move to top right
        self.rect = pygame.Rect(0,0,200,
            self.screen_rect.height-l_obst.obstacle_height-310)
        self.rect.x = self.screen_rect.width 
        
        #stores the x co-ordinate as a float
        self.xcoord = float(self.rect.x)
        
        #obstacle colour
        self.colour = fp_settings.obstacle_colour
        
    def update(self,fp_settings):
        """moves the obstacle along the screen"""
        self.xcoord -= fp_settings.obstacle_speed
        self.rect.x = self.xcoord
        
    def draw_obstacle(self):
        """Draws the obstacle to the screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)
    
