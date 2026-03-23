height = [1,8,6,2,5,4,8,3,7]

def maxarea(height):
    max, l, r, = 0, 0, len(height) -1
    while l < r:
        if max < (min(height[l], height[r]) * (r - l)):
            max = min(height[l], height[r]) * (r - l)
            if (min(height[l], height[r])) == height[l]:
                l += 1
            else:
                r -= 1
        elif height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max


print(maxarea(height))