import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings

import os
import json

from croissant import Croissant
from obstacle import LowerObstacle
from obstacle import UpperObstacle
from scoreboard import Scoreboard
from high_scoreboard import HighScoreboard

def run_game():
    """main program which runs the game flappy croissant"""
    pygame.init()
    
    #creates a file to store high score if there is not already one
    path = "C:/Users/joshe/Documents/flappy_croissant/high_score"
    filename = 'highest_score.json'
    for root,dirs,files in os.walk(path):
        print(files)
        if filename not in files:
            with open(filename, 'w') as f_obj:
                json.dump('0', f_obj)
            
    fp_settings = Settings()
    screen = pygame.display.set_mode(
       (fp_settings.screen_width,fp_settings.screen_height))
    pygame.display.set_caption("Flappy Croissant")
    
    #create a croissant
    crois = Croissant(fp_settings,screen)
    
    #create an upper and lower obstacles group and adds a single obstacle
    l_obstacles = Group()
    l_obst = LowerObstacle(fp_settings,screen)
    l_obstacles.add(l_obst)
    u_obstacles = Group()
    u_obst = UpperObstacle(fp_settings,screen,l_obst)
    u_obstacles.add(u_obst)
    
    #create a scoreboard and high-score board
    scoreboard = Scoreboard(fp_settings,screen)
    high_scoreboard = HighScoreboard(fp_settings,screen)
    
    #main loop for the game
    while True:
        gf.check_events(fp_settings,crois)
        
        if fp_settings.game_active:
            crois.update()
            gf.update_obstacles(fp_settings,screen,crois,l_obstacles,
                u_obstacles,scoreboard,high_scoreboard)
        
        gf.update_screen(fp_settings,screen,crois,l_obstacles,u_obstacles,
                            scoreboard,high_scoreboard)
    
run_game()
