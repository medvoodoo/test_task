# -*- coding: utf-8 -*-

x = 1000
y = 1000
max_sum = 25
matrix = dict()


def sum_is_good(x, y, max_sum):
    """
    Функция проверяет меньше ли сумма координат заданного числа
    """
    return sum(map(int, str(abs(x)) + str(abs(y)))) <= max_sum


def detect_or_create_position(matrix, x, y, max_sum):
    """
    Функция смотрит позицию, если она подходит и ее еще не существует,
    то ставится знак позиции для обработки
    """
    if sum_is_good(x, y, max_sum):
        if not y in matrix:
            matrix[y] = dict()
        if not x in matrix[y]:
            matrix[y][x] = 'P'

    return matrix


def transform_position(matrix, x, y, max_sum):
    """
    Алгоритм похожий на игру Жизнь.
    Помечаю клетку как обработанную X
    Пробую соседние клетки, если есть подходящая не созданная, то
    detect_or_create_position создает клетку с записью P
    """
    matrix[y][x] = 'X'
    matrix = detect_or_create_position(matrix, x + 1, y, max_sum)
    matrix = detect_or_create_position(matrix, x - 1, y, max_sum)
    matrix = detect_or_create_position(matrix, x, y + 1, max_sum)
    matrix = detect_or_create_position(matrix, x, y - 1, max_sum)
    return matrix


# создаю первую клетку, если прокатывает
matrix = detect_or_create_position(matrix, x, y, max_sum)
change = True
# цикл выполняю, пока есть хоть один переход с P на X
while change:
    change = False
    for y in list(matrix.keys()):
        for x in list(matrix[y].keys()):
            if matrix[y][x] == 'P':
                matrix = transform_position(matrix, x, y, max_sum)
                change = True

coun = 0
# здесь можно более красиво посчитать суммы, написал в лоб
for y in matrix.keys():
    coun += len(matrix[y].keys())
print (coun)
