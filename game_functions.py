import sys
import pygame
import json

from time import sleep

from croissant import Croissant
from obstacle import LowerObstacle
from obstacle import UpperObstacle
from scoreboard import Scoreboard

def check_events(fp_settings,crois):
    """checks for key presses from the user and responds"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game(fp_settings)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                crois.height = crois.rect.top
                crois.jump = True
            
def update_screen(fp_settings,screen,crois,l_obstacles,u_obstacles,scoreboard,
                    high_scoreboard):
    """updates the screen as the game is played"""
    screen.fill(fp_settings.bg_colour)
    
    #redraws all obstacles
    for obsta in l_obstacles:
        obsta.draw_obstacle()
    for obsta in u_obstacles:
        obsta.draw_obstacle()
    
    crois.blitme()
    scoreboard.show_score()
    high_scoreboard.show_score()
    
    pygame.display.flip()
    
def update_obstacles(fp_settings,screen,crois,l_obstacles,u_obstacles,
                        scoreboard,high_scoreboard):
    """Moves obstacles along the screen and adds new ones if needed"""
    
    l_obstacles.update(fp_settings)
    u_obstacles.update(fp_settings)
    
    new_obstacle(fp_settings,screen,l_obstacles,u_obstacles)
    update_score(fp_settings,crois,l_obstacles,scoreboard,high_scoreboard)
    check_croissant_hit(fp_settings,screen,crois,l_obstacles,u_obstacles,
                            scoreboard)


def new_obstacle(fp_settings,screen,l_obstacles,u_obstacles):
    """checks to see how far the obstacles have got and creates new ones"""
    for obstacle in l_obstacles:
        if obstacle.xcoord >= 300 and obstacle.xcoord < 300 + fp_settings.obstacle_speed:
            l_obst = LowerObstacle(fp_settings,screen)
            l_obstacles.add(l_obst)
            u_obst = UpperObstacle(fp_settings,screen,l_obst)
            u_obstacles.add(u_obst)
        
def update_score(fp_settings,crois,l_obstacles,scoreboard,high_scoreboard):
    """update score when obstacle is passed"""
    for obstacle in l_obstacles:
        if obstacle.xcoord + 200 >= crois.rect.x:
            if obstacle.xcoord + 200 < crois.rect.x+fp_settings.obstacle_speed:
                fp_settings.score += 1
                scoreboard.prep_score()
    
    if fp_settings.score > fp_settings.high_score:
        fp_settings.high_score = fp_settings.score
        high_scoreboard.prep_score()

def check_croissant_hit(fp_settings,screen,crois,l_obstacles,u_obstacles,
                            scoreboard):
    """checks if the croissant has hit an obstacle"""
    if pygame.sprite.spritecollideany(crois,l_obstacles):
        just_died(fp_settings,screen,crois,l_obstacles,u_obstacles,scoreboard)
    elif pygame.sprite.spritecollideany(crois,u_obstacles):
        just_died(fp_settings,screen,crois,l_obstacles,u_obstacles,scoreboard)
        
def just_died(fp_settings,screen,crois,l_obstacles,u_obstacles,scoreboard):
    """protocol for when you die in the game"""
    sleep(0.5)
    
    #remove obstacles
    l_obstacles.empty()
    u_obstacles.empty()
    
    #reset score
    fp_settings.score = 0
    scoreboard.prep_score()
    
    #recentre the croissant
    crois.center = crois.screen_rect.centery
    
    #create first obstacle for new game
    l_obst = LowerObstacle(fp_settings,screen)
    l_obstacles.add(l_obst)
    u_obst = UpperObstacle(fp_settings,screen,l_obst)
    u_obstacles.add(u_obst)
    
def quit_game(fp_settings):
    """quits game and stores high score"""
    with open(fp_settings.filename, 'w') as f_obj:
        json.dump(fp_settings.high_score, f_obj)
        sys.exit()
    
    
