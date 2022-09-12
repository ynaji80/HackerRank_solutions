
from copy import copy
s=""
last = []
for _ in range(int(input())):
    l = input().split()
    [ops, param] = l if len(l) == 2 else [l[0], -1]
    
    if int(ops) == 1:
        last.append(copy(s))
        s = s + param
        
    elif int(ops) == 2:
        last.append(copy(s))
        s = s[: - int(param)]
        
    elif int(ops) == 3:
        print(s[int(param)-1])
        
    elif int(ops) == 4 and last:
        s = last.pop()
        
        