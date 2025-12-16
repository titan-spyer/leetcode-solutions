# Longest Repeating Character Replacement
s = "ABAB" 
k = 2

def answer(s, k):
    left = 0
    chunks = set()
    ans = 0
    # max_freq = 0
    for r in range(len(s) - 1):
        while s[r] in chunks:
            if ((r - left + 1) - ans) <= k:
                chunks.discard(s[left])
                left += 1
        if (r - left + 1) - ans <= k:
            chunks.add(s[r])
            ans = max(ans, r - left + 1)
        
    return ans

print(answer(s, k))