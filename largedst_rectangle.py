def largestRectangle(h):
    # Write your code here
    maxi = 0
    for i in range(len(h)-1):
        mini1 = len(h[i:])*min(h[i:])
        mini2 = len(h[i:])* min(h[:len(h)-i])
        mini = max(mini1, mini2)
        if maxi < mini:
            maxi = mini
    return maxi
l =[8979, 4570, 6436, 5083, 7780,3269,5400,7579,2324,2116]
print(l[0:1])