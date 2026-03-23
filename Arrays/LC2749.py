def minOperations(num1, num2):
    for k in range(1, 61):
        x = num1 - k * num2
        if x < 0:
            break
        if bin(x).count('1') <= k:
            return k
    return -1
