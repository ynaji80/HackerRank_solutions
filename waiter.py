#!/bin/python3

import math
import os
import random
import re
import sys
from copy import copy
#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#
primes = [2,3]

for n in range (4, 10000):
    i= 2
    prime = 1
    while i <= n//2 :
        if n % i == 0:
            prime = 0
            break
        i+=1
    if prime == 1:
        primes.append(n)

    
def waiter(number, q):
    # Write your code here
    
    
    answer = []
    for i in range(q):
        a = []
        b = []
        for num in number:
            if num % primes[i] == 0:
                answer.append(num)
            else:
                a.append(num)
        number = list(reversed(a))
    
    answer += a
    return answer
        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
