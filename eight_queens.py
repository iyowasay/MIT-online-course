import numpy as np
import time
from os import system

n = 8  # board size
grid = np.chararray((n, n), unicode=True)
grid[:] = 'X'


def is_safe(arr, a, b):
    global n
    for _ in range(n):
        if arr[a][_] == 'Q':
            return False
    for _ in range(n):
        if arr[_][b] == 'Q':
            return False
    di = 1
    while -1 < a + di < 8 and -1 < b + di < 8:
        if arr[a+di][b+di] == 'Q':
            return False
        di += 1
    di = 1
    while -1 < a - di < 8 and -1 < b - di < 8:
        if arr[a-di][b-di] == 'Q':
            return False
        di += 1
    di = 1
    while -1 < a + di < 8 and -1 < b - di < 8:
        if arr[a+di][b-di] == 'Q':
            return False
        di += 1
    di = 1
    while -1 < a - di < 8 and -1 < b + di < 8:
        if arr[a-di][b+di] == 'Q':
            return False
        di += 1
    return True


result = []


def eight_queens(li, col, res):
    global n
    if col >= 8:
        # res.append(li)
        print(li)
        print()
        return
    else:
        for i in range(n):
            if is_safe(li, i, col):
                li[i][col] = 'Q'
                # print(grid)
                # time.sleep(0.4)
                # system('clear')
                eight_queens(li, col+1, res)
                li[i][col] = 'X'
        return


eight_queens(grid, 0, result)


for x in range(len(result)):
    print(result[x])
    print()

print(len(result))
