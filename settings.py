import json

class Settings():
    """Class containing all settings for flappy croissant"""
    
    def __init__(self):
        """initialise the settings for the game"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230,230,230)
        
        #obstacle settings
        self.obstacle_colour = (1,50,32)
        self.obstacle_speed = 0.7
        
        #file to store high score
        self.filename = "high_score/highest_score.json"
        
        self.initialise_dynamic_settings()
        
    def initialise_dynamic_settings(self):
        """Initialises settings that can change throughout the game"""
        self.game_active = True
        self.score = 0
        with open(self.filename, 'r') as f_obj:
            self.high_score = int(json.load(f_obj))
