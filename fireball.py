import pygame

class Fireball:
    fireball_img_path = 'fireball.png'
    fireball_x_offset = 80
    fireball_y_offset = 40
    
    def __init__(self, x, y, screen):
        self.x = x + self.fireball_x_offset
        self.y = y + self.fireball_y_offset
        self.fireball = self.fireball = pygame.image.load(self.fireball_img_path)
        self.screen = screen    
            
    def update(self):
        self.x += 5
        
    def render(self):
        self.screen.blit(self.fireball, (self.x, self.y))
