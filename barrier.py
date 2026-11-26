import pygame 
# this takes from the python toolbox for me to use.
class Barrier: 
# this makes a class called barriers a blueprint.
    
    def __init__(self,left, top):
        self.health = 4 
        # this gives each barrier its health.
        self.alive =True 
         # this starts the alive thing and the game only draws barriers that are alive.
        self.rect = pygame.Rect ([left,top,60,40]) 
        #this decides where the rec is and its size and left and top are handed in.

    def hit (self): 
        if self.health == False:
            return 

    # this runs each time a bilet hits a barrier.
        self.health = self.health -1
    # this shows that each hit takes 1 away from the health.
        self.rect.height = self.rect.height - 10 
    #this takes away from the rec's height each times it is hit and 10 is 40 devided by 4.
        if self.health <= 0:
    # this gives a condition like if health ahs run out then what?.
            self.alive = False 
    # this shows that this spesific barrier is not alive anymore.
 
