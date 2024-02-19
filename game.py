import time
from defs import *
import pygame
import random

# СОЗДАНИЕ ПОЛЯ 
size_place = 200
         
game_place = [0] * size_place
 
for i in range(size_place): 
    game_place[i] = [0] * size_place

# РАНДОМ ПОЛЕ 

# for x in range(0, size_place):
#     for y in range(0, size_place):
#         game_place[x][y] = random.randrange(0, 2) * random.randrange(0, 2) * random.randrange(0, 2)  * random.randrange(0, 2) * random.randrange(0, 2) * random.randrange(0, 2)
            
# РИСОВКА

place_pixel(game_place, 50, 50)
place_pixel(game_place, 51, 50)
place_pixel(game_place, 50, 51)
place_pixel(game_place, 51, 51)

# МАСШТАБ
size_mult = 5

# ПОЛЕ
pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
# БУФЕР МАССИВ
game_place_bufer = [0] * size_place

for i in range(size_place): 
    game_place_bufer[i] = [0] * size_place
# ЦИКЛ ОТРИСОВКИ

while not done:
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
        
    # ОБНОВЛЕНИЕ ПО ПРАВИЛАМ 
    for x in range(1, size_place - 1):
        for y in range(1, size_place - 1):
            
            # B3/S12345
            # B35678/S5678
            # B1/S012345678
            # B234/S
            # ПЕРВОЕ ПРАВИЛО ДЛЯ МЕРТВЫХ КЛЕТОК
            if (game_place[x][y] == 0) and (((game_place[x - 1][y - 1] + game_place[x][y - 1] + game_place[x + 1][y - 1] + \
                game_place[x - 1][y] + game_place[x + 1][y] + \
                game_place[x - 1][y + 1] + game_place[x][y + 1] + game_place[x + 1][y + 1]) >= 2) and ((game_place[x - 1][y - 1] + game_place[x][y - 1] + game_place[x + 1][y - 1] + \
                game_place[x - 1][y] + game_place[x + 1][y] + \
                game_place[x - 1][y + 1] + game_place[x][y + 1] + game_place[x + 1][y + 1]) <= 4)):

                place_pixel(game_place_bufer, x, y)
                
            
            # ВТОРОЕ ПРАВИЛО ДЛЯ ЖИВЫХ КЛЕТОК
            # elif (game_place[x][y] == 1) and (((game_place[x - 1][y - 1] + game_place[x][y - 1] + game_place[x + 1][y - 1] + \
            #     game_place[x - 1][y] + game_place[x + 1][y] + \
            #     game_place[x - 1][y + 1] + game_place[x][y + 1] + game_place[x + 1][y + 1]) >= 0)):
                
            #     place_pixel(game_place_bufer, x, y)
            else:
                pop_pixel(game_place_bufer, x, y)
    
    game_place = game_place_bufer
    
    game_place_bufer = []
    
    # ОБНОВЛЕНИЕ БУФЕРА
    game_place_bufer = [0] * size_place
    
    for i in range(size_place): 
        game_place_bufer[i] = [0] * size_place
        
    # РЕНДЕР ПОЛЯ
    for x in range(0, size_place):
        for y in range(0, size_place):
            if game_place[x][y] == 1:
                pygame.draw.rect(screen, (0, 255, 0), (x * size_mult, y * size_mult, x * size_mult + size_mult, y * size_mult + size_mult))
            if game_place[x][y] == 0:
                pygame.draw.rect(screen, (0, 0, 0), (x * size_mult, y * size_mult, x * size_mult + size_mult, y * size_mult + size_mult))
                
    pygame.display.flip()
