import pygame

class Flipflop:
    flipflop_img_path = 'ad.png'
    flipflop_x_offset = 50
    flipflop_y_offset = 20
    flipflop_rotation = 0
    
    def __init__(self, x, y, screen):
        self.x = x + self.flipflop_x_offset
        self.y = y + self.flipflop_y_offset
        self.flipflop = self.flipflop = pygame.image.load(self.flipflop_img_path)
        self.screen = screen    
            
    def update(self):
        self.x += 5
        
    def render(self):
        img = pygame.transform.rotate(self.flipflop, self.flipflop_rotation)
        self.screen.blit(img, (self.x, self.y))
        self.flipflop_rotation -= 11
