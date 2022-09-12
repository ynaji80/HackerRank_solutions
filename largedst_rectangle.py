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
