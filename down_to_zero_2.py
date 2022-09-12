#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'downToZero' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
weight = [0]*(10**6+1)
queue = deque()
queue.append(0)
while queue:
    n = queue.popleft()
    c = weight[n]+1
    step = n+1
    if n < len(weight)-1 and weight[step] == 0:
        weight[step] = c
        queue.append(step)
    
    for i in range(2,n+1):
        step = n*i
        if step >= len(weight):
            break
        if weight[step] == 0:
            weight[step] = c
            queue.append(step)



def downToZero(n):
    # Write your code here
    if n<=3:
        return n
    return weight[n]
        
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
