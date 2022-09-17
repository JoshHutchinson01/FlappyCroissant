import pygame

class Croissant():
    """Creates a croissant class"""
    
    def __init__(self,fp_settings,screen):
        """initialises the croissant"""
        self.fp_settings = fp_settings
        self.screen = screen
        
        #Load the croissant image and get its rect
        self.image_big = pygame.image.load('images/croissant.bmp')
        self.image = pygame.transform.scale(self.image_big, (80,80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #place a new croissant in the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        #create float value for the y coordinate of the croissant
        self.center= float(self.rect.centery)
        
        #set the jump marker to false
        self.jump = False
        self.height = 0
        
    def update(self):
        """updates the position of the croissant based on input"""
        if self.jump and self.height - self.rect.top < 200 and self.rect.top > 0:
            self.center -= 2
        else:
            self.jump = False
            self.center += 0.35
        
        #update rect using self.center
        self.rect.centery = self.center
        
    def blitme(self):
        """Draw the croissant at its current location"""
        self.screen.blit(self.image, self.rect)
