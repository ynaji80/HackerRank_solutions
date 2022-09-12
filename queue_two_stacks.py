q = int(input())
stack=[]
stack2=[]
for _ in range(q):
        l = list(map(int,input().split()))
        type= int(l[0])
        if type == 1:
            x= int(l[1])
            stack.append(x)
        elif type == 2:
            if not stack2:
                while stack :
                    stack2.append(stack.pop())
            stack2.pop()
        elif type == 3:
            print(stack2[-1] if stack2 else stack[0])
