import pygame

from flipflop import Flipflop

class Hef:
    hef_right_img_path = 'hef.png'
    hef_left_img_path = 'hef.png'
    
    jump_up = False
    jump_down = False
    jump_count = 0
    jump_time = 10
    
    fireball_offset = 100
    fireballs = []
    fired = False
    
    def __init__(self, screen):
        self.hef_right = pygame.image.load(self.hef_right_img_path)
        self.hef_left = pygame.image.load(self.hef_left_img_path)
        self.hef = self.hef_right
        
        self.x = 0
        self.y = 300
        self.width = self.hef.get_width
        self.height = self.hef.get_height
        
        self.screen = screen
        
        
    def update(self):
        #################
        # Handle events #
        #################
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            self.y -= 3
    
        if pressed[pygame.K_DOWN]: 
            self.y += 3
        
        if pressed[pygame.K_LEFT]: 
            self.x -= 3
            self.hef = self.hef_left
        
        if pressed[pygame.K_RIGHT]: 
            self.x += 3
            self.hef = self.hef_right
            
        if pressed[pygame.K_f]:
            if not self.fired:
                self.fired = True
                self.fireballs.append(Flipflop(self.x,self.y, self.screen))
        else:
            self.fired = False
            
        if pressed[pygame.K_SPACE] and not (self.jump_up or self.jump_down): 
            self.jump_up = True
            
        
        ##################
        # Handle changes #
        ##################
        if self.jump_up:
            self.y -= 6
            
        if self.jump_down:
            self.y += 6
        
        if self.jump_down and self.jump_count>0:
            self.jump_count -= 1
        elif self.jump_down and self.jump_count<=0:
            self.jump_down = False
        
        if self.jump_up and self.jump_count<self.jump_time:
            self.jump_count += 1
        elif self.jump_up and self.jump_count>=self.jump_time:
            self.jump_up = False
            self.jump_down = True
            
        for fireball in self.fireballs:
            fireball.update()
    
            
    def render(self):
        self.screen.blit(self.hef, (self.x, self.y))
        for fireball in self.fireballs:
            if fireball.x > self.screen.get_width():
                self.fireballs.remove(fireball)
            else:
                fireball.render()
