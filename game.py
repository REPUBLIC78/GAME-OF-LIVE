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

yes = int(input("random Y/N = 1/0? : "))
if yes:
    for x in range(0, size_place):
        for y in range(0, size_place):
            game_place[x][y] = random.randrange(0 , 2)
            
# ВВОД ПРАВИЛ

game_rule_b = input('ВВЕДИТЕ ПРАВИЛО ДЛЯ МЕРТВЫХ: ')
game_rule_s = input('ВВЕДИТЕ ПРАВИЛО ДЛЯ ЖИВЫХ  : ')

b = [int(i) for i in game_rule_b]
s = [int(i) for i in game_rule_s]
    
# РИСОВКА

place_pixel(game_place, 50, 50)
place_pixel(game_place, 51, 50)
place_pixel(game_place, 51, 51)
place_pixel(game_place, 52, 51)
place_pixel(game_place, 52, 53)

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
            
            sum_live = game_place[x - 1][y - 1] + game_place[x][y - 1] + game_place[x + 1][y - 1] + game_place[x - 1][y] + game_place[x + 1][y] + game_place[x - 1][y + 1] + game_place[x][y + 1] + game_place[x + 1][y + 1]
            # ПЕРВОЕ ПРАВИЛО ДЛЯ МЕРТВЫХ КЛЕТОК
            if (game_place[x][y] == 0) and (sum_live in b):
                place_pixel(game_place_bufer, x, y)
            # ВТОРОЕ ПРАВИЛО ДЛЯ ЖИВЫХ КЛЕТОК
            elif (game_place[x][y] == 1) and (sum_live in s):
                place_pixel(game_place_bufer, x, y)
            else:
                pop_pixel(game_place_bufer, x, y)
    
    game_place = game_place_bufer
    
    game_place_bufer = []
    
    # ОБНОВЛЕНИЕ БУФЕРА
    
    game_place_bufer = [0] * size_place
    
    for i in range(size_place): 
        game_place_bufer[i] = [0] * size_place
        
    # ИЗМЕНЕНИЕ ЦВЕТА
    
    color = 255
    
    color = color - 1
    if color == 0:
        color = 255
    
    # РЕНДЕР ПОЛЯ
    
    for x in range(0, size_place):
        for y in range(0, size_place):
            if game_place[x][y] == 1:
                pygame.draw.rect(screen, (255, 255, 255), (x * size_mult, y * size_mult, x * size_mult + size_mult, y * size_mult + size_mult))
            if game_place[x][y] == 0:
                pygame.draw.rect(screen, (0, 0, 0), (x * size_mult, y * size_mult, x * size_mult + size_mult, y * size_mult + size_mult))
                
    pygame.display.flip()
