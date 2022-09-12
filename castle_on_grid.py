#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid, startX, startY, goalX, goalY):
    c=0 
    queue = deque([[startX, startY,c]])
    visited = set()
    while queue:
        x, y, c = queue.popleft()
        c+=1
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            xi, yj = x, y
            while True:
                xi, yj = xi+i, yj+j
                if 0 <= xi < len(grid) and 0 <= yj < len(grid[0]) and grid[xi][yj] == ".":
                    if (xi, yj) == (goalX, goalY):
                        return c
                    elif (xi, yj) not in visited:
                        queue.append([xi, yj, c])
                        visited.add((xi, yj))
                else : 
                    break
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
        
    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
