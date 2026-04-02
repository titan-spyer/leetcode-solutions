letters = ["c","f","j"]
target = "a"

def solution(letters, target):
    l, r = 0, len(letters) - 1
    ans = letters[0]
    while l <= r:
        m = (r+l) // 2
        if letters[m] > target:
            ans = letters[m]
            r = m - 1
        else:
            l = m + 1
    return ans

print(solution(letters, target))