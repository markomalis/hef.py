import os
import pygame

from yoshi import Yoshi
from hef import Hef

pygame.init()

# Screen settings
width = 780
height = 516

screen = pygame.display.set_mode((width, height))
done = False
is_blue = True
x = 30
y = 30

jump_up = False
jump_down = False
jump_count = 0
jump_time = 10

clock = pygame.time.Clock()


background  = pygame.image.load('bg.jpg')
ad = pygame.image.load('ad.png')

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

yoshi = Hef(screen)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    yoshi.update()
    
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    yoshi.render()
    
    pygame.display.flip()
    clock.tick(60)
