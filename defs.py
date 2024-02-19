

# УСТАНОВКА ПИКСЕЛЕЙ
def place_pixel(game_place, x, y):
    game_place[x][y] = 1

# УДАЛЕНИЕ ПИКСЕЛЯ
def pop_pixel(game_place, x, y):
    game_place[x][y] = 0