#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    if len(s) % 2 !=0:
        return "NO"
    
    pairs = {
        "}" : "{",
        "]" : "[",
        ")" : "("
    }
    
    stack = []
    for elm in s:
        if elm not in pairs :
            stack.append(elm)
        elif elm in pairs and not stack:
            return "NO"
        elif pairs.get(elm) == stack[-1] and len(stack) > 0:
            stack.pop()
    
    return "YES" if not stack else "NO"
   
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
